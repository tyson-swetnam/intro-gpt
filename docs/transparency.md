# Transparency and Accountability

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Transparency is a cornerstone of developing trust, specifically when AI is involved in research, government, or healthcare.

!!! Info "Definitions"

    **AI transparency** is the degree of openness in a system design, the data that it uses, its operational framework. Transparency includes:
        
    * Access to the data a system was trained upon
    * Explanation of how a model arrives at its decisions
    * List of guardrails, safeguards, and measures in place to mitigate bias

    **Explainable AI (XAI)** focuses on describing specific sequence of steps that an AI model undertakes to arrive at a result, prediction, or response. XAI includes AI transparency and enables comprehension. 

    * [UNESCO's "Transparency and Explainability"](https://www.unesco.org/en/legal-affairs/recommendation-ethics-artificial-intelligence#:~:text=The%20transparency%20and%20explainability%20of,liability%20regimes%20to%20work%20effectively){target=_blank} is a core ethical principle, deeming it essential for the ethical deployment and trustworthy adoption of XAI technologies.

## Establishing Accountability

[**Coalition for Health AI (CHAI)**](https://chai.org/){target=_blank} advances the responsible development, deployment, and oversight of AI in healthcare

[**NIST AI Risk Management Framework (AI RMF)**](https://www.nist.gov/itl/ai-risk-management-framework){target=_blank} has developed a framework to better manage risks to individuals, organizations, and society associated with AI.

[**Organization for Economic Cooperation and Development (OECD) AI Principles**](https://oecd.ai/en/ai-principles){target=_blank} promote use of AI that is innovative and trustworthy and that respects human rights and democratic values.

[**World Health Organization (WHO)**](https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models){target=_blank} has released AI Ethics and governance guidelines for large multi-modal models 

[**EU AI Act**](https://artificialintelligenceact.eu/) is comprehensive legislation that includes oversight of AI with a six year (2031) implementation timeline, which is already underway.

### Mechanisms 

**Audits** - regular systematic audits are essential, these includ bias audits to detect discrimination and fairness evaluations, security vulnerability checks, and performance reviews for accuracy and reliability. 

**Human Oversight** - high risk systems require human-in-the-loop approaches which are validated by human experts before implementation

**Governance Structures** - clear and effective governance structures are fundamental to AI accountability. This involves defined leadership and oversight (boards), where responsibility across organizations is formalized and put into standard operating procedures. 

**Record-keeping / Logs** - traceability and auditability require detailed records of the AI system's operation and user actions. Audit rails provide invaluable resources for incident investigation, understanding system responses, and demonstrating compliance. 

## Transparency

??? Danger "The Black Box Problem :material-box-shadow:"

    Many AI models rely on complex architectures that function as "black boxes," where their internal decision-making processes are opaque and not easily understood by human observers. This lack of transparency creates significant accountability challenges, especially in high-stakes fields like healthcare.

    A real-world example is the case of AI-enabled pulse oximeters, which were found to overstate blood oxygen saturation in individuals with darker skin. This flaw, rooted in biased training data, highlights how a lack of transparency can hide life-threatening biases within a medical device, leading to unequal care. ([Read more at the ACLU](https://www.aclu.org/news/privacy-technology/algorithms-in-health-care-may-worsen-medical-racism){target=_blank})

### Strategies for Mitigation

To counter the black box problem and foster responsible AI, several strategies are essential:

*   **Promoting Data Diversity and Bias Mitigation:** Actively working to ensure training datasets are representative of the entire population to prevent algorithmic bias. This includes collecting more diverse data and using techniques to identify and correct biases in models.
*   **Strengthening Data Security and Privacy:** Implementing robust security measures and privacy-preserving techniques (like federated learning or differential privacy) to protect sensitive data used by AI systems.
*   **Fostering Human-in-the-Loop (HITL) Approaches:** Integrating human expertise and oversight into AI workflows. This ensures that critical decisions are validated by experts and allows for continuous monitoring and correction of AI behavior.
*   **Enhancing Transparency and Explainable AI (XAI):** Developing and deploying XAI methods that can provide clear explanations for how a model arrived at a specific decision. This is crucial for building trust and enabling meaningful audits. For example, the open science movement advocates for making data and models used in health research publicly available to allow for independent verification and scrutiny. ([Learn about Open Science in AI for Health](https://pmc.ncbi.nlm.nih.gov/articles/PMC8515002/){target=_blank})

## Assessment

??? question "True or False: The 'black box' problem refers to the physical appearance of AI hardware."

    !!! failure "False"

        The "black box" problem describes the difficulty in understanding the internal decision-making processes of complex AI models.

??? question "Which of the following is NOT a core component of AI transparency?"

    A. Access to the data a system was trained upon

    B. The speed of the algorithm's computation

    C. Explanation of how a model arrives at its decisions

    D. List of safeguards in place to mitigate bias

    ??? success "Answer"
        
        B. The speed of the algorithm's computation 
        
        While computational speed is a performance metric, it is not a core component of transparency, which focuses on openness, data, and decision-making logic.

??? question "What is the primary goal of Explainable AI (XAI)?"

    A. To make AI models run faster

    B. To describe the steps an AI model takes to reach a result

    C. To replace human oversight entirely

    D. To secure AI systems from cyberattacks

    ??? success "Answer"

        **B: To describe the steps an AI model takes to reach a result**
        
        XAI focuses on making the decision-making process of an AI model understandable to humans.

??? question "True or False: The EU AI Act is a set of voluntary guidelines for companies to consider."

    !!! failure "False"

        The EU AI Act is comprehensive legislation with a formal implementation timeline, making it a mandatory legal framework for AI governance in the European Union.

??? question "Which organization developed the AI Risk Management Framework (AI RMF) to manage risks associated with AI?"

    A. World Health Organization (WHO)

    B. Coalition for Health AI (CHAI)

    C. National Institute of Standards and Technology (NIST)

    D. Organization for Economic Cooperation and Development (OECD)

    ??? success "Answer"
        
        C: National Institute of Standards and Technology (NIST)

        NIST is responsible for the AI Risk Management Framework.
