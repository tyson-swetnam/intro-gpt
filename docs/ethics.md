---
type: Ethics Guide
title: Ethics of Artificial Intelligence
description: >-
  Traces AI ethics from the 1956 Dartmouth workshop to the 2026 essays of
  Bregman and Gates on AI denial, governance, and the economic transition.
resource: https://tyson-swetnam.github.io/intro-gpt/ethics/
tags: [ethics]
sources:
  - resource: https://rutgerbregman.substack.com/p/an-inconvenient-truth-about-ai
    title: An Inconvenient Truth About AI
    author: Rutger Bregman
  - resource: https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make
    title: The turbulent AI era is here
    author: Bill Gates
  - resource: https://spectrum.ieee.org/dartmouth-ai-workshop
    title: IEEE Spectrum on the 1956 Dartmouth AI workshop
  - resource: https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth
    title: Artificial Intelligence coined at Dartmouth
  - resource: https://techcrunch.com/2026/08/26/bill-gates-wants-to-see-a-robot-tax-and-human-reserved-jobs-to-mitigate-harms-from-ai/
    title: TechCrunch interview with Bill Gates on robot taxes
generated:
  by: human:tswetnam
  at: "2026-08-30T15:21:35-06:00"
verified:
  - by: human:tswetnam
    at: "2026-08-30T15:21:35-06:00"
status: stable
---

# Ethics of Artificial Intelligence

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## History

In 1956 a small group of scientists gathered at [Dartmouth](https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth){target=_blank} for a [Summer Research Project on Artificial Intelligence](https://spectrum.ieee.org/dartmouth-ai-workshop){target=_blank}. 

A new field of Science had begun. 

<figure>
<a href="https://spectrum.ieee.org/dartmouth-ai-workshop" target="_blank" rel="noopener noreferrer">
    <img src="https://spectrum.ieee.org/media-library/close-up-of-a-black-and-white-photo-of-seven-smiling-men-sitting-on-a-lawn.jpg?id=33603729&width=1800&quality=85" alt="Dartmouth AI Workshop, 1956" width="700">
</a>
<figcaption><a href="https://spectrum.ieee.org/dartmouth-ai-workshop" target="_blank" rel="noopener noreferrer">Dartmouth Summer Research Project on Artificial Intelligence, 1956. Credit: IEEE Spectrum, The Minsky Family</a></figcaption>
</figure>

Over the next 70 years, Artificial Intelligence persisted mainly in [the minds of science fiction writers](legal.md) and the small group of industry researchers and academics who continued to work toward creating the digital infrastructure needed for Artificial Intelligence to bloom, and to one day achieve the ultimate goal of [Artificial General Intelligence (AGI)(:simple-wikipedia:)](https://en.wikipedia.org/wiki/Artificial_general_intelligence){target=_blank}. 

## Using AI ethically

As consumers of GPTs and other AI platforms, we must consider in what ways can we use AI both effectively, and ethically.

!!! Success "By the end of this module you will be able to..."

    1. Distinguish ethical **principles**, legal **instruments**, and accountability **mechanisms** for AI.
    2. Explain the difference between voluntary and binding AI governance, with a 2026 example of each.
    3. Describe **reward hacking** and why evaluation containment matters, using the [OpenAI and Hugging Face incident](legal.md#case-study-the-openai-and-hugging-face-incident-july-2026).
    4. Explain why logs alone do not establish accountability, and what [independent investigation](transparency.md) adds.
    5. Compare Bregman's and Gates's 2026 prescriptions for the AI transition.

## Is AI denial the new climate denial?

!!! Quote ":material-bullhorn: Rutger Bregman — 'An Inconvenient Truth About AI' (2026)"

    Historian **Rutger Bregman** argues that the political polarity of denial has flipped. In [a widely shared essay (and video essay)](https://rutgerbregman.substack.com/p/an-inconvenient-truth-about-ai){target=_blank}, he writes:

    > Twenty years ago, climate denial was a problem of the right. Today, AI denial is a problem of the left. And the consequences could be even more disastrous.

    His case, condensed:

    - **The skeptics keep moving the goalposts.** The "stochastic parrot / blurry JPEG / lumbering pattern-matcher" framing (Chomsky, Bender &amp; Gebru, and others) predicted the technology would stall. Instead the same systems have passed medical-licensing exams and out-diagnosed doctors, won gold at the International Mathematical Olympiad, out-scored PhDs in their own fields, and now write **more than 90% of the code** inside leading AI labs. Judging today's models from a frustrating attempt back in 2023, he writes, is "like judging smartphones by a 2007 BlackBerry."
    - **The build-out is historic.** He calls the AI data-center boom the largest capital project in recorded human history — "larger than the Moon Landing and the Manhattan Project combined" — and notes one leading lab's revenue scaled from roughly \$1B to \$45B annualized in fifteen months. Even where parts of it are a bubble, "bubbles build infrastructure."
    - **The risks are civilizational.** Biosecurity (chatbots that coach on engineering pathogens), cybersecurity (frontier models that can probe power grids and water systems), and — above all — **power**. He invokes the "**Intelligence Curse**": if the machines do the work, the people who own them no longer need the rest of us as workers, soldiers, taxpayers, or voters, dissolving the "no taxation without representation" bargain on which democracy was built.
    - **But the answer is not "shut it down."** A blanket moratorium, Bregman argues, is *the left's own version of climate denial* — refusing to engage in the hope the future goes away. He calls instead for **state capacity** (institutes that evaluate frontier models the way the FDA evaluates drugs), **international coordination** (on the model of nuclear-arms treaties), democracies that actually **build**, and a **positive vision** (basic income, shorter work weeks) so the productivity gains are not captured by a tiny ownership class.

    Whatever you make of his timeline, the essay is a sharp prompt for this course: **disengagement is itself an ethical choice.** Of one lab's decision to withhold a model it judged too dangerous to release, Bregman warns — "conscience is not a policy."

    *Worth weighing against this lesson's companion on the [Environmental &amp; Health Impacts](environment.md) of the very build-out Bregman urges democracies to accelerate — fast data-center permitting reads differently from the fenceline of a gas-fired turbine.*

To illustrate the sheer scale of that build-out, Bregman points to a chart from researcher **Fin Moorhouse** — total capital spending on AI data centers set against history's great megaprojects:

<figure>
<blockquote class="twitter-tweet" data-dnt="true"><a href="https://twitter.com/finmoorhouse/status/2044933442236776794"></a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<figcaption>The chart Bregman cites for the scale of the AI build-out — spending on data centers that he calls "larger than the Moon Landing and the Manhattan Project combined." Source: <a href="https://x.com/finmoorhouse/status/2044933442236776794" target="_blank" rel="noopener noreferrer">Fin Moorhouse</a>. (If the embed doesn't load, open the post directly.)</figcaption>
</figure>

## Bill Gates: "We are not preparing for it" (2026)

!!! Quote ":material-bullhorn: Bill Gates — 'The turbulent AI era is here. The choices we make now are critical.' (2026)"

    In an [almost 6,000-word essay](https://www.gatesnotes.com/a-turbulent-ai-era-and-critical-choices-to-make){target=_blank} published August 26, 2026 — a sharp turn from his enthusiastic 2023 "Age of AI" letter — Microsoft co-founder **Bill Gates** writes:

    > Even under the best circumstances, the transition to this new AI era will be one of the most turbulent times in human history. ... Right now, we are not preparing for it.

    His argument, condensed:

    - **Entry- and mid-level jobs are the most exposed** — white-collar and manual alike — and waiting until people are actually displaced "will be too late."
    - **"Human Reserved" jobs.** Gates proposes deliberately keeping some occupations for people, on a nature-reserve analogy: land where development is restricted because something there is worth preserving. The essay's examples run to caregiving, education, and mental-health roles; in an [accompanying interview](https://techcrunch.com/2026/08/26/bill-gates-wants-to-see-a-robot-tax-and-human-reserved-jobs-to-mitigate-harms-from-ai/){target=_blank} he floated childcare and jury service, and suggested up to ~40% of jobs could initially be reserved.
    - **Tax tokens and robots.** Hiring a person incurs payroll taxes; buying a robot is usually a write-off. Gates calls correcting that imbalance — taxing AI tokens and robots to fund retraining and stronger safety nets — "a change to the tax system that's greater than any in my lifetime."
    - **Chatbots vs. critical thinking.** Companion AIs engineered never to challenge you are addictive at "the worst possible time for humans to lose their critical thinking skills," amid deepfakes and personalized misinformation — and he urges international cooperation on AI governance.

    *For a skeptical read on whether these prescriptions could work, see [ABC News's expert critique](https://abcnews.com/Business/bill-gates-diagnoses-problems-ai-expert-questions-prescription/story?id=135966993){target=_blank}; more coverage at [CNBC](https://www.cnbc.com/2026/08/26/bill-gates-ai-jobs-economic-upheaval.html){target=_blank} and [MIT Technology Review](https://www.technologyreview.com/2026/08/26/1142946/bill-gates-ai-danger-threshold/){target=_blank}.*

**Where the two essays collide.** Bregman and Gates both reject "shut it down," and both insist capacity must be built *before* the disruption arrives. They diverge on emphasis: Bregman on political mobilization and state evaluation institutes, Gates on economic transition design — reserved jobs and token-tax redistribution. Underneath both sits the [Turing Trap](legal.md#foundations-of-the-ethical-principles-for-ai): an economy that rewards replacing humans rather than augmenting them. And both essays presume the very build-out whose local costs are the subject of the [Environmental & Health Impacts](environment.md) lesson.

## AI Constitutions, Bills of Rights, and Pope Leo XIV's encyclical

The deeper treatment of foundational governance documents for AI — corporate "AI constitutions" like Anthropic's *Claude Constitution*; the public *Blueprint for an AI Bill of Rights*; sociologist Alondra Nelson's "civic grammar" framework, T. H. Marshall's social-citizenship argument, and the three-imperatives framework from Nelson's *Daedalus* essay; and Pope Leo XIV's May 2026 encyclical *Magnifica Humanitas* — has been consolidated into the [Ethical & Legal Considerations](legal.md) lesson, where the U.S. Executive Orders, international agreements, and congressional context already live. Two anchors:

- [Blueprint for an AI Bill of Rights](legal.md#blueprint-for-an-ai-bill-of-rights) — the policy timeline; Nelson's "civic grammar"; the cross-partisan diffusion of state-level AI bills (Connecticut, Oklahoma, Florida, the Student AI Bill of Rights); T. H. Marshall's social-citizenship framework; the three imperatives for studying AI; international convergence; the limits of rights talk; and the gap between declaration and enforcement.
- [Catholic social teaching: *Magnifica Humanitas*](legal.md#catholic-social-teaching-magnifica-humanitas-pope-leo-xiv-2026) — Pope Leo XIV's first encyclical and its convergence with the civic-grammar critique of corporate self-governance.
- [Case study: the OpenAI and Hugging Face incident (July 2026)](legal.md#case-study-the-openai-and-hugging-face-incident-july-2026) — what happened when a frontier lab's evaluation agents reached a third party's production infrastructure, and the legal and policy fallout.

## [:material-scale-balance: Ethical and Legal Considerations](legal.md)

## [:material-mirror: Transparency & Accountability](transparency.md)

## [:simple-weightsandbiases: Bias & Discrimination](bias.md)

## [:material-leaf: Environmental & Health Impacts](environment.md)


## Assessment

??? Question "Can you explain the difference between "Ethics of AI" and "Ethical AI?""

    Hint: Refer to how [Siau and Wang (2020)](#ethics-of-artificial-intelligence) define each term

    ??? Success "Ethics of AI"

        * **Ethics of AI** refers to principles and regulations

    ??? Success "Ethical AI"

        * **Ethical AI** focuses on how AI behaves

??? Question "How does Asimov's Three Laws of Robotics relate to modern ethical concerns of AI?"

    ??? Success "Do no harm"

        Asmiov emphasizes preventing harm to humans and how that concept informs current AI safety practices.

??? Question "True or False: The Turing Trap suggests that efforts to make AI more human-like will empower workers' economic and political power."

    ??? Failure "False"

        The Turing Trap warns against replacing humans with AI, and that AI could be used to drive down wages and to a loss of economic and political power. 

??? Question "Name at least one major declaration or agreement on AI Ethics"

    ??? Success "International Agreements"
             
        * Council of Europe Framework Convention on Artificial Intelligence and human rights

        * Political Declaration on Responsible Military Use of Artificial Intelligence and Autonomy

        * G20 AI Principles
    
    ??? Success "Principles and Ethics"

        * Asilomar AI Principles

        * UNESCO Recommendation on the Ethics of Artificial Intelligence

        * OECD AI Principles

        * Toronto Declaration

??? Question "True or False: It is okay to use a GPT to write a research proposal on a topic you have no experience in?"

    Hint: Review ["Using AI Ethically"](#using-ai-ethically)

    ??? Failure "False"

        If you do not have the ability to verify output truthfully or accurately, it is not safe to use a GPT for research.

??? Question "Bregman ('An Inconvenient Truth About AI') and Gates ('The turbulent AI era is here') both reject shutting AI development down. Name one concrete policy each proposes, and identify the assumption both prescriptions share."

    ??? Success "One answer"

        **Bregman:** state capacity — institutes that evaluate frontier models the way the FDA evaluates drugs (also treaty-style international coordination, and a positive vision such as basic income or shorter work weeks). **Gates:** "Human Reserved" jobs, and a tax on tokens and robots to fund the transition. **Shared assumption:** the disruption arrives regardless of our comfort with it, so institutional and economic capacity must be built *before* displacement — Bregman's failure mode is disengagement ("AI denial"); Gates's is unpreparedness ("Right now, we are not preparing for it"). Both treat waiting as itself an ethical choice.

---

**Last Updated:** August 2026
