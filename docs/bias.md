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
