# Public Health 

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## [:material-run-fast: Bias and Data Quality](../../bias.md)

## [:material-run-fast: Ethics: Transparency & Accountability](../../transparency.md)

## Standardization 

The standardization of protocols and controls is critical for ensuring consistent, high-quality public health practices across different organizations and regions. 

**AI Protocol Analysis and Harmonization**

AI can analyze multiple existing protocols to identify commonalities, differences, and best practices:

??? Question "Example prompt"

    ```markdown
    Analyze different measles testing protocols from various health departments
    in Arizona, Texas, New Mexico, Sonora, and Chihuahua. 
    Identify:
    - Common required steps across all protocols
    - Key differences in methodology
    - Best practices that appear in multiple protocols
    - Potential gaps or missing elements
    - Recommendations for a standardized protocol
    ```

**Natural Language Processing for Protocol Extraction**

AI can extract structured information from unstructured protocol documents:

- Convert narrative guidelines into step-by-step procedures
- Identify required equipment, materials, and personnel
- Extract critical values, thresholds, and decision points
- Create standardized terminology mappings

**Automated Protocol Validation**

AI systems can check protocols for:
- Completeness (all necessary steps included)
- Consistency (no contradictory instructions)
- Compliance with regulations and standards
- Evidence-based practice alignment

### Human-in-the-Loop (HITL) Approaches

Human-in-the-loop systems combine AI efficiency with human expertise to improve accuracy and reliability:

**Key HITL Components:**

- **Expert Annotation**: Subject matter experts review and annotate AI-generated protocols
- **Iterative Refinement**: AI learns from expert corrections to improve future outputs
- **Decision Points**: Critical decisions require human approval before proceeding
- **Quality Assurance**: Random sampling and human verification of AI outputs

### Key Infrastructure Requirements

- **Scalability**: Handle increasing protocol volumes and complexity
- **Interoperability**: Connect with existing health information systems
- **Security**: Protect sensitive health information
- **Reliability**: 99.9% uptime for critical health operations
- **Traceability**: Complete audit trails for regulatory compliance

### Implementation Considerations

- **Change Management**: Training staff on new AI-assisted workflows
- **Ethical Guidelines**: Ensuring AI decisions are fair and unbiased
- **Regulatory Compliance**: Meeting local and federal health regulations
- **Performance Monitoring**: Tracking AI accuracy and human satisfaction
- **Continuous Learning**: Regular model updates based on new evidence

### Best Practices for Implementation

1. **Start Small**: Pilot with non-critical protocols first
2. **Maintain Transparency**: Document AI decision-making processes
3. **Preserve Expertise**: AI augments, not replaces, human judgment
4. **Regular Audits**: Systematic review of AI performance
5. **Stakeholder Engagement**: Include all users in design and testing
6. **Continuous Training**: Keep both AI models and humans updated

Human-in-the-loop approaches that improve accuracy and reliability, combined with robust AI infrastructure, allow for more seamless integration into public health practices while maintaining the critical human oversight necessary for healthcare decision-making. 

## Case Studies

#### :simple-awesomelists: Awesome Lists

Maintained on GitHub and often feature the badge: [![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome?tab=readme-ov-file#health-and-social-science){target=_blank}, Awesome lists contain community-maintained lists of popular and widely used software, data, and code for almost everything on the internet.

* [:simple-awesomelists: Awesome Healthcare](https://github.com/kakoni/awesome-healthcare#readme){target=_blank}

* [:simple-awesomelists: Awesome Healthcare Datasets](https://github.com/geniusrise/awesome-healthcare-datasets){target=_blank}

### Diagnostics

AI has great promise for enhancing diagnostic capabilities, but have exhibited [biases on race and ethnicity](https://www.nytimes.com/2021/03/15/technology/artificial-intelligence-google-bias.html){target=_blank}. There are calls to address these biases in big data and AI for health care by taking an [open science approach](https://pmc.ncbi.nlm.nih.gov/articles/PMC8515002/){target=_blank}


List of FDA approved AI medical devices: [https://www.datawrapper.de/_/IBGhg/](https://www.datawrapper.de/_/IBGhg/)


<iframe
	src="https://www.datawrapper.de/_/IBGhg/"
	frameborder="0"
	width="850"
	height="450"
></iframe>

**Positive Examples**

High speed internet access via wired, broadband, or satellite allows clinicians to stream data to the cloud and larger AI resources and improved access to specialty care in Underserved and Rural Areas.

**Negative Examples:**

* AI-enabled pulse oximeters overstate blood oxygen saturation in individuals with darker skin, [exacerbating racial bias](https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism){target=_blank}

**Readings:**

* [https://www.medtechdive.com/news/fda-ai-medical-devices-growth/728975/](https://www.medtechdive.com/news/fda-ai-medical-devices-growth/728975/){target=_blank}

* [https://nam.edu/perspectives/advancing-artificial-intelligence-in-health-settings-outside-the-hospital-and-clinic/](https://nam.edu/perspectives/advancing-artificial-intelligence-in-health-settings-outside-the-hospital-and-clinic/){target=_blank}

* [https://www.nature.com/articles/s41746-018-0040-6](https://www.nature.com/articles/s41746-018-0040-6){target=_blank}

* [https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/){target=_blank}

### Disease Surveillance & Prediction

AI-powered predictions change the landscape of population-level public health surveillance. 

Machine learning (predictive AI) has been used for many years to analyze data and make predictions around [disease spread and outbreak detection](https://www.preprints.org/manuscript/202504.1250/v1){target=_blank}. 

AI-systems can quickly analyze electronic health records (EHRs), social media platforms, online search queries, environmental data, genomic sequences, wearable devices, 
Of course. Here is the updated markdown table with public URLs for every example. Any examples for which I could not find a reliable, public URL have been removed.

| Application Area | AI Technique(s) Used | Data Sources Leveraged | Specific Examples/Platforms | Key Outcomes/Impacts |
| --- | --- | --- | --- | --- |
| Early Outbreak Detection | Machine Learning, NLP | Social Media, News Reports, Airline Travel Data, Official Health Reports | [BlueDot](https://bluedot.global/), [HealthMap](https://www.healthmap.org/en/) | Early warning for COVID-19 by detecting initial signals before official reports; faster public health response. |
| Real-Time Monitoring | Machine Learning, NLP | EHRs, Lab Reports, Public Health Data, Free-text data | [CDC NLP analysis for vaccine safety](https://www.cdc.gov/csels/dmi/projects/ai-ml.html) | Continuous tracking of disease spread and monitoring safety of vaccines by analyzing large volumes of free-text data. |
| Epidemic Forecasting | Machine Learning, Deep Learning | Historical Disease Data, Climate Patterns, Population Mobility, Search Queries | [CDC FluSight](https://www.cdc.gov/flu-forecasting/data-vis/current-week.html), [Dengue/Influenza models](https://doi.org/10.1038/s41598-025-85437-w) | Improved prediction accuracy for flu seasons, dengue outbreaks; better preparedness. |
| Identifying High-Risk Populations | Machine Learning | Demographic, Socioeconomic, Health Data, Aerial Imagery | [TowerScout](https://www.ischool.berkeley.edu/projects/2020/towerscout) | Enables targeted interventions, such as identifying cooling towers from imagery to speed up response to Legionnaires' disease outbreaks. |
| Pathogen Genomic Surveillance | AI Algorithms, Machine Learning | Genomic Sequences of Pathogens | [Nextstrain](https://nextstrain.org/) | Rapid detection of new variants (e.g., SARS-CoV-2), understanding transmissibility/virulence changes. |
| Syndromic Surveillance (Unconv.) | NLP, Machine Learning, Image Analysis | Online Search Queries, Social Media Posts, Wikipedia page views, Chest X-rays | [AI for TB detection from X-rays](https://delft.care/cad4tb/) | Early detection of community transmission before clinical reporting and improved speed and accuracy for TB surveillance. |
| Antimicrobial Resistance (AMR) Tracking | Predictive Analytics, ML | Clinical Data, Epidemiological Data, Lab Results | [AI-driven AMR surveillance systems](https://www.mdpi.com/2079-6382/12/5/861) | Improved detection of AMR trends, rapid pathogen ID and resistance profiling, guidance for stewardship. |
| Vector-Borne Disease Prediction | Machine Learning | Environmental Data (temp, humidity, rainfall), Satellite Imagery, Historical Case Data | [AI models for Malaria prediction](https://gcgh.grandchallenges.org/grant/ai-based-malaria-incidence-prediction-under-current-and-future-climate-southern-ethiopia-aim) | Prediction of high-risk areas for outbreaks, enabling targeted vector control measures. |
| Resource Allocation Prediction | Machine Learning | Outbreak Data, Hospital Capacity Data, Supply Chain Information | [NHS A&E demand forecasting tool](https://www.england.nhs.uk/2023/08/ai-tool-improving-outcomes-for-patients-by-forecasting-ae-admissions/) | Optimization of resource deployment during public health emergencies. |
| Misinformation Monitoring | NLP | Social Media Content, Online News | [Project Heal](https://www.healthcareitnews.com/news/cloud-based-ai-services-could-help-fight-health-misinformation), [EPIWATCH](https://kirby.unsw.edu.au/news/new-grant-help-detect-and-counter-public-health-fake-news) | Identification of false narratives that could impede public health responses, enabling counter-messaging. |

**Readings:**

* [Zeng et al. (2021) Artificial intelligence–enabled public health surveillance—from local detection to global epidemic monitoring and control. Artificial Intelligence in Medicine Technical Basis and Clinical Applications](https://doi.org/10.1016/B978-0-12-821259-2.00022-3){target=_blank}

* [Hattab, G. et al. (2025) The Way Forward to Embrace Artificial Intelligence in Public Health. American Journal of Public Health 115, 123_128](https://doi.org/10.2105/AJPH.2024.307888){target=_blank}

### Resource Allocation

Perhaps the most ethically fraught application of AI in health care is on resource allocation. Decisions made by algorithms for high-risk care have exhibited racial biases. 

**Positive Examples:**

* The UK's National Health Service (NHS) uses an AI-powered tool to forecast demand for emergency services, helping to optimize the allocation of staff, beds, and other resources to improve patient outcomes. ([Read more](https://www.england.nhs.uk/2023/08/ai-tool-improving-outcomes-for-patients-by-forecasting-ae-admissions/){target=_blank})

**Negative Examples:**

* Training data based on historical spending for health care on black vs white patients resulted in an algorithm systematically biased toward spending on more on white patients than on black patients, resulting in a perpetuation and exacerbation of the health disparity. 

### Clinical Decision Support

AI-powered tools can assist healthcare providers in making more informed decisions, but they must be used with caution as they can also perpetuate existing biases.

**Positive Examples:**

* **Oncology Screening:** [Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology](https://www.nature.com/articles/s43018-025-00991-6){target=_blank}
* **Diabetic Retinopathy Detection:** AI systems like [LumineticScore](https://www.digitaldiagnostics.com/products/eye-disease/lumineticscore/){target=_blank} can analyze retinal images to detect diabetic retinopathy, a leading cause of blindness, enabling early intervention and treatment, particularly in areas with limited access to specialists.
* **Drug Discovery:** Language models like [Google's TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/){target=_blank} are being developed to accelerate drug discovery by understanding and predicting the properties of therapeutic compounds.
* **Diagnostic Conversations:** Research systems like [Google's AMIE](https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/){target=_blank} are exploring the potential for AI to conduct diagnostic conversations and improve medical reasoning. ([Read more](https://doi.org/10.48550/arXiv.2401.05654){target=_blank})

**Negative Examples:**

* **Skin Cancer Detection:** AI models for detecting skin cancer have shown lower accuracy on darker skin tones, which can lead to missed or delayed diagnoses for patients from underrepresented racial and ethnic groups.


### Mental Health

The application of AI in mental health presents both significant opportunities and serious risks, particularly concerning the well-being of vulnerable populations.

**Positive Examples:**

* **Increased Access to Care:** AI-powered chatbots and virtual therapists can help mitigate shortages of mental health providers, especially in rural and underserved areas, by offering accessible, on-demand support. ([Read more](https://www.nytimes.com/2025/04/15/health/ai-therapist-mental-health.html){target=_blank})
* **Potential for Effective Treatment:** Early research suggests that generative AI chatbots may become a valuable tool in mental health treatment, with some studies showing promising outcomes. ([Read the study](https://ai.nejm.org/doi/full/10.1056/AIoa2400802){target=_blank})
* **Positive Mental Health:** AI is being explored for applications in positive psychology, focusing on well-being and flourishing. ([Read the review](https://doi.org/10.3389/fdgth.2024.1280235){target=_blank})

**Negative Examples:**

* **Unregulated and Unaccountable Care:** The proliferation of unlicensed and unaccountable AI chatbots posing as therapists raises serious ethical concerns, as they may provide harmful advice or fail to respond appropriately in crisis situations. ([Read more](https://www.nytimes.com/2025/02/24/health/ai-therapists-chatbots.html){target=_blank})
* **Risk of Harm:** Unregulated AI has been accused of contributing to negative mental health outcomes, including exacerbating distress, cyberbullying, and even being implicated in cases of suicide.
* **Lack of Oversight:** There is currently little regulatory oversight for AI therapy companies, creating a gap in ensuring the safety and effectiveness of these services. ([Read more](https://www.apaservices.org/practice/business/technology/artificial-intelligence-chatbots-therapists){target=_blank})



## Further Reading



[WHO Guidance: Ethics and Governance of Artificial Intelligence for Health](https://iris.who.int/bitstream/handle/10665/341996/9789240029200-eng.pdf){target=_blank}

[Focus Group on "Artificial Intelligence for Health" (FG-AI4H)](https://www.itu.int/en/ITU-T/focusgroups/ai4h/Pages/default.aspx){target=_blank}
