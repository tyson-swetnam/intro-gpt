# Public Health AI Lab — Triage, Surveillance, Abstraction

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! Example "What you'll build (60–90 min)"
    Three artifacts that mirror real public-health workflows:

    1. A **classification table** for inbound SMS health messages
    2. A **one-page outbreak briefing** synthesized from village reports + case counts
    3. A **structured JSON record set** abstracted from messy clinic notes

    Each exercise applies one technique from the [Prompt Engineering Deep Dive](../../prompts.md) — you are *applying* prompt engineering to public-health work, not learning it from scratch.

## Prerequisites

| ✔︎ | Requirement | Notes |
|---|-------------|-------|
|   | Read [Prompt Engineering](../../prompts.md) first | CRAFT framework, few-shot, prompt chaining |
|   | Access to a chat-style LLM | Claude, ChatGPT, or Gemini in any browser |
|   | 60–90 min | All exercises run in a single chat session |

---

## Why this lesson exists

Public-health workers spend hours every week on low-to-moderate technical computer tasks: sorting inbound messages, triaging phone reports, reconciling line lists, abstracting charts. Off-the-shelf chat LLMs can give those hours back **without** new infrastructure, **without** new vendor contracts, and **without** moving sensitive data — provided the prompts are written carefully and a human stays in the loop on every consequential decision.

This lab is built around three workflows the [Ending Pandemics Academy](https://endingpandemics.org/){target=_blank} and CDC syndromic surveillance teams already deploy in the field. The prompts and synthetic data here are simplified for a 90-minute classroom session, but the shape of the work is the real shape of the work.

## Real-world anchors

The exercises map onto deployed and emerging systems:

- **Cambodia 115 Hotline + Thailand PODD + Tanzania AfyaData.** Community-driven event-based surveillance run through SMS, voice calls, and mobile apps. The Ending Pandemics Academy at the University of Arizona Zuckerman College trains practitioners to combine these signals with prompt-engineered LLMs and retrieval workflows.
- **CDC National Syndromic Surveillance Program (NSSP) and PandemicLLM.** [PandemicLLM](https://arxiv.org/abs/2404.06962){target=_blank} demonstrates that an LLM, given structured case counts and free-text situation reports, can produce forecast-grade short-range outbreak guidance — the same fusion task you do by hand in Exercise 2.
- **Penn Medicine clinical summarization and John Snow Labs FHIR-Ready AI.** Multiple pilot studies report 40–60% reductions in time spent on chart abstraction when the model is prompted with a tight schema and a small set of validated examples — the pattern in Exercise 3.

---

## Exercise 1 — SMS Symptom Triage (~30 min)

**Applies:** [Few-Shot Learning](../../prompts.md#5-using-examples-few-shot-learning) and the [CRAFT framework](../../prompts.md#the-craft-framework).

**Scenario.** You are running a community SMS line for a rural district health office. Eight messages arrived overnight. You need to sort them into four buckets — **urgent**, **route-to-clinic**, **misinformation**, **not-actionable** — and you need to do it before the 8 a.m. clinic huddle.

### The prompt

Paste the block below into your chat LLM. The block uses the CRAFT structure (context, role, action, format, tone) and includes three labeled examples to anchor the classifier.

```text
Context: I run an SMS health line for a rural district. I receive 50–200 inbound
messages per night and need to triage them before the morning clinic huddle.

Role: Act as a public-health triage nurse with three years of community SMS
experience. You are cautious — when unsure, you escalate.

Action: Classify each inbound SMS into exactly one of these buckets:
  - URGENT: symptoms that may need same-day medical attention
  - ROUTE-TO-CLINIC: non-urgent but should see a clinician within a week
  - MISINFORMATION: contains a factual claim that, if acted on, could cause harm
  - NOT-ACTIONABLE: greeting, test, irrelevant, or unintelligible

Format: A markdown table with columns | # | Message | Classification | One-line rationale |.
After the table, list any messages where you were less than 80% confident.

Tone: Concise, clinical, no hedging language inside the table cells.

Examples:
  "my baby has been vomiting for two days and won't drink water"
    -> URGENT (dehydration risk in infant)
  "is it true the new vaccine has a microchip"
    -> MISINFORMATION (factually false claim circulating in community)
  "good morning sister"
    -> NOT-ACTIONABLE (greeting only)

Now classify these 8 messages:
  1. fever 3 days, headache, neck stiff, light hurts my eyes
  2. can my child take amoxicillin if she is allergic to penicillin
  3. drinking bleach cures malaria right
  4. test
  5. cough 2 weeks getting worse, blood in sputum, lost weight
  6. when does the family planning clinic open
  7. my husband fell and cannot move his left side, started 30 minutes ago
  8. is paracetamol safe in pregnancy
```

### Success criterion

A single markdown table with all 8 rows classified plus a short list of low-confidence messages. Messages 1, 5, and 7 should land in **URGENT** (meningitis-suspect, TB-suspect, stroke-suspect). Message 3 should land in **MISINFORMATION**. If your model puts message 7 anywhere other than URGENT, the prompt is failing — escalate or rerun.

### Bias audit (5 min)

Rerun the same prompt with messages 1, 5, and 7 rewritten in code-switched English/Spanish, e.g. *"siete en los ojos light hurts mucho headache desde tres días"*. Compare classifications. Did the urgency rating drop? This is a known failure mode of LLM triage — see [Bias and Data Quality](../../bias.md) — and is the reason these systems are deployed as a *first pass* under human review, never as a final routing decision.

### Real-world echo

Cambodia 115, mHero, Yale's viral-triage prototype, and the Penn COVID Chatbot all run variations of this workflow at production scale. None of them route any message to "ignore" without a human spot-check.

---

## Exercise 2 — Outbreak Signal Synthesis (~30 min)

**Applies:** [Prompt Chaining](../../prompts.md#4-prompt-chaining) and [Working with Documents](../../prompts.md#working-with-documents).

**Scenario.** You are the duty epidemiologist. You have three free-text reports filed by community health volunteers in three villages this week, plus a small structured case-count table from the district lab. You need a one-page early-warning brief on the supervisor's desk by lunch.

This exercise uses a **three-step chain** instead of one mega-prompt. After each step, paste the model's output into the next prompt as the input. This mirrors how PODD and AfyaData operators actually triangulate signals.

### Step 2A — Extract structured signals from the field reports

```text
Role: Field epidemiologist.
Action: Read the three village reports below. For each report, extract:
  - village_name
  - date_reported
  - presenting_syndromes (list)
  - estimated_case_count (or "unknown")
  - notable_environmental_factors
  - reporter_confidence (low/medium/high, your judgment)
Format: A JSON array, one object per village.

Reports:

[Village A — Tue]
"This week we have seen many people with fever and rash, mostly children
under 10. The school sent home about 20 kids. A goat in the same compound
also died but the family ate it. Rains are heavy and the well is muddy."

[Village B — Wed]
"Three adults with severe diarrhea since Sunday, two were hospitalized.
The shared pump near the market broke last week and people are drawing
from the river. No fever reported."

[Village C — Wed]
"Cough and fever in maybe 8–12 people, started after the funeral last
Saturday where many travelers came. One elderly woman died at home, her
family says she was already weak."
```

### Step 2B — Fuse the signals with the structured case-count table

Paste the JSON output from Step 2A into the prompt below, followed by the table.

```text
Role: District epidemiologist preparing a situation assessment.
Action: Combine the structured signals (above) with this district lab
case-count table from the past 14 days. Identify the two strongest signals
and rank them by suspected outbreak risk. Note any signal where the field
report and the lab data disagree.

| Date  | Village A | Village B | Village C |
| ----- | --------- | --------- | --------- |
| D-13  | 2 fever   | 0         | 1 fever   |
| D-7   | 6 fever+rash | 1 diarrhea | 2 fever |
| D-3   | 14 fever+rash | 4 diarrhea | 7 fever+cough |
| D-0   | 21 fever+rash | 5 diarrhea | 11 fever+cough |

Format: Markdown with H3 headings: "Top signals", "Disagreements",
"Confidence notes".
```

### Step 2C — Produce the one-page early-warning brief

```text
Role: Senior epidemiologist writing for a non-specialist district medical
officer. Audience reads on a phone over breakfast.
Action: Convert the assessment above into a one-page brief.
Format: Exactly four sections, each 2–4 sentences:
  1. Situation
  2. Signal strength (with explicit uncertainty language)
  3. What we do not yet know
  4. Recommended next step (single concrete action)
Tone: Calm, declarative. No alarm words. No jargon a clinic nurse
wouldn't recognize.
```

### Success criterion

A one-page markdown brief that flags **Village A's escalating fever+rash cluster** as the highest-priority signal (suspect measles, given child-skewed presentation and rapid case growth), **Village B's diarrhea cluster** as the second priority (suspect waterborne, given the broken pump), and explicitly says what is *not* yet known (case definition, lab confirmation, geographic spread).

### Real-world echo

PODD (Thailand), AfyaData (Tanzania), PandemicLLM, and CDC NSSP all do versions of "extract → fuse → narrate" — usually with retrieval grounding and human review at every step. The chain pattern matters: if you skip Step 2A and paste raw reports into Step 2C, the LLM will hallucinate structure, miss the goat-dies-and-was-eaten zoonotic signal in Village A, and bury the broken pump in Village B.

---

## Exercise 3 — Chart Abstraction Stretch (~20 min)

**Applies:** [CRAFT framework](../../prompts.md#the-craft-framework) and [Working with Documents](../../prompts.md#working-with-documents).

**Scenario.** You are abstracting clinic notes for a quality-improvement review. The notes are messy — abbreviations, code-switching, dates in three formats. You need clean structured records.

### The prompt

```text
Context: I am abstracting clinic visit notes for a QI review of pediatric
respiratory care. The notes were dictated in haste and contain abbreviations,
mixed-language phrases, and inconsistent date formats.

Role: Clinical data abstractor with two years of pediatric chart-review
experience. You flag rather than guess when a field is unclear.

Action: Extract one record per patient visit into the schema below. If a
field cannot be determined from the note, write "UNCLEAR" and add a
flag in the "needs_human_review" array.

Schema:
  - patient_id (string)
  - visit_date (ISO 8601, YYYY-MM-DD)
  - presenting_symptom (single short phrase)
  - severity_1to5 (integer, 1=mild, 5=critical)
  - recommended_action (single short phrase)
  - needs_human_review (array of field names that were unclear)

Format: A JSON array. After the JSON, write a 3-sentence reflection on
which fields were hardest to extract and why.

Tone: Clinical and literal. Do not infer beyond what is written.

Notes:

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

### Success criterion

A JSON array with three objects. P-002 should land at severity 5 with `recommended_action` = ED transfer. The reflection should call out the **dual date format issue** (5/3/26 vs 03/05/2026 are ambiguous between U.S. and ISO interpretations) as a needs-human-review flag — if the model silently picks one convention without flagging it, the prompt is failing.

### Reflection (5 min)

Where would you place a human checkpoint? At minimum: anywhere `needs_human_review` is non-empty, anywhere severity ≥ 4, and any record where the date format is ambiguous. Write down where *you* would add a second checkpoint a junior abstractor might miss.

### Real-world echo

The Penn Medicine clinical-summarization pilots and John Snow Labs' FHIR-Ready AI use this exact pattern — schema-constrained extraction with explicit unclear-flagging — and report 40–60% reductions in chart-abstraction time. The unlock is the schema, not the model.

---

## Responsible Implementation Checkpoints

Each exercise above has a known failure mode that has caused real-world harm. Use these as audit lenses when adapting these prompts to your own work.

!!! Warning "Pulse-oximeter bias (Exercise 1, 3)"
    AI-enabled pulse oximeters [overstate blood-oxygen saturation in patients with darker skin](https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism){target=_blank}. Any triage system that relies on a sat reading — including any LLM that scores severity from a chart — inherits that bias. If your prompt uses sat as a severity input, document the limitation and require a human spot-check on borderline readings.

!!! Warning "Historical-spending bias (Exercise 2)"
    A widely deployed U.S. care-allocation algorithm [systematically routed less care to Black patients than to White patients](https://www.science.org/doi/10.1126/science.aax2342){target=_blank} because it was trained on historical health-care *spending* as a proxy for need. Any outbreak-prioritization prompt that learns from past response patterns will reproduce past response inequities. Audit the inputs your chain uses, not just the outputs.

!!! Warning "Training-data scope bias (Exercise 3)"
    AI dermatology and retinopathy models trained predominantly on lighter-skinned cohorts perform measurably worse on darker skin. The same logic applies to any chart-abstraction model trained on a single language, region, or specialty — if your clinic notes regularly code-switch or use local abbreviations the model has not seen, the "UNCLEAR" rate is your early warning. See [Bias and Data Quality](../../bias.md) and [Ethics: Transparency & Accountability](../../transparency.md).

---

## Real-world systems referenced

A reference table of deployed and emerging public-health AI systems. Each maps to one or more of the workflows above.

| Application area | Technique | Example system | Data sources |
| --- | --- | --- | --- |
| Early outbreak detection | ML, NLP | [BlueDot](https://bluedot.global/){target=_blank}, [HealthMap](https://www.healthmap.org/en/){target=_blank} | News, social, airline, official reports |
| Real-time monitoring | NLP | [CDC NLP for vaccine safety](https://www.cdc.gov/csels/dmi/projects/ai-ml.html){target=_blank} | EHRs, lab reports, free-text PH data |
| Epidemic forecasting | ML, deep learning | [CDC FluSight](https://www.cdc.gov/flu-forecasting/data-vis/current-week.html){target=_blank} | Historical case data, climate, mobility |
| High-risk population ID | ML | [TowerScout](https://www.ischool.berkeley.edu/projects/2020/towerscout){target=_blank} | Demographic, aerial imagery |
| Pathogen genomic surveillance | ML | [Nextstrain](https://nextstrain.org/){target=_blank} | Pathogen genomic sequences |
| Syndromic surveillance | NLP, image analysis | [CAD4TB](https://delft.care/cad4tb/){target=_blank} | Search queries, social, chest X-rays |
| AMR tracking | Predictive analytics | [AI-driven AMR surveillance](https://www.mdpi.com/2079-6382/12/5/861){target=_blank} | Clinical, epi, lab data |
| Vector-borne disease prediction | ML | [Malaria climate models](https://gcgh.grandchallenges.org/grant/ai-based-malaria-incidence-prediction-under-current-and-future-climate-southern-ethiopia-aim){target=_blank} | Environmental, satellite, case data |
| Resource allocation | ML | [NHS A&E demand forecasting](https://www.england.nhs.uk/2023/08/ai-tool-improving-outcomes-for-patients-by-forecasting-ae-admissions/){target=_blank} | Outbreak, hospital, supply-chain |
| Misinformation monitoring | NLP | [EPIWATCH](https://kirby.unsw.edu.au/news/new-grant-help-detect-and-counter-public-health-fake-news){target=_blank} | Social media, online news |
| Clinical decision support | LLM, vision | [LumineticsCore](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/){target=_blank}, [TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/){target=_blank}, [AMIE](https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/){target=_blank} | Retinal images, molecular data, conversation |

The full FDA list of approved AI medical devices is at [datawrapper.de/_/IBGhg](https://www.datawrapper.de/_/IBGhg/){target=_blank}.

---

## Further Reading

- [WHO Guidance: Ethics and Governance of AI for Health](https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf){target=_blank}
- [ITU/WHO Focus Group on AI for Health (FG-AI4H)](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Pages/default.aspx){target=_blank}
- [Ending Pandemics Academy](https://endingpandemics.org/){target=_blank}
- [UA Public Health & AI Summer School](https://publichealth.arizona.edu/ai){target=_blank}
- [Hattab et al. (2025) The Way Forward to Embrace AI in Public Health. AJPH 115:123–128](https://doi.org/10.2105/AJPH.2024.307888){target=_blank}
- [Zeng et al. (2021) AI-enabled public health surveillance — from local detection to global epidemic monitoring](https://doi.org/10.1016/B978-0-12-821259-2.00022-3){target=_blank}

## Optional Homework

Each link below extends one of the exercises above with a deeper agentic workflow.

- [Vibe Coding](../../vibe.md) — wire Exercise 2's chain into an agent that reads village reports from disk and writes the brief to a markdown file.
- [MCP](../../mcp.md) — connect a chat LLM to a real syndromic-surveillance database via the Model Context Protocol.
- [RAG](../../rag.md) — extend Exercise 3 with retrieval over your local clinical guidelines so the LLM cites a specific protocol when it recommends an action.
- [GIS Mapping Lab](./gis.md) — apply the same prompt-engineering skills to building a story map of an outbreak.
