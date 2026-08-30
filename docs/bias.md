---
type: Ethics Guide
title: Bias and Discrimination
description: >-
  Sources of AI bias, prevention strategies, real public-health harms, and a
  2026 Nature study of state-media influence on LLMs across query languages.
resource: https://tyson-swetnam.github.io/intro-gpt/bias/
tags: [ethics, bias, public-health]
sources:
  - resource: https://www.science.org/doi/10.1126/science.aax2342
    title: Dissecting racial bias in an algorithm used to manage the health of populations
    author: Obermeyer et al.
  - resource: https://www.nature.com/articles/s41586-026-10506-7
    title: State media control influences large language models
    author: Waight, Yang, Yuan et al.
  - resource: https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism
    title: Algorithms in Health Care May Worsen Medical Racism
  - resource: https://huggingface.co/datasets/uonlp/CulturaX
    title: CulturaX multilingual training corpus
  - resource: https://www.nature.com/articles/d41586-026-01486-9
    title: State media control shapes LLM behaviour by influencing training data
generated:
  by: human:tswetnam
  at: "2026-06-03T23:27:38Z"
verified:
  - by: human:tswetnam
    at: "2026-06-03T23:27:38Z"
status: stable
---

# Bias and Discrimination

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

This lesson addresses the critical challenges of bias in AI. We will briefly explore their origins, impacts, and strategies for recognizing, mitigating, and preventing them.

## Understanding AI bias & its origins

!!! Info "Definitions"

    **AI Bias** - occurs when an AI system produces systematically prejudiced or unfair results (outputs). Erroneous assumptions made during the development of the model, or biases in the data upon which it was trained are both potential sources.

    **Algorithmic Discrimination** occurs when an the use of an AI results in the unfair or illegal treatment of individuals or groups based on a protected characteristic (age, disability, race, religion, sex, or socioeconomic status).

    **Fairness** includes metrics around equalized error rates across groups and parity of outcomes across groups. 

## Sources of Bias

**Algorithmic** - when the algorithm used to process the information prioritizes certain features over others, e.g. optimization techniques that favor majority over minority groups

**Data** - the most common source of AI bias is when the data used to train a model are flawed, unrepresentative, lack global diversity, and do not reflect the ground truth of the real-world 

* **Selection Bias** when training data are not representative of the whole population 

* **Measurement Bias** when the data systematically differs from the true values, or when proxies are used

* **Exclusion Bias** when certain types or groups are omitted from data collection

* **Experience or Expertise Bias** when subjective judgements among the collectors, labellers, or data input are introduced

* **Environment Bias** when data collected in one context are not generalizable to other contexts

**Human Decision** - when biases held by humans influence the decisions around data labeling, model development, engineering or outputs

* **Confirmation Bias** - over reliance on pre-existing beliefs or patterns in data
    
* **Stereotyping Bias** - perpetuation of a labeling bias that is harmful to specific groups

* **Out-Group Bias** - generalizing underrepresented groups as being more similar to one another than they actually are

* **Empathy Bias** - inability to incorporate nuanced human experiences, emotions, or subjective elements into a quantitative model

**Synthetic Bias** - when models based on biased training data are used to generate synthetic datasets, they perpetuate their bias into the new trained model

## Bias prevention strategies

### Data-centric approaches 

Can help to ensure data are representative, high quality, and contain the diversity of the study system:

**Collection** - curate datasets accurately to represent all relevant groups and populations.

**Quality** - identify and address issues within data sets, including compatibility problems, gaps within populations, and underrepresentation in historical data. 
 
**Balancing** - under-sample majority and over-sample minority groups, use synthetic data generation to capture under-represented samples

**Labeling** - consistent, annotated, with masks for irrelevant factors, sensitive and secure

**Continuous** - data are updated throughout the entire lifecycle of their use, not just a single collection phase.

### Algorithmic Techniques

Technical tools can help to identify bias in models:

**Bias Detection** - [specialized software tools](https://dialzara.com/blog/10-top-tools-for-ethical-ai-development-2024/) designed to flag, measure, and analyze biases.

**Fairness Metrics** - equalized odds, demographic parity, counterfactual fairness

**Algorithmic Adjustments** - pre-processing (adjusting training data), in-process (modifying algorithm), or post-processing (adjust outputs)

**Explainable AI (XAI)** - understand which inputs are driving model decisions, reveal hidden biases or reliance on spurious factors

## Concrete examples in public health

The categories above are easier to remember when you can map each to a deployed system that caused real harm. Three to anchor:

!!! Warning "Pulse-oximeter racial bias (measurement bias)"
    AI-enabled pulse oximeters [overstate blood-oxygen saturation in patients with darker skin](https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism){target=_blank}. Any downstream system that ingests sat readings — clinical decision support, severity scoring, an LLM that classifies SMS triage based on "the patient said sat 92" — inherits that bias. This is **measurement bias**: the data systematically differs from the true value, and the difference is patterned by skin tone.

!!! Warning "Historical-spending bias in care allocation (selection / measurement bias)"
    A widely deployed U.S. care-allocation algorithm [systematically routed less care to Black patients than to White patients](https://www.science.org/doi/10.1126/science.aax2342){target=_blank} (Obermeyer et al., 2019, *Science*) because it was trained on historical health-care **spending** as a proxy for medical need. Spending was lower for Black patients not because they were healthier but because they had less access. Any outbreak-prioritization or resource-allocation prompt that learns from past response patterns will reproduce past inequities.

!!! Warning "Training-scope bias in dermatology and retinopathy (selection bias)"
    AI dermatology and retinopathy models trained predominantly on lighter-skinned cohorts perform measurably worse on darker skin — a clear **selection bias** in the training data. The same logic applies to clinical text: if your chart-abstraction model has not seen code-switched notes or local abbreviations, the silent-failure rate on those records is higher. When you build LLM workflows on top of clinical data, the abstention rate (how often the model says "UNCLEAR") on under-represented inputs is your early-warning signal.

## A 2026 case study: state-media bias across query languages

Waight, Yang, Yuan and colleagues (2026) provide one of the first large-scale empirical demonstrations that authoritarian information ecosystems leave measurable fingerprints on commercial LLMs used by hundreds of millions of people. The University of Oregon-led team published their findings in *Nature*: **["State media control influences large language models"](https://www.nature.com/articles/s41586-026-10506-7){target=_blank}** ([DOI: 10.1038/s41586-026-10506-7](https://doi.org/10.1038/s41586-026-10506-7){target=_blank}).

**What they did**

The authors traced the pathway from online media to training data to model behavior through four converging methods:

1. **Training-corpus analysis** — a 5-word-gram similarity audit of [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX){target=_blank} (a widely-used multilingual training corpus) found that **~3.1 million Chinese-language documents (1.64%) match state-coordinated media corpora — roughly 41× the rate of Chinese Wikipedia.** For documents mentioning Chinese political leaders or institutions, match rates climbed as high as **24%**.
2. **Small-model training experiments** — replicating the corpus → behavior effect by training their own models on controlled mixes.
3. **Human evaluation** of model outputs across paired prompts.
4. **Real-world chatbot audits** — dual audits comparing the same query in Chinese vs. English against commercial LLMs about Chinese government and political entities.

The pattern was then replicated across **37 countries** with varying levels of media freedom.

**Key finding**

> Responses generated in Chinese are markedly more favorable toward China's institutions and leaders than the English-language counterparts to the same query, on the same model. Models queried in the languages of countries with lower media freedom show a stronger pro-regime valence than models queried in the languages of countries with higher media freedom.

In bias-taxonomy terms, this is **data bias** with a new dimension: the same model can have different ideological valences depending on the query language, because each language slice of the training data is dominated by different source corpora — and those source corpora reflect the editorial control of the states that produce them.

**Why this matters for the workshop**

- **Translation is not neutral.** Asking the same question of the same LLM in English vs. Mandarin (or Russian, or Persian) may produce systematically different answers — not because the model "thinks differently" in each language, but because each language's training data was shaped by different editorial gatekeepers.
- **Standard fairness metrics miss it.** Demographic parity, equalized odds, counterfactual fairness — none directly measure cross-language ideological skew. Detecting it requires the kind of dual-audit methodology Waight et al. demonstrate.
- **It generalizes.** The 37-country replication suggests the mechanism applies wherever state-coordinated media is a significant share of a language's web presence — not just to obvious geopolitical hot-button queries.

For a plain-language summary, see the Nature News & Views companion: [State media control shapes LLM behaviour by influencing training data](https://www.nature.com/articles/d41586-026-01486-9){target=_blank}. The authors also maintain a [project site](https://state-media-influence-llm.github.io/){target=_blank} with replication materials.

## Assessment

??? question "True or False: AI bias only originates from the data used to train the model."

    !!! failure "False"

        AI bias can originate from the data, the algorithm, and human decisions during the development process.

??? question "Which of the following is an example of 'Selection Bias'?"

    A. An algorithm that prioritizes majority groups over minority groups.

    B. A dataset for a skin cancer detection model that predominantly features images of light-skinned individuals.

    C. Subjective judgments from data labelers influencing the data.

    D. Using a model trained on data from one hospital in a different country.

    ??? success "Answer"
        
        **B. A dataset for a skin cancer detection model that predominantly features images of light-skinned individuals.**
        
        Selection bias occurs when the training data are not representative of the whole population.

??? question "What is the primary purpose of 'Explainable AI (XAI)' in bias mitigation?"

    A. To generate synthetic data for underrepresented groups.

    B. To understand which inputs are driving model decisions, potentially revealing hidden biases.

    C. To ensure the model's predictions are always 100% accurate.

    D. To make the model run faster on new hardware.

    ??? success "Answer"

        **B: To understand which inputs are driving model decisions, potentially revealing hidden biases.**
        
        XAI helps to make the model's decision-making process transparent, which is crucial for identifying and addressing bias.

??? question "True or False: 'Algorithmic Discrimination' is when an AI model makes a simple mistake."

    !!! failure "False"

        Algorithmic Discrimination is when the use of an AI results in the unfair or illegal treatment of individuals or groups based on a protected characteristic.

??? question "Which of these is NOT a data-centric approach to bias prevention?"

    A. Curating datasets to accurately represent all relevant groups.

    B. Over-sampling minority groups.

    C. Modifying the algorithm during the training process.

    D. Ensuring data labels are consistent and annotated.

    ??? success "Answer"
        
        **C: Modifying the algorithm during the training process.**

        This is an algorithmic technique, not a data-centric approach.
