# Generative AI for Life Sciences Research — KEYS Internship

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

A one-hour module for [BIO5 KEYS Research Internship](https://keys.arizona.edu/){target=_blank} students. Forty minutes of lecture on what generative AI is actually doing in life-sciences labs in 2026, followed by twenty minutes of hands-on practice on the University of Arizona's [genai.arizona.edu](https://genai.arizona.edu/){target=_blank} platform.

!!! Example "What you'll walk out with (60 min)"

    - A working mental model of what an LLM is doing when it answers you, and where that breaks
    - A short list of tasks AI is genuinely useful for in a bench-science or computational-biology lab
    - A clear sense of the failure modes — hallucinated citations, fabricated protocols, leaked data — and how to avoid them
    - First-hand experience comparing models on a real research question, and verifying (or busting) AI-generated citations against primary sources
    - A reusable prompt for one task you'll actually do this week in your KEYS lab

## Who this is for

KEYS interns working in BIO5-affiliated labs across bioscience, biomedical engineering, biotechnology, statistics, and computational biology. No coding background required. Some background in high-school biology helps; the specific examples will translate to whatever your lab does.

## Schedule

| Block | Duration | Activity |
|-------|----------|----------|
| 1 | 5 min  | Why this lesson exists |
| 2 | 10 min | What generative AI actually is |
| 3 | 15 min | What it's useful for in your lab |
| 4 | 10 min | What it's risky for — and the policies that protect you |
| 5 | 20 min | Hands-on at [genai.arizona.edu](https://genai.arizona.edu/){target=_blank} |

---

## Part 1 — Why this lesson exists (5 min)

Generative AI did not replace researchers in 2024-2026. It did change the daily workflow of almost every working scientist. AlphaFold won the 2024 Nobel Prize in Chemistry for predicting protein structures from sequence — work that previously took years of crystallography per structure. Hundreds of biotech and pharma teams now use large language models to draft code, summarize literature, and pre-screen candidate molecules. Your KEYS mentor almost certainly uses AI tools in their week, even if they don't talk about it much.

The goal of this hour is not to make you an expert. It's to give you enough of a working mental model that, in the moment, you can decide:

- *Is this a task where reaching for an AI assistant will save me real time?*
- *Is this a task where reaching for an AI assistant will quietly produce a wrong answer I won't catch?*
- *Is this a task where pasting this data into an AI tool would violate my lab's policies, my mentor's trust, or federal law?*

By the end of the hour you should have rough answers to all three for the kinds of tasks KEYS interns actually do.

---

## Part 2 — What generative AI actually is (10 min)

**A Large Language Model (LLM) is a pattern-recognition system trained on enormous amounts of text.** Given everything you've typed so far in a conversation, it predicts the most likely next word, then the next, then the next. Modern frontier models — Claude, GPT, Gemini, Llama, Gemma — are extraordinarily good at this, to the point that the outputs feel like thought. They are not databases. They do not "look things up." They generate plausible continuations.

Three consequences of this design that matter in a research setting:

1. **Hallucination is a feature of how the model works, not a bug.** When the model doesn't know something, it produces plausible-sounding text anyway, because plausibility is what it was trained to optimize. You will get confident-sounding citations to papers that do not exist, protocol steps with invented temperatures, and statistics with invented p-values.

2. **Knowledge cutoffs are real.** Each model has a date after which it knows nothing. Ask a model about a paper published last month and it may invent one rather than admit ignorance. Some models can "search the web" to compensate; many cannot.

3. **The same prompt can give different answers in different runs.** LLMs sample probabilistically. Run the same question twice, you may get different (but both confidently stated) answers. This is a useful test you'll do in Exercise 1.

For the deeper background — what a transformer is, how training works, the difference between foundation models and fine-tuned models — see the [AI landscape](../ai_landscape.md) lesson. For now, that mental model (next-word predictor trained on text) is enough.

---

## Part 3 — What it's useful for in your KEYS lab (15 min)

Here is where AI genuinely earns its keep in a life-sciences lab, organized by the kind of work you'll actually do this summer.

### Literature work

- **Summarizing a paper** you don't have time to read in full. Always read the abstract and figures yourself; let the AI summary scaffold the rest.
- **Comparing two papers' findings** side by side. Useful when your mentor sends you three papers and asks "what do these have in common?"
- **Finding vocabulary you're missing.** "What does *ChIP-seq* stand for and what is it actually measuring?" is a perfect AI question.
- **Drafting a literature review outline** that you then fill in with actual reading.

### Writing

- **Tightening a paragraph** without changing scientific content. Ask: *"Improve the clarity of this paragraph; do not change any factual claims."*
- **Translating between informal lab notes and formal scientific writing.** Your scribbled bench notes become a methods-section draft.
- **Catching grammar and structural problems** before your mentor reads your draft.
- **Outlining your final KEYS presentation** in a structure that walks an audience from question → methods → results → significance.

### Code and data analysis

- **Generating starter code** for plots, statistical tests, or data cleaning in Python or R.
- **Debugging error messages** by pasting the full traceback and asking what's going wrong.
- **Explaining unfamiliar code** your mentor wrote ("walk me through this script line by line").
- **Converting between data formats** (CSV → JSON, FASTA → table, etc.).

For more on AI-assisted coding, see the [Vibe Coding](../vibe.md) lesson — but a chat interface like genai.arizona.edu is the right starting point.

### Thinking

- **Brainstorming experimental design alternatives.** AI is good at "what are five other ways someone might test this?"
- **Walking through a difficult concept** until you understand it. Ask it to explain at the level of a high-school junior, then at the level of a first-year grad student.
- **Generating hypotheses to test.** Then *you* test them, in lab — the AI does not.
- **Steel-manning objections** you might face in your KEYS final presentation. "What's the strongest critique of my approach?"

### Real life-sciences examples to know about

- **[AlphaFold](https://deepmind.google/technologies/alphafold/){target=_blank}** (DeepMind) — protein structure prediction from sequence. 2024 Chemistry Nobel.
- **[ESM and ESMFold](https://github.com/facebookresearch/esm){target=_blank}** (Meta) — protein language models; predict structure and function directly from amino-acid sequences.
- **Drug discovery at scale** — companies like [Recursion](https://www.recursion.com/){target=_blank}, [Isomorphic Labs](https://www.isomorphiclabs.com/){target=_blank}, and [Insilico Medicine](https://insilico.com/){target=_blank} use AI to generate and screen candidate molecules.
- **FDA-approved AI medical devices** — there are now [hundreds of cleared AI/ML devices](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-enabled-medical-devices){target=_blank}, mostly in medical imaging.
- **Foundation models for genomics** — newer systems like Evo and Borzoi that learn directly from DNA sequences at scale.

The unifying pattern: **AI assists hypothesis generation and pattern recognition; experiments validate.** A model that predicts a protein structure or proposes a candidate molecule still needs wet-lab or clinical confirmation before anyone trusts it. Your KEYS project is the experiment side of that loop.

---

## Part 4 — What it's risky for (10 min)

### The hallucination problem

This is the failure mode you most need to internalize.

- Models invent **citations** — specific paper titles, authors, journals, and DOIs that look real and are not.
- Models invent **protocol details** — specific concentrations, incubation times, temperatures, buffer recipes.
- Models invent **statistics** — test results, p-values, sample sizes pulled from thin air.

The rule: **AI-generated facts are not facts until you have verified them against a primary source.** You will do this in Exercise 2.

### The data privacy problem

When you paste data into a commercial chatbot (ChatGPT.com, Claude.ai, etc.), you may be sending it to a third party that does not have a data-sharing agreement with your lab or the University of Arizona.

- **Do not paste unpublished research data** into commercial chatbots.
- **Do not paste patient-identifying information** anywhere. Ever. HIPAA exists.
- **Do not paste proprietary protocols** your lab considers confidential or that came from a sponsor's intellectual property.
- When you need to work with sensitive material, **use the U of A platform at [genai.arizona.edu](https://genai.arizona.edu/){target=_blank}** — it's FERPA-aligned and your conversations are not used to train models.

If you are working with human-subjects data, your project has IRB protections that come with rules about what you can and cannot share. **Ask your mentor first.**

### The disclosure problem

- Many journals and many fellowship applications now **require disclosure** of AI tool use. Your final KEYS deliverable may have its own rules — ask your mentor before you start using AI heavily.
- Research has found that [disclosing AI use makes people trust you less](https://theconversation.com/being-honest-about-using-ai-at-work-makes-people-trust-you-less-research-finds-253590){target=_blank} — but be honest anyway. Reputational risk from undisclosed AI use is much worse than the trust hit from disclosing.

### The replacement temptation

AI is not your mentor. It is not the experimental method. It is not your scientific judgment. Treat an AI assistant as a *junior collaborator* — one who is fast, occasionally wrong, and has no stake in the outcome. You still own the conclusions. Your name goes on the poster.

For more on responsible AI use in research, see the [Ethics of AI](../ethics.md) and [Bias & Discrimination](../bias.md) lessons.

---

## Part 5 — Hands-on at genai.arizona.edu (20 min)

Open [genai.arizona.edu](https://genai.arizona.edu/){target=_blank} in a browser and log in with your UA NetID. The platform is an [OpenWebUI](https://openwebui.com/){target=_blank} interface that gives you free access to multiple frontier models — Claude, OpenAI, Gemma, Meta Llama, and Amazon Nova — through a single chat window. Conversations are private and are not used to train models. ([Platform details from the U of A Responsible AI office.](https://responsibleai.arizona.edu/u-of-a-gen-ai){target=_blank})

Work through the four exercises in order. Each takes about five minutes.

### Exercise 1 — Compare two models on a research question (5 min)

Pick a topic from your KEYS lab. Ask one of the available models:

```
I'm a high school student starting a research project in <your lab's area —
e.g. CRISPR base editing, cancer-cell migration, microbiome data analysis>.
Explain in plain language:
1. What is the main experimental approach in this field?
2. What are the most common pitfalls a new student makes?
3. What should I ask my mentor about before I touch anything in the lab?
```

Then switch to a **different model** (the model selector is at the top of the chat) and ask the exact same prompt.

!!! Question "Reflection"

    - Did the two models agree?
    - Did either model say something specific you couldn't immediately verify?
    - Which response would you actually use to prepare for your first day in lab — and why?

### Exercise 2 — Test for hallucination (5 min)

Ask the model for three specific citations supporting a claim from your field:

```
List three peer-reviewed papers from the last five years that show
<a specific claim relevant to your KEYS project — e.g. "off-target
effects of CRISPR-Cas9 are reduced by high-fidelity variants" or
"single-cell RNA-seq reveals tumor heterogeneity in pancreatic cancer">.
For each: authors, year, journal, DOI.
```

Now check each DOI by pasting it into [doi.org](https://doi.org/){target=_blank}. Some will resolve to the paper described. Some will redirect to a different paper. **Some will not exist at all.**

!!! Question "Reflection"

    - How many of the three were real?
    - Could you tell which were fake just from how the citation looked?
    - If you'd used this in a poster without checking, what would have happened?

This is the single most important habit to build. *AI-generated citations are not citations until you have confirmed them in a primary source.*

### Exercise 3 — Protocol explainer (5 min)

Find a protocol from your KEYS lab — your mentor probably has a written one for whatever you're learning this week. Paste a short excerpt (a paragraph or two; do **not** paste anything your mentor flagged as confidential) and ask:

```
I'm a high school intern who has never run this protocol before. Walk me
through it step by step, flagging:
- Any safety concerns I should ask my PI about
- Steps that look like they could fail silently (i.e. give a wrong answer
  without an obvious error)
- Reagents or instruments where a mistake would be expensive
```

!!! Question "Reflection"

    - Did the AI's explanation match what your mentor told you?
    - Where did it differ — and which version do you trust?
    - Was there anything the AI flagged as risky that your mentor *hadn't* mentioned? Worth bringing back to your mentor.

### Exercise 4 — Write your own structured prompt (5 min)

Use the **CRAFT framework** from the [Prompt Engineering lesson](../prompts.md#the-craft-framework) — **C**ontext, **R**ole, **A**ction, **F**ormat, **T**one — to write a prompt for one real task you'll do this week in your KEYS lab.

A skeleton:

```
[CONTEXT] I am a KEYS intern in <lab name / area>. My project involves
<one-sentence description>. I am working on <specific task this week>.

[ROLE] Act as <senior grad student / staff scientist / quantitative biologist>
who has done this kind of work and is patient with explaining the basics.

[ACTION] <Specific task: "draft an outline," "explain this concept,"
"suggest three plot types for this dataset," etc.>

[FORMAT] <How you want the answer: numbered list, table, paragraph, etc.>

[TONE] Clear and direct. Flag anything you are uncertain about rather than
inventing details.
```

Run it. Then iterate — adjust one piece of the CRAFT structure and re-run. Notice how much output quality changes from small prompt changes.

!!! Question "Reflection"

    Save the prompt that worked best. You'll use variations of it all summer.

---

## After class

When you have time during the rest of your KEYS internship, the workshop has deeper lessons on each of the topics we touched today:

- [Prompt Engineering Deep Dive](../prompts.md) — CRAFT, few-shot learning, chain-of-thought, prompt chaining
- [Daily Productivity](../daily-productivity.md) — AI for emails, summaries, scheduling, data analysis without writing code
- [AI in Research](../research.md) — deep research workflows, literature synthesis, hypothesis generation
- [Ethics of AI](../ethics.md) — including Alondra Nelson's "civic grammar" framework and Pope Leo XIV's *Magnifica Humanitas* encyclical on AI
- [Bias & Discrimination](../bias.md) — algorithmic bias, especially in medical and biological AI
- [Vibe Coding](../vibe.md) — AI-assisted coding for data analysis and computational projects
- [Choosing a Platform](../choose.md) — current pricing and capability comparison across models

For hands-on labs that go deeper:

- [Public Health AI Lab](publichealth/casestudy.md) — SMS triage, outbreak surveillance, chart abstraction
- [Vibe Coding a Public Health Map](publichealth/gis.md) — full agentic workflow building an interactive data visualization

## Further reading for highly motivated KEYS interns

- Jumper, J. et al. (2021). *Highly accurate protein structure prediction with AlphaFold.* Nature. [doi.org/10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2){target=_blank}
- Lin, Z. et al. (2023). *Evolutionary-scale prediction of atomic-level protein structure with a language model.* Science. [doi.org/10.1126/science.ade2574](https://doi.org/10.1126/science.ade2574){target=_blank}
- Bommasani, R. et al. (2022). *On the Opportunities and Risks of Foundation Models.* arXiv. [doi.org/10.48550/arXiv.2108.07258](https://doi.org/10.48550/arXiv.2108.07258){target=_blank}
- Bender, E. M. et al. (2021). *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?* FAccT. [doi.org/10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922){target=_blank}
- University of Arizona [Responsible AI](https://responsibleai.arizona.edu/){target=_blank} — campus policies, tools, and training
- University of Arizona [Generative AI LibGuide](https://libguides.library.arizona.edu/genAI){target=_blank} — research-focused guides from the UA Libraries

## Acknowledgments

This lesson was developed for the [BIO5 KEYS Research Internship Program](https://keys.arizona.edu/){target=_blank}. Thanks to the KEYS program staff, the BIO5 mentors who host interns each summer, and the U of A Responsible AI team for making [genai.arizona.edu](https://genai.arizona.edu/){target=_blank} freely available to the UA community.
