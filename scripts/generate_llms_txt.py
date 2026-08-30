#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt into the built site directory.

Reads section structure from zensical.toml [[project.nav]] and per-page
titles/descriptions from OKF frontmatter, then writes:

  <out>/llms.txt       llmstxt.org discovery file linking raw .md sources
  <out>/llms-full.txt  concatenated page bodies with source separators

Runs post-build (locally or in CI): the outputs land next to the rendered
HTML so https://.../intro-gpt/llms.txt covers every URL beneath it.

Usage: python3 scripts/generate_llms_txt.py \
           [--config zensical.toml] [--docs docs] [--out site] [--strict]
"""

import argparse
import sys
import tomllib
from pathlib import Path

import yaml


def parse_frontmatter(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            try:
                meta = yaml.safe_load(text[4:end])
            except yaml.YAMLError:
                meta = None
            if isinstance(meta, dict):
                return meta, text[end + 5:]
    return {}, text


def flatten_nav(nav):
    """[[project.nav]] is a list of single-key tables: {Section: [entries]}.
    Entries are {Title = "path.md"} tables, bare path strings, or nested
    lists of the same. Yields (section, [(title, relpath), ...])."""
    sections = []
    for table in nav:
        for section, entries in table.items():
            pages = []
            _collect(entries, pages)
            sections.append((section, pages))
    return sections


def _collect(entries, out):
    if isinstance(entries, str):
        out.append((None, entries))
    elif isinstance(entries, list):
        for entry in entries:
            _collect(entry, out)
    elif isinstance(entries, dict):
        for title, value in entries.items():
            if isinstance(value, str):
                out.append((title, value))
            else:
                _collect(value, out)


def md_url(site_url: str, rel: str) -> str:
    return f"{site_url}/{rel}"


def html_url(site_url: str, rel: str) -> str:
    if rel == "index.md":
        return site_url + "/"
    return f"{site_url}/{rel[:-3]}/"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="zensical.toml")
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--out", default="site")
    ap.add_argument("--strict", action="store_true",
                    help="fail on missing descriptions or unnavigated pages")
    args = ap.parse_args()

    cfg = tomllib.loads(Path(args.config).read_text(encoding="utf-8"))["project"]
    site_url = cfg["site_url"].rstrip("/")
    docs = Path(args.docs)
    out = Path(args.out)
    problems = []

    sections = flatten_nav(cfg.get("nav", []))

    # Coverage: docs pages missing from nav go into a trailing "Other" section,
    # except OKF-reserved files (log.md), which are deliberately unnavigated
    # and get a "Meta" section without a warning.
    in_nav = {rel for _, pages in sections for _, rel in pages}
    reserved, extras = [], []
    for path in sorted(docs.rglob("*.md")):
        rel = str(path.relative_to(docs))
        if rel in in_nav or any(
            part.startswith(("#", ".#")) or part.endswith("~") for part in path.parts
        ):
            continue
        if rel == "log.md":
            reserved.append((None, rel))
        else:
            extras.append((None, rel))
    if extras:
        problems.append(f"pages not in nav (added under 'Other'): {[r for _, r in extras]}")
        sections.append(("Other", extras))
    if reserved:
        sections.append(("Meta", reserved))

    lines = [f"# {cfg['site_name']}", "", f"> {cfg['site_description']}", ""]
    full = [f"# {cfg['site_name']} — full content", "",
            f"> {cfg['site_description']}", ""]

    for section, entries in sections:
        lines += [f"## {section}", ""]
        for nav_title, rel in entries:
            meta, body = parse_frontmatter((docs / rel).read_text(encoding="utf-8"))
            title = meta.get("title") or nav_title or rel
            desc = str(meta.get("description") or "").strip().replace("\n", " ")
            if not desc:
                problems.append(f"{rel}: missing description")
            lines.append(f"- [{title}]({md_url(site_url, rel)}): {desc}")

            full += [
                "",
                "-" * 78,
                f"# {title}",
                f"URL: {html_url(site_url, rel)}",
                f"Source: {md_url(site_url, rel)}",
                "-" * 78,
                "",
                body.strip(),
            ]
        lines.append("")

    out.mkdir(parents=True, exist_ok=True)
    (out / "llms.txt").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (out / "llms-full.txt").write_text("\n".join(full).rstrip() + "\n", encoding="utf-8")

    total = sum(len(entries) for _, entries in sections)
    print(f"Wrote {out / 'llms.txt'} ({total} pages, {len(sections)} sections) "
          f"and {out / 'llms-full.txt'}")
    for problem in problems:
        print(f"WARNING: {problem}", file=sys.stderr)
    if problems and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
