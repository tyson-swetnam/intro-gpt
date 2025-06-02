# Public Health 

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## [:material-run-fast: Bias and Data Quality](../../bias.md)

## [:material-run-fast: Ethics: Transparency & Accountability](../../transparency.md)

## Standardization 

Standardization of protocols and controls are also requested.

Human-in-the-loop approaches that improve accuracy and reliability

Robust AI infrastructure to allow for more seamless integration into public health practices. 

## Case Studies end Examples

### Diagnostics

AI has great promise for enhancing diagnostic capabilities, but have exhibited [biases on race and ethnicity](https://www.nytimes.com/2021/03/15/technology/artificial-intelligence-google-bias.html){target=_blank}. There are calls to address these biases in big data and AI for health care by taking an [open science approach](https://pmc.ncbi.nlm.nih.gov/articles/PMC8515002/){target=_blank}

* AI-enabled pulse oximeters overstate blood oxygen saturation in individuals with darker skin, [exacerbating racial bias](https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism){target=_blank}

* AI techniques for detecting skin cancer have lower accuracy on dark skin.


### Disease Surveillance & Prediction

AI-powered predictions change the landscape of population-level public health surveillance. 

Machine learning (predictive AI) has been used for many years to analyze data and make predictions around [disease spread and outbreak detection](https://www.preprints.org/manuscript/202504.1250/v1){target=_blank}. 

AI-systems can quickly analyze electronic health records (EHRs), social media platforms, online search queries, environmental data, genomic sequences, wearable devices, 

| Application Area | AI Technique(s) Used | Data Sources Leveraged | Specific Examples/Platforms | Key Outcomes/Impacts |
| --- | --- | --- | --- | --- | 
| Early Outbreak Detection | Machine Learning, NLP | Social Media, News Reports, Airline Travel Data, Official Health Reports | [BlueDot](https://bluedot.global/){target=_blank}, [HealthMap](https://www.healthmap.org/en/){target=_blank} | Early warning for COVID-19, Zika; faster public health response | 
| Real-Time Monitoring | Machine Learning | EHRs, Lab Reports, Public Health Data | Various research models, hospital surveillance systems | Continuous tracking of disease spread and intensity | 
| Epidemic Forecasting | Machine Learning, Deep Learning | Historical Disease Data, Climate Patterns, Population Mobility, Search Queries | [Google Flu Trends (deprecated)](https://en.wikipedia.org/wiki/Google_Flu_Trends), [CDC FluSight](https://www.cdc.gov/flu-forecasting/data-vis/current-week.html){target=_blank}, [Dengue/Influenza prediction models](https://doi.org/10.1038/s41598-025-85437-w){target=_blank} | Improved prediction accuracy for flu seasons, dengue outbreaks; better preparedness | 
| Identifying High-Risk Populations | Machine Learning | Demographic, Socioeconomic, Health Data | Models for predicting vulnerability to specific diseases or severe outcomes | Enables targeted interventions and resource allocation to most vulnerable groups |
| Pathogen Genomic Surveillance | AI Algorithms, Machine Learning | Genomic Sequences of Pathogens | Systems for analyzing viral/bacterial genomes | Rapid detection of new variants (e.g., SARS-CoV-2), understanding transmissibility/virulence changes |
| Syndromic Surveillance (Unconv.) | NLP, Machine Learning | Online Search Queries (symptoms), Social Media Posts (symptom mentions) | Google Flu Trends, models analyzing Twitter/Facebook data | Early detection of community transmission before clinical reporting |
| Antimicrobial Resistance (AMR) Tracking | Predictive Analytics, ML | Clinical Data, Epidemiological Data, Lab Results | AI-driven AMR surveillance systems | Improved detection of AMR trends, rapid pathogen ID and resistance profiling, guidance for stewardship |
| Vector-Borne Disease Prediction | Machine Learning | Environmental Data (temp, humidity, rainfall), Satellite Imagery, Historical Case Data | AI models for Malaria, Dengue, Zika prediction | Prediction of high-risk areas for outbreaks, enabling targeted vector control measures |
| Resource Allocation Prediction | Machine Learning | Outbreak Data, Hospital Capacity Data, Supply Chain Information | Models forecasting demand for medical supplies, beds, personnel | Optimization of resource deployment during public health emergencies | 
| Misinformation Monitoring | NLP | Social Media Content, Online News | AI tools tracking health-related misinformation | Identification of false narratives that could impede public health responses, enabling counter-messaging |


* [Zeng et al. (2021) Artificial intelligence–enabled public health surveillance—from local detection to global epidemic monitoring and control. Artificial Intelligence in Medicine Technical Basis and Clinical Applications](https://doi.org/10.1016/B978-0-12-821259-2.00022-3){target=_blank}

* [Hattab, G. et al. (2025) The Way Forward to Embrace Artificial Intelligence in Public Health. American Journal of Public Health 115, 123_128](https://doi.org/10.2105/AJPH.2024.307888){target=_blank}

### Resource Allocation

Perhaps the most ethically fraught application of AI in health care is on resource allocation. Decisions made by algorithms for high-risk care have exhibited racial biases. 

* Training data based on historical spending for health care on black vs white patients resulted in an algorithm systematically biased toward spending on more on white patients than on black patients, resulting in a perpetuation and exacerbation of the health disparity. 

### Clinical Decision Support


[Google's TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/){target=_blank}, a collection of language models aimed at helping pharmaceutical companies with drug discovery.

TxGemma understands and predicts the properties of therapeutic entities — throughout the entire discovery process, from identifying promising targets to helping predict clinical trial outcomes. 

[https://deepmind.google/models/gemma/txgemma/](https://deepmind.google/models/gemma/txgemma/)

[Google's Articulate Medical Intelligence Explorer (AMIE)](https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/){target=_blank} A research AI system for diagnostic medical reasoning and conversations

* [Tu et al. (2024) Towards Conversational Diagnostic AI](https://doi.org/10.48550/arXiv.2401.05654){target=_blank}


### Mental Health

Unregulated AI is dangerous to the mental health of vulnerable populations. AI has been accused of contributing to individuals suicide, exacerbating distress, and cyberbullying. Unlicensed and unaccountable [AI chatbots are posing as therapists](https://www.nytimes.com/2025/02/24/health/ai-therapists-chatbots.html).

AI therapy companies are proliferating, but [there is little oversight](https://www.apaservices.org/practice/business/technology/artificial-intelligence-chatbots-therapists). Evidence of AI therapy effectiveness on mental health is still forthcoming, but some [early research](https://ai.nejm.org/doi/abs/10.1056/AIoa2400802){target=_blank} suggest AI may become a valuable tool and [help to mitigate national and rural provider shortages](https://www.nytimes.com/2025/04/15/health/ai-therapist-mental-health.html){target=_blank}. 

* [Heinz et al. (2025) Randomized Trial of a Generative AI Chatbot for Mental Health Treatment. NEJM AI 2025;2(4)](https://ai.nejm.org/doi/full/10.1056/AIoa2400802){target=_blank}

* [Thakkar et al. (2024) Artificial Intelligence in positive mental health: a narrative review. Front Digit Health. 2024 Mar 18;6:1280235](https://doi.org/10.3389/fdgth.2024.1280235){target=_blank}



## Further Reading



[WHO Guidance: Ethics and Governance of Artificial Intelligence for Health](https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf){target=_blank}

[Focus Group on "Artificial Intelligence for Health" (FG-AI4H)](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Pages/default.aspx){target=_blank}