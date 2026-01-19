# Teaching with AI

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

!!! Danger "**Full Disclosure: Material on this website was copy edited or is based on suggestions made by a GPT**"

!!! Question "**Have you integrated AI into your coursework yet?**"

    ??? Failure "No, and thats OKAY!" 

        A thoughtful, wait and see, approach to incorporating AI into your educational material is rational and reasonable.

        Making the decision to incorporate an AI into your education strategy, student assessment, and grading is no easy task. 

        Further, costs and accessibility issues around AI continue to persist across academia. Underserved institutions and colleges with small budgets, or little investment into IT may not have the ability to meet security requirements needed for secure access to student's coursework or personal data (protected by FERPA).

        An important fact to consider though is that [*most* of your students are already making use of AI for their assignments and study.](https://www.gse.harvard.edu/ideas/usable-knowledge/24/09/students-are-using-ai-already-heres-what-they-think-adults-should-know){target=_blank} (ref: [:fontawesome-regular-file-pdf: Source](https://digitalthriving.gse.harvard.edu/wp-content/uploads/2024/06/Teen-and-Young-Adult-Perspectives-on-Generative-AI.pdf){target=_blank} ).

        Read about [:fontawesome-brands-openai: OpenAI Educator Considerations](https://platform.openai.com/docs/chatgpt-education/educator-considerations-for-chatgpt){target=_blank}

    ??? Success "Yes, but go ahead and read on"

        Thats great! 
        
        Make sure to read through the rest of this section to make sure that you're using GPTs in ways that keep your student's data and personal information safe. 
        
        Also, ensure that you're using approved AI software that has been vetted by university security and IT staff.

By 2026, AI has become a transformative force in higher education. Research indicates that approximately 65-75% of faculty at R1 universities have integrated AI tools into their teaching practice, with adoption rates varying by institution type and discipline. Student usage remains even higher, with over 60% of undergraduates regularly using AI for coursework [(EDUCAUSE, 2024)](https://educause.edu){target=_blank}.

GPTs can compose essays, pass advanced tests, and initially appeared as a threat to academic integrity [(Eke 2023)](https://doi.org/10.1016/j.jrt.2023.100060){target=_blank}. Online education faced extreme challenges regarding effective remote student assessment [(Susnjak & McIntosh 2024)](https://doi.org/10.3390/educsci14060656){target=_blank}.

However, attempting to modify coursework to avoid assessment techniques where GPTs excel or using detection tools to identify AI-generated content has proven largely futile [(MIT Sloan EdTech 2024)](https://mitsloanedtech.mit.edu/ai/teach/ai-detectors-dont-work/){target=_blank}. Detection tools produce significant false positives and disproportionately flag work by non-native English speakers [(Liang et al., 2023)](https://doi.org/10.1016/j.patter.2023.100779){target=_blank}; [(Weber-Wulff et al., 2024)](https://doi.org/10.1007/s40979-023-00146-z){target=_blank}.

"**Instead of engaging in a futile cheating arms race, why not embrace AI strategically?**"

Proponents of integrating AI into educational curricula [(:simple-newyorktimes:)](https://www.nytimes.com/2023/01/12/technology/chatgpt-schools-teachers.html){target=_blank} argue that by adapting and integrating GPTs into the curriculum, we also develop a modern workforce who are empowered by AI assistants. 

[Cain (2023)](https://link.springer.com/article/10.1007/s11528-023-00896-0){target=_blank} explores ways in which prompt engineering can be brought into the classroom and "transition [students] from passive recipients to active co-creators of their learning experiences."


??? Tip "Pro vs Cons of AI in Economics Classrooms"

    At the 2024 EconEd conference Professor Justin Wolfers examined how AI is revolutionizing economics education by enhancing student learning and easing educators' workloads. In response, Professor Jon Meer discussed how educators are navigating AI integration in the classroom. Meer’s session provides a practical and valuable roadmap for effective implementation.

    [https://www.macmillanlearning.com/college/us/events/econed](https://www.macmillanlearning.com/college/us/events/econed){target=_blank} 

    Justin's Pros presentation: [https://www.youtube.com/watch?v=sTeOLgMN4UM](https://www.youtube.com/watch?v=sTeOLgMN4UM){target=_blank}

    <iframe width="560" height="315" src="https://www.youtube.com/embed/sTeOLgMN4UM?si=wuVujujwUz57-Vnv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

    Jon's Cons presentation: [https://www.youtube.com/watch?v=NXbEvLd1vVk](https://www.youtube.com/watch?v=NXbEvLd1vVk){target=_blank}

    <iframe width="560" height="315" src="https://www.youtube.com/embed/NXbEvLd1vVk?si=kfkw-Jpg-LQP7swq" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## AI-Augmented Course Design

Effective integration of AI into teaching begins with intentional course design. AI can support every stage of the backward design process, from defining learning objectives to creating assessments and learning activities.

### Backward Design with AI Assistance

Using AI tools to support the backward design process:

**1. Define Learning Objectives**

AI can help generate, refine, and align learning objectives with Bloom's Taxonomy:

```
Prompt: I'm designing a course on [topic] for [level] students. Help me create
5-7 measurable learning objectives at the analysis and synthesis levels of
Bloom's Taxonomy. The course should prepare students to [intended outcomes].
```

**2. Plan Assessments**

AI assists in designing assessments that measure learning objectives:

```
Prompt: Based on these learning objectives: [paste objectives], suggest 3
different assessment methods that would effectively measure student achievement.
For each method, explain how it addresses specific objectives and provide one
detailed example.
```

**3. Design Learning Activities**

AI helps create scaffolded learning activities aligned with objectives and assessments:

```
Prompt: Given these learning objectives [paste] and this final assessment [describe],
design a sequence of 4-5 learning activities that would prepare students for success.
Include active learning strategies and opportunities for formative feedback.
```

!!! Tip "Curriculum Mapping with AI"

    **Use AI to check curriculum alignment:**

    * Upload your syllabus and ask AI to identify gaps between objectives, activities, and assessments
    * Request suggestions for better scaffolding or pacing
    * Generate visual curriculum maps showing how topics build across the semester
    * Identify prerequisite knowledge that may need review

    **Example Prompt:**
    ```
    Analyze this syllabus for alignment between learning objectives, weekly topics,
    and assessments. Identify any gaps or misalignments and suggest improvements.
    ```

### Syllabus AI Policies (2026 Best Practices)

One of the most critical decisions faculty face is how to address AI use in the syllabus. Research shows that clear, explicit policies reduce confusion and academic integrity violations [(Ithaka S+R, 2025)](https://sr.ithaka.org){target=_blank}.

Consider these approaches along a spectrum from prohibited to encouraged:

=== "Prohibited Approach"

    **When to use:** High-stakes writing courses, foundational skill development, or when authentic individual work is essential for learning.

    **Sample Syllabus Language:**

    *AI Policy: Prohibited Use*

    "In this course, all work must be your own, completed without the assistance of AI tools such as ChatGPT, Claude, Gemini, or similar technologies. Using AI to generate, edit, or substantially assist with any assignment constitutes a violation of academic integrity and will be treated as plagiarism under the [University Code of Academic Integrity](https://deanofstudents.arizona.edu/policies/code-academic-integrity){target=_blank}.

    **Rationale:** This course focuses on developing your individual writing and critical thinking skills. Using AI shortcuts this development and prevents you from building essential capabilities.

    **If you're unsure:** Ask before submitting. It's always better to clarify than to face integrity consequences."

=== "Regulated Approach"

    **When to use:** Most courses where some AI use is acceptable but needs boundaries and disclosure.

    **Sample Syllabus Language:**

    *AI Policy: Regulated Use with Disclosure*

    "AI tools like ChatGPT, Claude, and Gemini can be valuable learning aids when used appropriately. In this course:

    **Permitted Uses:**

    * Brainstorming and generating ideas
    * Grammar and clarity checking
    * Explaining concepts you've encountered in readings
    * Generating practice problems for self-study
    * Creating study guides and summaries

    **Prohibited Uses:**

    * Writing any portion of assignments submitted for credit
    * Completing problem sets or lab work
    * Taking quizzes or exams
    * Generating citations or conducting literature searches (you must verify all sources)

    **Disclosure Requirement:**

    All assignments must include an "AI Use Statement" describing any AI tools used and how. Example: *"I used ChatGPT to check grammar and clarity on my final draft."*

    Failure to disclose AI use is an academic integrity violation."

=== "Encouraged Approach"

    **When to use:** Professional programs, advanced courses, or when AI collaboration skills are learning objectives.

    **Sample Syllabus Language:**

    *AI Policy: Encouraged Use with Documentation*

    "In this course, you are **required** to use AI tools as part of your professional skill development. However, you must use them thoughtfully and document your process.

    **Learning Objectives:**

    * Develop effective prompt engineering skills
    * Learn to critically evaluate AI output
    * Understand when AI is helpful vs. when human expertise is essential
    * Practice ethical AI collaboration

    **Requirements:**

    1. **Document Your Process:** For each major assignment, submit a "Process Log" showing:
       - Prompts you used
       - AI responses you received
       - How you evaluated, modified, or rejected AI suggestions
       - Your final decisions and why you made them

    2. **Demonstrate Learning:** Your grade is based on your critical engagement with AI, not just the final product. Show me your thinking.

    3. **Cite AI Appropriately:** Use this format: *"Initial draft developed in collaboration with Claude 4.5 (Anthropic, 2026). See appendix for interaction log."*

    **This approach treats AI as a professional tool you must learn to use effectively, not as a shortcut.**"

!!! Warning "Key Elements for Any Policy"

    Regardless of approach, your policy should include:

    * **Clear boundaries** - Specific examples of what is/isn't allowed
    * **Rationale** - Help students understand *why* the policy exists
    * **Disclosure requirements** - How students should document AI use
    * **Consequences** - What happens if policy is violated
    * **Support resources** - Where students can get help or ask questions

    Update your policy at the start of each term as AI capabilities and norms evolve.

### Learning Objective Generation

AI excels at helping faculty articulate clear, measurable learning objectives:

??? Question "How can AI help write better learning objectives?"

    **Technique 1: Bloom's Taxonomy Alignment**
    ```
    I want students to understand [concept]. Generate 3 learning objectives at the
    'apply' level and 3 at the 'evaluate' level using Bloom's Taxonomy. Make them
    measurable and appropriate for undergraduate juniors.
    ```

    **Technique 2: Discipline-Specific Objectives**
    ```
    I'm teaching [course name] in [discipline]. What are the core competencies students
    should develop? Frame these as measurable learning objectives using action verbs.
    ```

    **Technique 3: SMART Objectives**
    ```
    Refine these draft learning objectives to be SMART (Specific, Measurable, Achievable,
    Relevant, Time-bound): [paste your draft objectives]
    ```

## Automated Grading and Feedback

AI-powered grading tools are advancing rapidly, offering faculty ways to provide more timely, detailed feedback while managing workload. However, human oversight remains essential to ensure fairness and catch AI limitations.

### Tools and Platforms

| Tool | Primary Use | Features | LMS Integration | Pricing | Best For |
|------|-------------|----------|-----------------|---------|----------|
| **[Gradescope AI](https://www.gradescope.com/){target=_blank}** | Coding & written assignments | AI-assisted rubric creation, pattern recognition, similarity detection | Canvas, Blackboard, Moodle | Institutional licensing | Computer science, STEM courses |
| **[Magic School AI](https://www.magicschool.ai/){target=_blank}** | K-12 & general education | Assignment generation, feedback, report card comments | Limited | $99/year individual | K-12 and general ed courses |
| **[Education Copilot](https://educationcopilot.com/){target=_blank}** | Lesson plans & materials | Automated lesson planning, handout generation, AI chat for students | None (standalone) | Free tier, $9-15/mo pro | Course material creation |
| **[Grammarly for Education](https://www.grammarly.com/edu){target=_blank}** | Writing feedback | Grammar, clarity, tone, plagiarism | Google Classroom, Canvas | Institutional licensing | Writing-intensive courses |
| **[Turnitin Feedback Studio](https://www.turnitin.com/products/feedback-studio/){target=_blank}** | Writing with AI detection | Automated feedback, originality checking, AI detection | Canvas, Blackboard, Moodle, D2L | Institutional licensing | Writing courses across disciplines |

!!! Warning "FERPA Compliance for Grading Tools"

    When using AI grading tools:

    * Verify the vendor has signed a FERPA agreement with your institution
    * Understand where student data is stored and how it's used
    * Never upload student identifying information to consumer AI tools
    * Use anonymous student IDs when possible
    * Review your institution's approved vendor list before adopting tools

### When to Automate (and When Not To)

**Good Candidates for AI-Assisted Grading:**

* Large enrollment courses with standardized rubrics
* Multiple-choice or short-answer questions with clear correct answers
* Code assignments where output can be objectively tested
* Grammar and mechanics in writing (not argument quality or originality)
* Initial screening of submissions before human review

**Keep Human Grading For:**

* Nuanced argumentation and critical analysis
* Creative work where originality and voice matter
* Complex problem-solving with multiple valid approaches
* Work from students with disabilities or accommodations
* High-stakes assessments affecting grades significantly

**Hybrid Approach (Best Practice):**

1. AI provides initial feedback and suggested scoring
2. Instructor reviews AI assessment for accuracy and fairness
3. Instructor adds personalized comments and adjusts scores
4. Students receive both automated and human feedback

??? Tip "Effective Automated Feedback Strategies"

    **Formative, Not Just Summative:**

    * Use AI feedback on drafts before final submission
    * Let students revise based on AI suggestions (and explain what they changed)
    * Track improvement over multiple submissions

    **Transparent with Students:**

    * Tell students when AI is being used for grading
    * Explain the human review process
    * Offer appeal mechanisms for AI-assigned grades

    **Iterative Improvement:**

    * Review AI feedback for patterns of errors or bias
    * Adjust rubrics and training data based on mismatches
    * Share concerning patterns with tool vendors

## Classroom Management with AI

### AI Teaching Assistants

Virtual teaching assistants powered by AI can handle routine student questions, freeing instructors for higher-level support:

**Implementation Models:**

* **Q&A Chatbot:** Answer common questions about syllabus, due dates, policies 24/7
* **Content Explainer:** Provide clarifications on course concepts with links to resources
* **Assignment Guide:** Walk students through assignment requirements and submission process
* **Office Hours Support:** Pre-answer common questions so office hours focus on complex issues

**Example Tools:**

* **Custom GPTs** (ChatGPT Team/Enterprise): Create a bot with your syllabus, policies, and FAQs
* **Claude Projects**: Upload course materials for students to query (if institutionally licensed)
* **Course-specific chatbots**: Khanmigo, Ivy.ai, AdmitHub (check institutional partnerships)

!!! Danger "Teaching Assistant Limitations"

    **What AI TAs Cannot Do:**

    * Provide medical or crisis counseling (always direct to professional services)
    * Make exceptions to policies or grant extensions (instructor decision)
    * Access or discuss individual student grades (FERPA violation)
    * Substitute for meaningful instructor-student relationships

    Always include a disclaimer: *"I'm an AI assistant for [Course Name]. For complex questions, accommodations, or personal matters, please contact Prof. [Name] directly."*

### Discussion Facilitation

AI can enhance online and hybrid discussions:

* **Seed Questions:** Generate discussion prompts that encourage critical thinking
* **Summarization:** AI synthesizes long discussion threads for students joining late
* **Participation Analytics:** Identify students not participating and suggest engagement strategies
* **Debate Preparation:** Students practice arguments with AI before peer discussion

### Real-Time Engagement Tools

**Live Polling and Q&A (AI-Enhanced):**

* **Mentimeter AI:** Generates word clouds and summarizes open responses
* **Slido:** AI-powered Q&A moderation and question clustering
* **Poll Everywhere:** Real-time sentiment analysis of student responses

**Use Cases:**

* Gauge understanding during lectures (concept checks)
* Identify confusing points requiring clarification
* Crowdsource questions for Q&A sessions
* Generate discussion topics from student input

## Multimodal Teaching Materials

AI enables faculty to create diverse teaching materials without specialized technical skills.

### Video Generation

**AI Video Tools:**

* **Synthesia:** Create video lectures with AI avatars (text-to-video)
* **HeyGen:** Generate personalized video content with your digital likeness
* **Descript:** AI-powered video editing, transcription, and overdubbing
* **Lumen5:** Transform text content into engaging video presentations

**Educational Use Cases:**

* Pre-recorded "micro-lectures" for flipped classroom models
* Multilingual course content (AI translation + dubbed videos)
* Accessible video content with automatic captions and translations
* Personalized video feedback on assignments

!!! Tip "Video Generation Best Practices"

    **Quality Control:**

    * Always review AI-generated videos for accuracy before sharing
    * Watch for unnatural speech patterns or lip-sync issues
    * Test videos with students and gather feedback

    **Accessibility:**

    * Use AI to generate accurate captions and transcripts
    * Provide text alternatives for all video content
    * Ensure color contrast and visual accessibility

    **Authenticity:**

    * Consider whether AI avatar video feels authentic for your teaching style
    * Some students may prefer genuine instructor presence
    * Use AI video strategically, not as complete replacement

### Interactive Simulations

**AI-Powered Interactive Learning:**

* **Claude Artifacts:** Create interactive visualizations, simulations, and tools directly in conversation
* **ChatGPT Canvas:** Collaborative space for building and refining educational content
* **Custom Web Apps:** Use AI to generate interactive HTML/JavaScript tools for demonstrations

**Examples:**

* Interactive graphs showing economic concepts
* Scientific simulations (physics, chemistry)
* Data visualization tools students can manipulate
* Choose-your-own-adventure scenarios for case studies

### Educational Image Generation

**AI Image Tools:**

* **DALL-E 3 (via ChatGPT Plus):** Generate custom diagrams, illustrations, examples
* **Midjourney:** High-quality artistic images for presentations
* **Adobe Firefly:** Commercial-safe AI images integrated with Adobe tools
* **Stable Diffusion:** Open-source image generation (requires technical setup)

**Use Cases:**

* Create custom diagrams and infographics
* Generate historical scene reconstructions
* Visualize abstract concepts
* Develop test questions with novel images

!!! Warning "Copyright and AI-Generated Images"

    * AI-generated images may have unclear copyright status
    * Some tools train on copyrighted work (ethical concerns)
    * Attribution practices are still evolving
    * Check institutional policies before using AI images in published materials
    * For commercial textbooks or MOOCs, consult legal counsel

## Security and FERPA Considerations for GPTs in Higher Education

The integration of GPTs into classrooms introduces challenges, particularly in terms of data security and compliance with the Family Educational Rights and Privacy Act (FERPA). 

This section outlines key considerations for educators and administrators.

!!! Danger "FERPA and GDPR Protections"

    **FERPA (United States):**

    FERPA protects the privacy of student education records. It gives parents certain rights regarding their children's education records. These rights transfer to the student at 18 years of age or beyond the high school level.

    * **Education Records:** Includes files, documents, or other materials that contain information directly related to a student and are maintained by an agency or institution of education.
    * **Directory Information:** Information contained in an education record that would not generally be considered harmful or an invasion of privacy if disclosed.
    * **Rights Under FERPA:** Parents and eligible students have the right to inspect and review the student's education records, request the amendment of records they believe are inaccurate or misleading, and have some control over disclosing personally identifiable information from education records.

    **GDPR (European Union & International Students):**

    If your institution enrolls international students from the EU, GDPR may apply:

    * **Stricter consent requirements** - Explicit opt-in consent needed for data processing
    * **Right to erasure** - Students can request deletion of their data ("right to be forgotten")
    * **Data portability** - Students can request their data in machine-readable format
    * **Breach notification** - Stricter timelines (72 hours) for reporting data breaches
    * **Cross-border transfers** - Additional safeguards for data transferred outside EU

    Many AI platforms (especially those based in US or non-EU countries) may not be GDPR-compliant by default. Consult your institutional data privacy office before using AI tools with international student data.

## Generative AI and Compliance with FERPA and GDPR
    
Commercial GPTs, such as those used for creating educational content, chatbots, or data analysis tools, can potentially handle personal or sensitive information. 

**Faculty members must ensure that using these technologies complies with FERPA regulations before using them in the classroom.**

FERPA mandates the protection of student education records. 

Before using GPTs in educational settings, remember:

- Do not use student education records with Commercial or external AI tools, unless the data falls under directory information, and even then make certain you are compliant with university policy.
- When using student data, implement data minimization which anonymizes student information to avoid release of personally identifiable information (PII).
- Be extremely cautious when inputting student data into GPTs, as this can lead to unintended data leaks or exposure of PII.

### Identifying and Securing Student Data

To ensure FERPA compliance:

- Consult with your university's information technology and information security unit before using an AI software. Ensure that you only use secure, vetted, platforms that are approved by your university.  
- Do not use 3rd party software (plugins or extensions) to analyze or prompt with student data.

## Security Risks and Mitigation Strategies

### Data Leakage and Exposure

- Avoid copying sensitive emails, video/audio transcripts, or student information into GPT platforms for summarization or analysis.
- Educate all staff and teaching assistants on the risks of sharing personal or confidential information with AI systems.

### Academic Integrity

- [Develop clear policies](https://libguides.library.arizona.edu/students-chatgpt/integrity){target=_blank} on the appropriate use of AI tools for all assignments and exams. The existing [Code of Academic Integrity](https://deanofstudents.arizona.edu/policies/code-academic-integrity){target=_blank} already explains how to deal with cases of plagiarism.
- **Note on AI Detection Tools:** Research shows AI detection tools are unreliable, producing false positives that disproportionately affect non-native English speakers [(Liang et al., 2023)](https://doi.org/10.1016/j.patter.2023.100779){target=_blank}; [(Weber-Wulff et al., 2024)](https://doi.org/10.1007/s40979-023-00146-z){target=_blank}. Rather than relying on detection, consider process-based assessment and AI-transparent assignments. See [Plagiarism & AI Detection](plagiarism.md) for comprehensive discussion of detection tools, their limitations, and alternative assessment approaches.

### Technical Security Measures

- Implement zero-trust security solutions, such as secure web gateways, to control access to GPT tools.
- Use URL and content filtering to prevent unauthorized data uploads and limit access to AI platforms.

### Ethical Considerations

- Address potential equity issues arising from unequal access to AI tools among students.
- Consider the impact of AI on critical thinking skills and social interactions in the learning environment.


## Guiding Graduate Students and Postdoctoral Researchers in AI Usage

Training the next generation of researchers to use AI effectively and ethically is a crucial aspect of graduate mentorship. By 2026, AI has become an integral part of the research workflow for most graduate students, and advisors play a critical role in shaping how students engage with these powerful tools.

### Balancing AI Assistance with Independent Learning

Platforms like ChatGPT and Claude are available 24/7 to address virtually any question or problem, offering unprecedented support for graduate student research. However, it is essential to strike a balance between AI assistance and the development of independent critical thinking and research skills.

To achieve this balance, advisors should:

**Encourage AI Literacy:**

* Provide students with resources to understand AI capabilities and limitations
* Discuss how AI tools work, including training data biases and hallucination risks
* Share discipline-specific guidance on appropriate AI use in your field

**Teach Responsible AI Usage:**

* Emphasize using AI as a tool to support research, not replace critical thinking
* Model appropriate AI use in your own research and writing
* Demonstrate prompt engineering techniques for research applications

**Discuss Ethical Considerations:**

* Foster open discussions about ethical implications of AI in research
* Address issues of bias, fairness, transparency, and accountability
* Discuss authorship and attribution for AI-assisted work
* Review journal and publisher policies on AI use

**Promote Thoughtful Collaboration:**

* Encourage students to leverage AI strengths while developing their own expertise
* Teach students to verify AI outputs against primary sources
* Help students recognize when human expertise is essential vs. when AI can assist

**Stay Updated:**

* Ensure both advisors and students stay informed about evolving AI capabilities
* Share best practices and potential pitfalls as they emerge
* Participate in discussions about AI in your disciplinary organizations

### Dissertation and Thesis Support

AI can significantly accelerate dissertation progress when used appropriately:

**Literature Review Augmentation:**

* **Initial exploration:** Use AI to identify key themes, methodological approaches, and research gaps in a body of literature
* **Source organization:** AI can help categorize and synthesize findings from dozens of papers
* **Gap identification:** Ask AI to analyze your literature review and suggest underexplored areas
* **Synthesis assistance:** Generate initial frameworks for organizing complex literature

**Example Prompt for Literature Review:**
```
I'm conducting a literature review on [topic] with focus on [specific aspect].
I've read these 20 papers [provide titles or upload PDFs]. Help me:
1. Identify the main theoretical frameworks used
2. Summarize methodological approaches
3. Highlight areas of consensus and debate
4. Suggest potential research gaps

I'll verify your analysis against the original sources.
```

**Research Proposal Development:**

* Brainstorm research questions and hypotheses
* Generate alternative methodological approaches
* Draft sections of proposals (with significant human revision)
* Create project timelines and milestones
* Identify potential funding sources and grant opportunities

**Data Analysis Support:**

* Generate code for statistical analyses or data visualization
* Troubleshoot analysis problems
* Interpret statistical outputs (with advisor verification)
* Draft methods sections based on analysis steps taken

**Writing and Revision:**

* Improve clarity and academic tone
* Generate alternative ways to frame arguments
* Create outlines for dissertation chapters
* Identify logical gaps or weak transitions
* Assist with formatting and citation management

!!! Warning "Dissertation AI Use Guidelines"

    **Always Required:**

    * Consult with your advisor about acceptable AI use in your program
    * Disclose all AI assistance in acknowledgments or methodology sections
    * Verify all AI-generated information against primary sources
    * Ensure final work represents your original thinking and contribution

    **Never Acceptable:**

    * Using AI to write dissertation chapters without significant human intellectual contribution
    * Fabricating data, sources, or citations suggested by AI
    * Submitting AI-generated work as original without disclosure
    * Bypassing required research methods or analysis steps

    Many universities now have specific policies on AI use in dissertations. Check your graduate school handbook and discuss with your dissertation committee.

### Training Teaching Assistants for the AI Era

Graduate TAs need guidance on using AI in their teaching responsibilities while maintaining academic integrity:

**TA Training Workshop Topics:**

1. **AI Tools Overview** (1 hour)
   - Capabilities and limitations of current AI tools
   - Hands-on exploration of ChatGPT, Claude, and Gemini
   - Discipline-specific AI applications

2. **Grading with AI** (1.5 hours)
   - When AI-assisted grading is appropriate vs. problematic
   - How to use AI for feedback while maintaining fairness
   - Detecting AI-generated student work (and its limitations)
   - Handling suspected AI misuse

3. **Creating Course Materials** (1 hour)
   - Using AI to generate practice problems, quiz questions, discussion prompts
   - Creating accessible materials with AI assistance
   - Copyright and attribution for AI-generated content

4. **Supporting Students** (1 hour)
   - Teaching students effective AI use for learning
   - Responding to student questions about AI policies
   - Balancing AI assistance with genuine learning

5. **Ethical Considerations** (30 min)
   - FERPA compliance when using AI with student data
   - Bias and fairness in AI tools
   - Maintaining student privacy and trust

**TA Guidelines Document (Template):**

```markdown
# Teaching Assistant Guidelines for AI Use in [Course Name]

## Permitted Uses:

* Generating practice problems or study questions
* Creating answer keys (must verify accuracy)
* Providing feedback on student writing (grammar/clarity only)
* Answering routine student questions about logistics

## Prohibited Uses:

* Grading assignments without instructor review
* Sharing student work or data with consumer AI tools
* Creating exam questions without instructor approval
* Providing students with AI-generated solutions to assignments

## Best Practices:

* Always disclose to students when you've used AI to create course materials
* Document your AI use and share with supervising professor
* When in doubt, ask the instructor before using AI for any teaching task
* Verify accuracy of all AI-generated content before sharing with students

## Reporting Requirements:

* Report any suspected student AI misuse to the instructor (not directly accuse)
* Document situations where AI tools gave problematic or biased responses
* Share creative uses of AI that worked well in teaching
```

### Cross-Institutional Resources

Point graduate students to these research-focused AI resources:

* [Anthropic Claude for Research](https://www.anthropic.com/research){target=_blank}
* [OpenAI Research Portal](https://openai.com/research){target=_blank}
* [Research guidance from major publishers (Elsevier, Springer, etc.)](https://www.springernature.com/gp/policies/artificial-intelligence){target=_blank}
* Your university's graduate school AI guidance
* Discipline-specific professional society statements

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I will no longer approve graduate student dissertation proposals or dissertations unless they used ChatGPT or a similar AI to help them write part of it! (With appropriate acknowledgment). Yes, I am serious! <br><br>We&#39;re training PhDs to think, not to be robots.</p>&mdash; Seth (@DrSethMurray) <a href="https://twitter.com/DrSethMurray/status/1643353489341394945?ref_src=twsrc%5Etfw">April 4, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Teaching with Chatbots

[ChatGPT](https://chat.openai.com/){target=_blank} and [Gemini](https://gemini.google.com/){target=_blank} can improve teaching and learning processes by generating and assessing information and can be used as a standalone tool or  integrated into other systems. It can perform simple or technical tasks and examples show how it can augment teaching and learning.

[Gemini LearnLM](https://ai.google.dev/gemini-api/docs/learnlm){target=_blank} is available in [Google's AI Studio](https://aistudio.google.com/app/prompts/new_chat){target=_blank} and has advanced features for teaching or tutoring.

**Table: Potential role playing examples for chatbots for teaching and tutoring**

| Role playing | Description | Example of implementation |
| :-- | :-- | :-- |
| **Possibility engine** | AI can suggest alternative ways to express an idea | Students can write queries in ChatGPT/Gemini and use the "Regenerate" response function to explore alternative responses. |
| **Socratic opponent** | AI can act as an opponent to develop an argument | Students can enter prompts into ChatGPT/Gemini, using the  structure of a conversation or debate. Teachers can ask their students  to use ChatGPT/Gemini to prepare for discussions. |
| **Collaboration coach** | AI helps groups to research and solve problems together | When completing tasks and assignments, students can use ChatGPT/Gemini to find information while working in groups. | 
| **Guide on the side** | AI acts as a guide to navigating physical and conceptual spaces | Teachers use ChatGPT/Gemini to generate content for their  classes or courses, such as discussion questions, and to seek advice on  how to support students in learning specific concepts. |
| **Personal tutor** | AI tutors each student and gives immediate feedback on progress | ChatGPT/Gemini provides personalized feedback to students based on information provided by students or teachers (e.g., test scores). |
| **Co-designer** | AI assists throughout the design process | Teachers can seek ideas from ChatGPT/Gemini for designing or  updating a curriculum, including rubrics for assessment. Alternatively,  they can focus on specific goals, such as making the curriculum more  accessible. ChatGPT can provide recommendations and suggestions to help  achieve these objectives. |
| **Exploratorium**  | AI provides tools to play with, explore, and interpret data | Teachers provide basic information to students who  write different queries in ChatGPT to find out more. ChatGPT/Gemini can be used  to support language learning. |
| **Study buddy** | AI helps the student reflect on learning material | Students explain their current level of understanding  to ChatGPT/Gemini and ask for ways to help them study the material. ChatGPT/Gemini  could also be used to help students prepare for other tasks (e.g., job  interviews). |
| **Motivator** | AI offers games and challenges to extend learning | Teachers or students ask ChatGPT/Gemini for ideas about how to  extend students' learning after providing a summary of the current  level of knowledge (e.g., quizzes, exercises). |
| **Dynamic assessment** | AI provides educators with a profile of each student's current knowledge | Students engage in a tutorial-style dialogue with  ChatGPT/Gemini, and then request that ChatGPT/Gemini create a summary of their current  knowledge for sharing with their teacher or for assessment purposes. |
| **Assessment Designer** | AI creates rubrics, test questions, and alternative assessments aligned with learning objectives | Teachers provide learning objectives and assessment criteria, and AI generates draft rubrics, exam questions, or project guidelines. Instructors refine and customize these to fit their course needs. |
| **Accessibility Advocate** | AI generates accommodations, alt-text, transcripts, and accessible materials | Teachers upload course materials and request AI-generated captions for videos, alt-text for images, simplified versions for different reading levels, or translated content for multilingual learners. |

***

## More Resources on AI at University of Arizona

[University of Arizona Artificial Intelligence](https://artificialintelligence.arizona.edu/){target=_blank} 

[University of Arizona Library Student Guide to AI](https://libguides.library.arizona.edu/students-chatgpt/){target=_blank} 

[University of Arizona Data Lab AI Workshop Series](https://datascience.arizona.edu/education/uarizona-data-lab){target=_blank} 


!!! Tip ":simple-google: Google for Education"

    Google offers self-paced courses on generative AI. 
    
    Register with your @arizona.edu Google account and enroll in this 2-hour workshop: 
    [:simple-google: Generative AI For Educators](https://skillshop.exceedlms.com/student/path/1176018-generative-ai-for-educators){target=_blank} 

!!! Info "Teaching with ChatGPT"

    [ChatGPT for Teachers by We Are Teachers](https://www.weareteachers.com/chatgpt-for-teachers/){target=_blank}

    [Using AI in the Classroom by University of Wisconsin Madison](https://idc.ls.wisc.edu/guides/using-artificial-intelligence-in-the-classroom/){target=_blank}

    [ChatGPT Resources for Faculty by University of Pittsburg](https://teaching.pitt.edu/resources/chatgpt-resources-for-faculty/){target=_blank}

    [AI in the Classroom by Greylock Podcast](https://greylock.com/greymatter/ai-in-the-classroom/){target=_blank}

    [How to handle AI in Schools by CommonSense.org](https://www.commonsense.org/education/articles/chatgpt-and-beyond-how-to-handle-ai-in-schools){target=_blank}


## References

* [ChatGPT Cheat Sheet](https://www.kdnuggets.com/publications/sheets/ChatGPT_Cheatsheet_Costa.pdf). Neural Magic.
* [ChatGPT Cheat Sheet](https://maxrascher.gumroad.com/l/free-chatgpt-guide). Max Rascher.
* [ChatGPT for Studying: How to use the AI-powered chatbot to learn anything you want](https://www.studysmarter.co.uk/magazine/chatgpt-for-studying/). StudySmarter.
* [Learn Prompting](https://learnprompting.org/docs/intro). 
* [Prompt Engineering Guide](https://www.promptingguide.ai/).
* [The Prompt's The Thing: An Essential Guide to Google Gemini](https://spyscape.com/article/bing-prompt-guide). Skyscape.
* [100+ Creative ideas to use AI in education](https://docs.google.com/presentation/d/1wVgLWgeEvJm3fznlm0aV8ZiuWsW3o3aUQUCcvuM5vxQ/edit#slide=id.p). Sandra Abegglen, Marianna Karatsiori and Antonio Martinez-Arboleda.
* [200+ Best Gemini AI prompts you can't miss - ChatGPT compatible](https://tipseason.com/Gemini-prompts-for-everyone/). TipSeason.

***

