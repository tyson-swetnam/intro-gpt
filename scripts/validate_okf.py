#!/usr/bin/env python3
"""Validate OKF v0.2 frontmatter across the docs/ bundle.

Checks every markdown page for conformance with the Open Knowledge Format
(https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
plus this site's field policy (see CLAUDE.md). Prints one line per finding as
"path: [ERROR|WARN] message" and exits 1 if any ERROR is found (or any WARN
when --strict is given).

Usage: python3 scripts/validate_okf.py [docs] [--strict]
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

SITE_URL = "https://tyson-swetnam.github.io/intro-gpt"
OKF_VERSION = "0.2"

TYPES = {
    "Index",
    "Overview",
    "Setup Guide",
    "Prompting Guide",
    "Education Guide",
    "Research Guide",
    "Ethics Guide",
    "Tutorial",
    "Log",
}

# Controlled tag vocabulary — the single source of truth. Grow deliberately.
TAGS = {
    # section/kind
    "workshop", "setup", "prompt-engineering", "education", "research",
    "ethics", "tutorial",
    # vendor/platform
    "anthropic", "openai", "google", "microsoft", "github", "huggingface",
    # topic
    "pricing", "productivity", "coding", "data-analysis", "agentic-ai",
    "mcp", "rag", "local-llm", "academic-integrity", "bias", "legal",
    "sustainability", "gis", "public-health",
}

STATUS = {"draft", "stable", "deprecated"}

ACTOR_RE = re.compile(
    r"^(human:[A-Za-z0-9_.@-]+"
    r"|process:[A-Za-z0-9_./-]+"
    r"|[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)$"
)
SHORTCODE_RE = re.compile(r":(material|fontawesome|simple|octicons|lucide)[-_a-z0-9]*:")
LINK_RE = re.compile(r"\]\(([^)#?\s]+\.md)[^)]*\)")
LOG_HEADING_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})$")
LOG_CONVENTION_RE = re.compile(r"\*\*(Creation|Update|Deprecation)\*\*")

JUNK_PREFIXES = ("#", ".#")


def is_junk(path: Path) -> bool:
    return any(part.startswith(JUNK_PREFIXES) or part.endswith("~") for part in path.parts)


def split_frontmatter(text: str):
    """Return (meta dict, body) or (None, None) if no parseable block."""
    if not text.startswith("---\n"):
        return None, None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, None
    try:
        meta = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return None, None
    if not isinstance(meta, dict):
        return None, None
    return meta, text[end + 5:]


def canonical_url(rel: str) -> str:
    if rel == "index.md":
        return SITE_URL + "/"
    return f"{SITE_URL}/{rel[:-3]}/"


def parse_iso(value):
    """Parse an ISO-8601 string; return datetime or None."""
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


class Reporter:
    def __init__(self):
        self.errors = 0
        self.warnings = 0

    def error(self, path, msg):
        self.errors += 1
        print(f"{path}: [ERROR] {msg}")

    def warn(self, path, msg):
        self.warnings += 1
        print(f"{path}: [WARN] {msg}")


def check_actor_event(rep, rel, field, event, require_keys=True):
    if not isinstance(event, dict):
        rep.error(rel, f"{field} must be a mapping with by/at")
        return
    by = event.get("by")
    at = event.get("at")
    if require_keys and (by is None or at is None):
        rep.error(rel, f"{field} requires both by and at")
        return
    if by is not None and (not isinstance(by, str) or not ACTOR_RE.match(by)):
        rep.error(rel, f"{field}.by {by!r} is not a valid OKF actor")
    if at is not None and parse_iso(at) is None:
        rep.error(rel, f"{field}.at {at!r} is not an ISO-8601 string (quote it in YAML)")


def check_file(rep, docs: Path, path: Path):
    rel = str(path.relative_to(docs))
    meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if meta is None:
        rep.error(rel, "missing or unparseable YAML frontmatter block")
        return None

    is_log = rel == "log.md"

    # type
    okf_type = meta.get("type")
    if not isinstance(okf_type, str) or not okf_type.strip():
        rep.error(rel, "frontmatter must contain a non-empty 'type'")
    elif okf_type not in TYPES:
        rep.warn(rel, f"type {okf_type!r} not in the site taxonomy")

    # title
    title = meta.get("title")
    if not isinstance(title, str) or not title.strip():
        rep.error(rel, "missing 'title'")
    elif SHORTCODE_RE.search(title):
        rep.error(rel, "title must not contain icon shortcodes")

    # description
    desc = meta.get("description")
    if not isinstance(desc, str) or not desc.strip():
        rep.error(rel, "missing 'description'")
    else:
        if len(desc) > 300:
            rep.warn(rel, f"description is {len(desc)} chars (>300)")
        if "](" in desc or SHORTCODE_RE.search(desc):
            rep.warn(rel, "description should be plain text (no markdown/shortcodes)")
        # Zensical's native <meta name="description"> interpolates without
        # escaping (MiniJinja autoescape is off), so these break the attribute.
        unsafe = [c for c in '"<>' if c in desc]
        if unsafe:
            rep.error(rel, f"description contains attribute-breaking characters: {unsafe}")

    # resource
    resource = meta.get("resource")
    expected = canonical_url(rel)
    if resource != expected:
        rep.error(rel, f"resource {resource!r} != canonical {expected!r}")

    # tags
    tags = meta.get("tags")
    if not is_log:
        if not isinstance(tags, list) or not tags or not all(isinstance(t, str) for t in tags):
            rep.error(rel, "tags must be a non-empty list of strings")
        else:
            unknown = [t for t in tags if t not in TAGS]
            if unknown:
                rep.warn(rel, f"tags not in vocabulary: {unknown}")

    # sources (optional)
    sources = meta.get("sources")
    if sources is not None:
        if not isinstance(sources, list) or not sources:
            rep.error(rel, "sources, when present, must be a non-empty list")
        else:
            for i, src in enumerate(sources):
                if not isinstance(src, dict) or not isinstance(src.get("resource"), str):
                    rep.error(rel, f"sources[{i}] must be a mapping with a 'resource'")
                    continue
                if not re.match(r"^https?://", src["resource"]):
                    rep.error(rel, f"sources[{i}].resource must be an http(s) URL")
                lm = src.get("last_modified")
                if lm is not None and parse_iso(lm) is None:
                    rep.error(rel, f"sources[{i}].last_modified is not ISO-8601")

    # trust (not required on log.md)
    if not is_log:
        generated = meta.get("generated")
        if generated is None:
            rep.error(rel, "missing 'generated'")
        else:
            check_actor_event(rep, rel, "generated", generated)

        verified = meta.get("verified")
        if verified is None:
            rep.error(rel, "missing 'verified'")
        elif not isinstance(verified, list) or not verified:
            rep.error(rel, "verified must be a non-empty list")
        else:
            for i, event in enumerate(verified):
                check_actor_event(rep, rel, f"verified[{i}]", event)

        status = meta.get("status")
        if status not in STATUS:
            rep.error(rel, f"status {status!r} must be one of {sorted(STATUS)}")

    # lifecycle
    stale = meta.get("stale_after")
    if stale is not None:
        dt = parse_iso(stale)
        if dt is None:
            rep.error(rel, "stale_after is not an ISO-8601 string")
        elif dt.tzinfo and dt < datetime.now(timezone.utc):
            rep.warn(rel, f"page is stale (stale_after {stale})")

    return meta, body


def check_links(rep, docs: Path, path: Path, body: str):
    """WARN on internal .md link targets that don't resolve to a real page."""
    rel = str(path.relative_to(docs))
    for match in LINK_RE.finditer(body):
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("/"):
            resolved = docs / target.lstrip("/")
        else:
            resolved = path.parent / target
        try:
            resolved.resolve().relative_to(docs.resolve())
        except ValueError:
            rep.warn(rel, f"link target escapes docs/: {target}")
            continue
        if not resolved.exists():
            rep.warn(rel, f"broken internal link: {target}")


def check_bundle(rep, docs: Path, pages: dict, strict: bool):
    # okf_version on bundle root
    root_meta = pages.get("index.md", (None, None))[0]
    if root_meta is None or root_meta.get("okf_version") != OKF_VERSION:
        rep.error("index.md", f'bundle root must declare okf_version: "{OKF_VERSION}"')

    # index link coverage of every non-reserved page
    if root_meta is not None:
        body = pages["index.md"][1] or ""
        linked = set()
        for match in LINK_RE.finditer(body):
            target = match.group(1)
            if not target.startswith(("http://", "https://")):
                linked.add(target.lstrip("./"))
        for rel in sorted(pages):
            if rel in ("index.md", "log.md"):
                continue
            if rel not in linked:
                msg = f"not linked from the bundle index listing: {rel}"
                (rep.error if strict else rep.warn)("index.md", msg)

    # log.md structure
    log_entry = pages.get("log.md")
    if log_entry and log_entry[1] is not None:
        dates = []
        for line in log_entry[1].splitlines():
            m = LOG_HEADING_RE.match(line.strip())
            if m:
                dates.append(m.group(1))
            elif line.strip().startswith("- ") and not LOG_CONVENTION_RE.search(line):
                rep.warn("log.md", f"bullet without **Creation**/**Update**/**Deprecation**: {line.strip()[:60]}")
        if dates != sorted(dates, reverse=True):
            rep.error("log.md", "date headings must be strictly newest-first")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("docs", nargs="?", default="docs", help="bundle root (default: docs)")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    docs = Path(args.docs)
    if not docs.is_dir():
        print(f"{docs}: [ERROR] not a directory")
        return 1

    rep = Reporter()
    pages = {}
    for path in sorted(docs.rglob("*.md")):
        if is_junk(path.relative_to(docs)):
            continue
        result = check_file(rep, docs, path)
        if result is not None:
            pages[str(path.relative_to(docs))] = result
            check_links(rep, docs, path, result[1])

    check_bundle(rep, docs, pages, args.strict)

    print(f"Checked {len(pages)} pages: {rep.errors} error(s), {rep.warnings} warning(s)")
    if rep.errors or (args.strict and rep.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
