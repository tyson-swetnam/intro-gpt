# Public Health AI Lab — Triage, Surveillance, Abstraction

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

This lab assumes you've completed the [Prompt Engineering Deep Dive](../../prompts.md). Here we apply four advanced techniques — **few-shot learning**, **prompt chaining**, **chain-of-thought**, and **structured output** — to three real public-health workflows.

Each exercise follows the same shape:

1. A **bad prompt** that fails in a specific, instructive way.
2. A **better prompt** that introduces an anchor technique from `prompts.md`.
3. A **best prompt** that layers a second technique on top.

You finish with three artifacts and three sets of compared outputs that show what each technique actually buys you. (The bad → better → best progression mirrors the [Basic / Better / Best example](../../prompts.md#getting-started-basic-prompt-structure) at the top of the Deep Dive — applied end-to-end, with public-health stakes.)

!!! Example "What you'll build (60–90 min)"
    Three artifacts plus their bad/better/best comparisons:

    1. An **SMS triage classifier** with confidence scores
    2. A **one-page outbreak brief** synthesized via a reasoning chain
    3. A **structured chart-abstraction record set** with calibrated abstention

## Prerequisites

| ✔︎ | Requirement | Notes |
|---|-------------|-------|
|   | Read [Prompt Engineering](../../prompts.md) first | CRAFT, few-shot, prompt chaining |
|   | Access to a chat-style LLM | Claude, ChatGPT, or Gemini in any browser |
|   | 60–90 min | All exercises run in a single chat session |

A note on running the comparisons: open a **fresh chat** for each version (1A, 1B, 1C). LLMs that remember the prior context will "cheat" — they'll silently apply lessons from the better prompt to the bad one. Fresh chats are how you actually see the technique buy you something.

---

## Exercise 1 — SMS Symptom Triage (~30 min)

**Anchor technique:** [Few-shot learning](../../prompts.md#5-using-examples-few-shot-learning).
**Gap-filling technique:** Structured output with confidence scores.

**Scenario.** You run a community SMS health line for a rural district. Eight messages arrived overnight. You need to sort them — *urgent*, *route-to-clinic*, *misinformation*, *not-actionable* — before the 8 a.m. clinic huddle.

??? Clipboard "Inbound messages (used in all three versions below)"

    ```text
    1. fever 3 days, headache, neck stiff, light hurts my eyes
    2. can my child take amoxicillin if she is allergic to penicillin
    3. drinking bleach cures malaria right
    4. test
    5. cough 2 weeks getting worse, blood in sputum, lost weight
    6. when does the family planning clinic open
    7. my husband fell and cannot move his left side, started 30 minutes ago
    8. is paracetamol safe in pregnancy
    ```

### 1A — The bad prompt (zero-shot, vague)

```text
I run an SMS health line. Classify these 8 messages as urgent,
route-to-clinic, misinformation, or not-actionable.

[paste the 8 messages]
```

!!! Failure "What goes wrong"
    The model has no anchor for what *urgent* means in **this** context. Common failure modes you'll see across LLMs:

    - Message 1 (meningitis-suspect: fever + headache + neck stiff + photophobia) classified as **route-to-clinic** instead of **urgent**.
    - Message 3 ("drinking bleach cures malaria right") read as a *question* and answered with medical advice, instead of classified as **misinformation**.
    - Message 7 (acute stroke onset) sometimes correctly tagged urgent, sometimes not — inconsistent across reruns.

    The model doesn't know your operational definition. It defaults to a generic chatbot register.

### 1B — Better: add few-shot examples

The fix is to *show* the model what each category looks like, not just name them. Three labeled examples is usually enough to anchor a four-class classifier.

```text
I run an SMS health line. Classify each inbound message into one of:
  - URGENT: symptoms that may need same-day medical attention
  - ROUTE-TO-CLINIC: non-urgent but should see a clinician within a week
  - MISINFORMATION: a factual claim that, if acted on, could cause harm
  - NOT-ACTIONABLE: greeting, test, irrelevant, or unintelligible

Examples:
  "my baby has been vomiting for two days and won't drink water"
    -> URGENT (dehydration risk in infant)
  "is it true the new vaccine has a microchip"
    -> MISINFORMATION (false claim circulating in community)
  "good morning sister"
    -> NOT-ACTIONABLE (greeting only)

Output: a markdown table with columns | # | Message | Class | Rationale |.

Now classify these 8 messages:
[paste the 8 messages]
```

!!! Success "What changed"
    With three anchored examples, the meningitis-suspect message at #1 reliably lands in **URGENT** across reruns. Message 3 is recognized as **MISINFORMATION** rather than answered. The technique you applied is **few-shot learning** — see [prompts.md §5](../../prompts.md#5-using-examples-few-shot-learning).

### 1C — Best: structured output with confidence scores

The triage table from 1B is good, but it doesn't surface the cases you most need to spot-check — the *low-confidence* ones. Add a JSON schema that demands an explicit confidence score and reasoning.

```text
[same as 1B prompt above, replace the Output line with:]

Output: a JSON array. Each element must conform to this schema:
{
  "id": integer,
  "message": string,
  "classification": "URGENT" | "ROUTE-TO-CLINIC" | "MISINFORMATION" | "NOT-ACTIONABLE",
  "rationale": string (max 15 words),
  "confidence_0to100": integer,
  "needs_human_review": boolean (true if confidence_0to100 < 80
                                  OR classification is URGENT)
}

Return ONLY the JSON array, no preamble or commentary.
```

!!! Success "What changed"
    Now your downstream code (or a human reviewer with limited time) can filter for `needs_human_review == true` and triage **only** those messages. URGENT cases auto-flag regardless of confidence — a deliberate safety bias. The technique you applied is **structured output** — under-covered in `prompts.md` but pervasive in production LLM systems. The pattern (schema + explicit abstention/confidence field) is what production triage systems actually deploy.

### Reflection

Most learners find that **1B does the heavy lifting** — adding examples is the single biggest quality jump. **1C is what makes the system operable at scale**: confidence scores let one nurse review 50 borderline cases in the time it would take to read all 200 inbound messages.

**Real-world echo.** Cambodia's [115 Hotline](https://endingpandemics.org/){target=_blank}, Penn's COVID Chatbot, and Yale's viral-triage prototype all run variants of this pipeline. None of them route any message to "ignore" without a human spot-check on the borderline class.

**Bias note.** This classifier inherits any bias in the training data of the underlying LLM, plus any bias in the few-shot examples *you* chose. Rerun the better/best prompts with code-switched English/Spanish messages and watch what changes — see [Bias and Discrimination → Concrete examples in public health](../../bias.md#concrete-examples-in-public-health).

---

## Exercise 2 — Outbreak Signal Synthesis (~30 min)

**Anchor technique:** [Prompt chaining](../../prompts.md#4-prompt-chaining).
**Gap-filling technique:** Chain-of-thought (explicit "think step by step" reasoning).

**Scenario.** You are the duty epidemiologist. Three free-text reports filed this week from village health volunteers, plus a small structured case-count table from the district lab. Your supervisor wants a one-page early-warning brief on her desk by lunch.

??? Clipboard "Source data (used in all three versions below)"

    ```text
    [Village A — Tue]
    "This week we have seen many people with fever and rash, mostly children
    under 10. The school sent home about 20 kids. A goat in the same compound
    also died but the family ate it. Rains are heavy and the well is muddy."

    [Village B — Wed]
    "Three adults with severe diarrhea since Sunday, two were hospitalized.
    The shared pump near the market broke last week and people are drawing
    from the river. No fever reported."

    [Village C — Wed]
    "Cough and fever in maybe 8-12 people, started after the funeral last
    Saturday where many travelers came. One elderly woman died at home, her
    family says she was already weak."

    District lab case counts (last 14 days):
    | Date  | Village A     | Village B    | Village C       |
    | ----- | ------------- | ------------ | --------------- |
    | D-13  | 2 fever       | 0            | 1 fever         |
    | D-7   | 6 fever+rash  | 1 diarrhea   | 2 fever         |
    | D-3   | 14 fever+rash | 4 diarrhea   | 7 fever+cough   |
    | D-0   | 21 fever+rash | 5 diarrhea   | 11 fever+cough  |
    ```

### 2A — The bad prompt (one mega-prompt)

```text
I am a district epidemiologist. Read these three village reports and
the lab case-count table below. Write me a one-page outbreak brief for
my supervisor.

[paste the source data above]
```

!!! Failure "What goes wrong"
    A single mega-prompt typically:

    - **Hallucinates structure.** The model invents section headers ("Background", "Methodology") that don't apply to a one-page situation brief.
    - **Buries the broken-pump signal.** Village B's diarrhea cluster is real and waterborne, but the model often blends it into a generic "increased disease activity" paragraph.
    - **Misses the zoonotic clue.** The dead-and-eaten goat in Village A is a serious anthrax / hemorrhagic-fever differential. Mega-prompt outputs frequently drop this detail entirely or treat it as flavor text.

    The model is trying to do extraction + fusion + narration in one pass. Each is hard; together, they're a recipe for plausible-but-wrong prose.

### 2B — Better: split into a 3-step chain

Break the work the way an actual epidemiologist would: structure first, fuse second, narrate third. Open a fresh chat and run each step in sequence, **pasting the previous step's output into the next prompt**.

**Step 2B-i — Extract structured signals**

```text
Role: Field epidemiologist.
Action: For each of the three village reports below, extract a JSON object with:
  - village_name
  - presenting_syndromes (list)
  - estimated_case_count (or "unknown")
  - notable_environmental_factors (list)
  - zoonotic_or_animal_signals (string, "" if none)
  - reporter_confidence ("low" | "medium" | "high")

Output a JSON array.

[paste the three village reports]
```

**Step 2B-ii — Fuse with structured case counts**

```text
Role: District epidemiologist.
Action: Combine the structured signals (below) with the district lab case-count
table. Identify the two strongest outbreak signals and rank them by suspected
risk. Note any signal where the field report and the lab data disagree.

Format: Markdown with three H3 sections: "Top signals (ranked)", "Disagreements",
"Confidence notes".

[paste the JSON from step 2B-i]

[paste the case-count table]
```

**Step 2B-iii — Narrate as a one-page brief**

```text
Role: Senior epidemiologist writing for a non-specialist district medical
officer. Audience reads on a phone over breakfast.
Action: Convert the assessment below into a one-page brief.
Format: Exactly four sections, each 2-4 sentences:
  1. Situation
  2. Signal strength (with explicit uncertainty language)
  3. What we do not yet know
  4. Recommended next step (single concrete action)
Tone: Calm, declarative. No alarm words. No jargon a clinic nurse wouldn't recognize.

[paste the assessment from step 2B-ii]
```

!!! Success "What changed"
    Splitting the work makes each step diagnosable on its own. Step 2B-i preserves the goat-was-eaten signal as `zoonotic_or_animal_signals: "goat died and was consumed"`. Step 2B-ii ranks Village B's diarrhea cluster as the second priority because the broken pump plus river-water exposure is a clear waterborne pathway. The brief in 2B-iii now distinguishes what is known from what is not. The technique you applied is **prompt chaining** — see [prompts.md §4](../../prompts.md#4-prompt-chaining).

### 2C — Best: chain + chain-of-thought in the fusion step

The chain works, but the fusion step (2B-ii) still ranks signals based on whatever heuristics the model defaults to. You can make the reasoning visible — and improve it — by asking the model to think through each signal explicitly *before* ranking.

```text
[same as Step 2B-ii above, but replace "Identify the two strongest..."
with the block below]

Action: Combine the structured signals with the district lab case-count
table.

Before ranking, work through each signal one at a time. For each, write
ONE LINE answering each of these:
  - What does this signal tell us?
  - What's missing or uncertain?
  - Why does it escalate (or not)?
  - Is the lab data consistent with the field report?

After that line-by-line reasoning, identify the two strongest signals
and rank them by suspected outbreak risk.
```

!!! Success "What changed"
    Now the model explicitly notes that Village A's case-count growth (D-7=6 → D-0=21, ~3.5× in 7 days) plus child-skewed presentation ("mostly children under 10") plus rash is consistent with **measles** specifically — not just generic "fever+rash". It also surfaces that Village C's funeral-cluster signal could be respiratory and is plausibly underdetected (case counts only go to 11 but 8-12 were reported by the volunteer the same day). The technique you applied is **chain-of-thought** — making intermediate reasoning visible before the final answer. It's barely covered in `prompts.md` but is one of the highest-leverage techniques for any task involving ranking, scoring, or differential diagnosis.

### Reflection

In this exercise, **2B is the leverage step** — chaining unlocks the workflow. **2C is the safety step**: chain-of-thought turns a black-box ranking into something you can argue with, agree with, or override.

**Real-world echo.** [PandemicLLM](https://arxiv.org/abs/2404.06962){target=_blank}, Thailand's [PODD](https://endingpandemics.org/){target=_blank}, and Tanzania's AfyaData all do versions of "extract → fuse → narrate" — usually with retrieval grounding and human review at every step.

**Bias note.** Any outbreak-prioritization workflow that learns from past response patterns will reproduce past response inequities. See [Bias and Discrimination → Historical-spending bias](../../bias.md#concrete-examples-in-public-health).

---

## Exercise 3 — Chart Abstraction Stretch (~20 min)

**Anchor technique:** [The CRAFT framework](../../prompts.md#the-craft-framework).
**Gap-filling techniques:** Schema-constrained extraction + role-play + calibrated abstention.

**Scenario.** You're abstracting clinic notes for a quality-improvement review of pediatric respiratory care. The notes are messy — abbreviations, code-switching between English and Spanish, dates in three different formats.

??? Clipboard "Clinic notes (used in all three versions below)"

    ```text
    [P-001 — 5/3/26]
    "4yo F brought in by mama, cough x 4d, fiebre last night 39.2, retracciones
    mild, sat 96 RA. Looks tired pero alert. Sent home w/ amox 40mg/kg, return
    si empeora."

    [P-002 — May 3 2026]
    "infant 7mo, presented w/ apnea episodes per mom, 2 today. RR 70, sat 88
    in clinic. Sent to ED via ambulance immediately."

    [P-003 — 03/05/2026]
    "adolescent 14, asthma h/o, wheezing 2 days, peak flow 60% personal best,
    gave neb albuterol x 2 in clinic, pf -> 80%, d/c home w/ action plan
    review, follow up 1 wk."
    ```

### 3A — The bad prompt (prose instruction)

```text
Pull out the key info from these clinic notes for a QI review.

[paste the three clinic notes]
```

!!! Failure "What goes wrong"
    Without structure, the model returns:

    - **Inconsistent prose** per patient — sometimes a paragraph, sometimes bullets, sometimes a table. Useless for downstream analysis.
    - **Silent date-format resolution.** P-001's "5/3/26" and P-003's "03/05/2026" are *both ambiguous* between U.S. (M/D/Y) and ISO/European (D/M/Y) conventions. The model picks a convention and runs with it — usually U.S. for the first, ISO for the second, which means the two records are silently parsed under *different rules*. You will not catch this unless you go look.
    - **Mixed-language fields** ("fiebre", "retracciones", "si empeora") sometimes translated, sometimes dropped, sometimes left as-is.

### 3B — Better: schema-constrained extraction (CRAFT)

CRAFT forces you to spell out context, role, action, format, tone. Format is where you put a JSON schema.

```text
Context: I'm abstracting pediatric clinic notes for a QI review of
respiratory care.

Role: Clinical data abstractor.

Action: For each patient visit, extract one record into the schema below.

Format: A JSON array. Each element must conform to:
  {
    "patient_id": string,
    "visit_date": string (ISO 8601, YYYY-MM-DD),
    "presenting_symptom": string,
    "severity_1to5": integer,  // 1=mild, 5=critical
    "recommended_action": string
  }

Tone: Clinical and literal.

[paste the three clinic notes]
```

!!! Success "What changed"
    Output is now consistent across the three patients. P-002 lands at severity 5 with `recommended_action: "ED transfer"`. The technique you applied is **schema-constrained extraction** — under-covered in `prompts.md` but the workhorse of every production extraction pipeline.

    But: the model is **still silently resolving the date ambiguity**. P-001's `visit_date` and P-003's `visit_date` will be filled in confidently — and may be parsed inconsistently with each other. The schema constrains the *output shape*, not the *abstaining behavior*.

### 3C — Best: + role-play + calibrated abstention

Add two things: (1) a more specific role (an abstractor with experience flags rather than guesses), and (2) an explicit abstention convention so the model has somewhere to put "I don't know."

```text
Context: I'm abstracting pediatric clinic notes for a QI review of
respiratory care. The notes were dictated quickly and contain
abbreviations, mixed English/Spanish phrases, and inconsistent date formats.

Role: Clinical data abstractor with two years of pediatric chart-review
experience. You flag rather than guess. If a field is ambiguous, write
"UNCLEAR" and add the field name to needs_human_review.

Action: For each patient visit, extract one record into the schema below.

Format: A JSON array. Each element must conform to:
  {
    "patient_id": string,
    "visit_date": string (ISO 8601 if certain, else "UNCLEAR"),
    "presenting_symptom": string,
    "severity_1to5": integer or "UNCLEAR",
    "recommended_action": string,
    "needs_human_review": [string]  // field names that were unclear
  }

Tone: Clinical and literal. Do not infer beyond what is written.

After the JSON, write a 3-sentence reflection on which fields were
hardest to extract and why.

[paste the three clinic notes]
```

!!! Success "What changed"
    P-001 and P-003 now both flag `visit_date` as `UNCLEAR` and list it under `needs_human_review`. The model's reflection should explicitly call out the M/D/Y vs D/M/Y ambiguity. P-002 (which was unambiguous: "May 3 2026") still parses cleanly. The techniques you applied are **role-play** (the experienced-abstractor persona shifts the model's default toward caution) and **calibrated abstention** (giving the model a place to say "I don't know" prevents silent guessing).

!!! Tip "Aside: system prompts vs. chat prompts"
    If your platform supports system prompts separately from chat prompts (Claude, ChatGPT via Custom Instructions, the Gemini API), put the **Context, Role, and Tone** sections in the system prompt and only the **Action + Format + data** in the chat. Same content, but the system prompt persists across every message in the session — useful when you're abstracting hundreds of notes in one sitting. See [prompts.md §1](../../prompts.md#1-custom-instructions-and-system-prompts).

### Reflection

For chart abstraction, **3B unlocks structured downstream use** but **3C is what makes the system safe to deploy**. The lesson: a JSON schema by itself is not enough — you also need a sanctioned way for the model to refuse.

**Real-world echo.** [Penn Medicine's clinical-summarization pilots](https://www.pennmedicine.org/news/news-releases/2024){target=_blank} and [John Snow Labs FHIR-Ready AI](https://www.johnsnowlabs.com/){target=_blank} report 40–60% reductions in chart-abstraction time using this exact pattern (schema + explicit unclear-flagging). The unlock is the schema + abstention, not the model.

**Bias note.** Models trained predominantly on monolingual or single-region clinical text under-perform on code-switched notes. The `UNCLEAR` rate is your early-warning signal. See [Bias and Discrimination → Training-scope bias](../../bias.md#concrete-examples-in-public-health).

---

## Further Reading

- [WHO Guidance: Ethics and Governance of AI for Health](https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf){target=_blank}
- [ITU/WHO Focus Group on AI for Health (FG-AI4H)](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Pages/default.aspx){target=_blank}
- [Ending Pandemics Academy](https://endingpandemics.org/){target=_blank}
- [UA Public Health & AI Summer School](https://publichealth.arizona.edu/ai){target=_blank}
- [Hattab et al. (2025) The Way Forward to Embrace AI in Public Health. AJPH 115:123–128](https://doi.org/10.2105/AJPH.2024.307888){target=_blank}
- [Prompt Engineering Deep Dive](../../prompts.md) — the techniques applied here, in their own context

## Optional Homework

Each link below extends one of the exercises above with a deeper agentic workflow.

- [Vibe Coding](../../vibe.md) — wire Exercise 2's chain into an agent that reads village reports from disk and writes the brief to a markdown file.
- [MCP](../../mcp.md) — connect a chat LLM to a real syndromic-surveillance database via the Model Context Protocol.
- [RAG](../../rag.md) — extend Exercise 3 with retrieval over your local clinical guidelines so the LLM cites a specific protocol when it recommends an action.
- [GIS Mapping Lab](./gis.md) — apply the same prompt-engineering skills to building a story map of an outbreak.
