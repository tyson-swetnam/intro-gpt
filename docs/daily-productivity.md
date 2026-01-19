# General Productivity

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

![banner](assets/dailyprod-banner.png){width=1000}

## When to use a GPT

!!! note "About AI Model Names and Capabilities"
    Throughout this document, you'll see references to specific AI models and platforms (ChatGPT, Gemini, Copilot, Claude). Model names, versions, and capabilities evolve frequently as AI technology advances. The examples provided demonstrate general capabilities that may be available across multiple platforms, though specific features and integration options vary by provider and subscription level.

Prompt engineering can significantly enhance your productivity. In particular when Enterprise GPTs are integrated into your Microsoft Office Suite or Google Drive, and have secure access to your documents and data, GPTs can be used to:

*   **Draft Emails and manage inboxes:** Automate the creation of routine emails, summarize long email threads, and even prioritize your inbox based on sender and content.
*   **Meeting Summarization:** Quickly get the gist of meeting transcripts, identify action items, and track decisions made.
*   **Task Prioritization and Planning:** Organize tasks based on urgency and importance, create daily or weekly schedules, and set reminders.
*   **Content Creation and Brainstorming:** Generate ideas for articles, blog posts, social media content, and marketing campaigns.
*   **Language Translation:** Translate documents or conversations in real-time, facilitating communication with international colleagues or clients.
*   **Learning and Skill Development:** Get quick explanations of complex topics, find learning resources, and even practice new skills through simulated scenarios.

In our [:material-run-fast: Code Interpreter](code.md) lesson we discuss how GPTs can be used for:

*   **Code Generation and Debugging:** Write basic code snippets, find and fix bugs in existing code, and understand complex code segments.
*   **Data Analysis and Interpretation:** Summarize datasets, identify trends, and generate reports from raw data.

---

## Meeting Summary

[:simple-zoom: AI Companion](https://www.zoom.com/en/ai-assistant/){target=_blank}, along with other AI-powered meeting summary tools, can significantly boost productivity by automating note-taking and extracting key information from meetings. To effectively use these tools, it's important to understand best practices and institutional policies.

**Getting Started and Optimizing Use**

Begin by ensuring that the AI Companion feature is enabled in your Zoom settings. You can customize settings, such as choosing between brief and detailed summaries or specifying keywords for emphasis. 

Before meetings, set clear agendas to provide context for the AI. 

During the meeting, speak clearly, emphasize important terms, and encourage active participation to enrich the AI's analysis. 

While in a meeting you can ask the AI Companion for a summary or specific details, for example, "Has a decision been made about X?". 

After a meeting ends, Zoom will send an email summary to the host, which can be edited and shared with participants. 

Zoom can also highlight key parts of the meeting recording, or break down the recording into smart chapters.

!!! Danger "**Institutional Policies and Data Security**"

    It's crucial to adhere to institutional policies regarding the use of AI tools in official communications. 

    **Only use approved plug-ins such as Zoom AI Companion.** 

    Third-party software may not comply with the university's data security and privacy requirements. 
    
    Using unapproved third-party AI tools can pose significant risks. 

    Unofficial tools may **Compromise Data Security** -- they may store or process meeting data on external servers without adequate security measures, potentially exposing sensitive information to breaches. 

    **Violate Data Privacy** -- they might not adhere to data privacy regulations or institutional policies regarding the handling of personal and confidential data, such as student FERPA.

    **Lack of Accountability:** The university may have limited recourse or control over third-party vendors in case of data breaches or misuse.

    **Integration Issues:** 3rd party plug-ins may not integrate seamlessly with existing university systems, leading to inefficiencies and compatibility problems.

    Therefore, to maintain data security, privacy, and compliance with institutional policies, it is essential to use only officially sanctioned AI tools and plug-ins provided or approved by the university for official communication. Always consult your institution's IT department or relevant policies for guidance on approved tools and their proper usage.

!!! Example ":fontawesome-brands-openai: ChatGPT integrations"

    ChatGPT Plus and Pro versions offer multiple integrations to enhance productivity:

    - **Cloud Storage:** Microsoft OneDrive and Google Drive integrations allow you to attach documents directly to prompts
    - **Canvas:** A collaborative workspace for writing and coding projects with iterative editing
    - **Memory:** Remembers preferences and context across conversations for personalized assistance
    - **Custom GPTs:** Access specialized GPTs from the GPT Store or create your own for specific workflows
    - **Plugins:** Extend functionality with third-party tools (calendar, web browsing, data analysis, etc.)

    !!! Danger "**Make certain these integrations meet University security requirements**"

        Never submit student information, private conversations (Zoom AI Summaries), or other sensitive information through ChatGPT unless using a University of Arizona Enterprise license.

!!! Example ":material-microsoft: Microsoft Copilot integration in Microsoft Office 365"

    University of Arizona officially uses Microsoft Office Online for office productivity. This includes integration with Microsoft Copilot into Office 365.

    Microsoft Copilot features are available through the [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/){target=_blank} domain and directly within Microsoft 365 applications.

    Access to Copilot features may be controlled by your department or UITS. If you need access, contact your department's system administrator. 

!!! Example ":simple-google: Google Gemini integration in Google Workspaces"

    University of Arizona continues to have access to [Google Workspace](https://workspace.google.com/discover), but may be limited by your department or UITS.

    [Google for Education](https://edu.google.com/intl/ALL_us/) also has integration with Gemini, which needs to be authorized by a system administrator. 

## Chat Use Cases

### Example 1: Personal Planner

Suppose you're using an AI assistant as a personal planner. This prompt involves three tasks: **retrieving calendar data**, **creating an itinerary**, and **arranging tasks based on priority**.

??? example "Planning your day"

    **Prompt:**

    ```
    I need your help planning my day tomorrow.
    First, please list all my scheduled meetings and deadlines from my calendar.
    Then, taking into account 2 hours of break time, could you suggest a time-managed itinerary for me?
    Lastly, based on the priority of the tasks, can you create a task list in the order I should tackle them?
    ```

    **Response:**

    I would be happy to help you plan your day, but I need to clarify something first: I do not currently have access to your calendar or scheduling system.

    **To help you effectively, please share:**
    - Your scheduled meetings and their times
    - Any deadlines you have tomorrow
    - Tasks you need to complete
    - Your preferred working hours (e.g., 8 AM - 6 PM)

    Once you provide this information, I will:

    1. **Organize your schedule** with meetings as fixed anchor points
    2. **Create a time-blocked itinerary** that includes your 2 hours of break time strategically placed (ideally after cognitively demanding tasks and around lunch)
    3. **Prioritize your tasks** using the Eisenhower Matrix approach (urgent/important, important/not urgent, etc.)

    **Alternatively**, if you are using a platform with calendar integration enabled (such as Microsoft Copilot with Outlook, Google Gemini with Google Calendar, or a ChatGPT calendar plugin), you can use this same prompt there for automatic calendar access.

    Would you like to share your schedule details so I can create a personalized plan?

!!! info "Calendar Integration Availability"

    Modern AI assistants offer varying levels of calendar integration. Here's how to enable calendar access for each platform:

    **:material-microsoft: Microsoft Copilot with Microsoft 365**

    - **Requirements:** Enterprise Microsoft 365 account with Copilot access
    - **Setup:** Calendar integration is enabled by default for M365 Copilot users
    - **Access:** Available through [m365.cloud.microsoft](https://m365.cloud.microsoft/){target=_blank} or Copilot in Outlook
    - **Note:** Access may be controlled by your department or UITS administrator

    **:fontawesome-brands-openai: ChatGPT Plus/Pro Calendar Plugins**

    - **Requirements:** ChatGPT Plus or Pro subscription
    - **Setup:**
        1. Open ChatGPT and start a new chat
        2. Click the GPT Store icon or search for calendar plugins
        3. Install "Google Calendar" or "Outlook Calendar" plugin
        4. Authorize the plugin to access your calendar
    - **Limitations:** Plugin availability may change; check the GPT Store for current options

    **:simple-google: Google Gemini with Google Workspace**

    - **Requirements:** Google One AI Premium subscription or Google Workspace account
    - **Setup:** Calendar integration is built-in when signed in with a Google account
    - **Access:** Available at [gemini.google.com](https://gemini.google.com){target=_blank}
    - **Note:** May require system administrator authorization for Google Workspace for Education accounts

    **:simple-claude: Claude Desktop with MCP Calendar Server**

    - **Requirements:** Claude Pro subscription and Claude Desktop app
    - **Setup:**
        1. Install Claude Desktop from [claude.ai/download](https://claude.ai/download){target=_blank}
        2. Configure MCP server in Settings → Developer → Model Context Protocol
        3. Add Google Calendar MCP server (requires API credentials)
        4. See [modelcontextprotocol.io](https://modelcontextprotocol.io){target=_blank} for configuration details
    - **Note:** Requires technical setup; consult MCP documentation

    !!! warning "University Data Security"
        When integrating calendar access with AI assistants:

        - **Only use platforms approved by your institution** for university-related calendars
        - **Never share calendars containing FERPA-protected student information** through non-enterprise AI tools
        - **Review your institution's IT policies** before enabling calendar integrations
        - **Use enterprise/education licenses** rather than personal accounts when available

        For University of Arizona users, consult UITS policies and use officially sanctioned integrations (primarily Microsoft 365 Copilot).


### Example 2: Drafting Emails with AI

Modern email platforms include built-in AI assistants that can help you draft, refine, and improve your emails directly within your email client. This is especially useful for composing professional messages, summarizing information, or adjusting tone.

??? example "Drafting emails with AI assistance"

    === "Microsoft Copilot (Outlook Online - UA Users)"

        **Accessing Copilot in Outlook:**

        University of Arizona users have access to Microsoft Copilot through Office 365 Online.

        1. Go to [outlook.office.com](https://outlook.office.com){target=_blank} and sign in with your UA NetID
        2. Click **"New mail"** to start composing an email
        3. In the compose window, look for the **Copilot icon** (sparkle/star icon) in the toolbar
        4. Click the Copilot icon and select **"Draft with Copilot"**

        **Example: Meeting Recap Email**

        **Copilot Prompt:**

        ```
        Draft an email to my team summarizing today's meeting. Include:
        - New project timeline with July 30th deadline
        - Weekly client status updates rotating among team members
        - Brainstorming session next Wednesday for marketing strategies
        - Reminder to submit expense reports by Friday
        Use a professional but friendly tone.
        ```

        **Copilot Generated Email:**

        **Subject:** Meeting Recap - Action Items and Next Steps

        Hi Team,

        Thank you for your participation in today's productive meeting. Here's a summary of our key decisions and action items:

        **Project Timeline**
        We've finalized our project timeline with a deadline of **July 30th**. Please align your deliverables with this date and flag any potential conflicts early.

        **Client Status Updates**
        Our client has requested weekly status updates. We'll implement a rotating schedule—details on assignments will be shared shortly. Each team member will draft and send updates during their assigned week.

        **Marketing Strategy Session**
        We'll hold a brainstorming session next **Wednesday** to develop new marketing strategies. Please come prepared with ideas to share.

        **Expense Reports**
        Reminder: Submit all expense reports by **end of day Friday**.

        Please reach out if you have questions or need clarification.

        Best regards

        ---

        **Refining with Copilot:**

        After Copilot generates the draft, you can:

        - Click **"Regenerate"** for a different version
        - Click **"Adjust tone"** to make it more formal or casual
        - Click **"Make it shorter"** or **"Make it longer"**
        - Manually edit the text and ask Copilot to **"Improve selected text"**

        !!! tip "Copilot Features in Outlook"
            - **Draft with Copilot:** Generate emails from prompts
            - **Coaching by Copilot:** Get suggestions for tone, clarity, and sentiment
            - **Summarize:** Condense long email threads
            - **Available to:** All UA students, faculty, and staff through Office 365

    === "Google Gmail (Non-UA Users)"

        **Accessing "Help me write" in Gmail:**

        Gmail's AI writing assistant is available to Google Workspace users and some personal Gmail accounts.

        1. Go to [mail.google.com](https://mail.google.com){target=_blank}
        2. Click **"Compose"** to start a new email
        3. Look for the **"Help me write" icon** (sparkle icon with pen) in the compose window
        4. Click the icon to open the AI writing assistant

        **Example: Meeting Recap Email**

        **Gmail Prompt:**

        ```
        Write a professional email to my team summarizing our meeting today:
        - New deadline: July 30th
        - Weekly client updates will rotate among team
        - Marketing brainstorming session next Wednesday
        - Expense reports due this Friday
        ```

        **Gmail Generated Email:**

        Subject: Today's Meeting - Key Takeaways

        Hi team,

        Thanks for a great meeting today. Here are the key points we discussed:

        **New Project Deadline:** We've set a firm deadline of July 30th for project completion. Please ensure all your work aligns with this timeline.

        **Client Updates:** Going forward, we'll provide weekly status updates to the client. We'll rotate responsibility for these updates among the team. More details on the rotation schedule coming soon.

        **Marketing Brainstorm:** We'll meet next Wednesday for a brainstorming session focused on new marketing strategies. Come ready to share your ideas!

        **Expense Reports:** Please submit your expense reports by end of day Friday.

        Let me know if you have any questions.

        Thanks,

        ---

        **Refining with Gmail AI:**

        After Gmail generates the draft, you can:

        - Click **"Recreate"** to generate a new version
        - Click **"Formalize"** to make it more professional
        - Click **"Elaborate"** to add more details
        - Click **"Shorten"** to make it more concise
        - Manually edit and highlight text to ask for specific improvements

        !!! tip "Gmail AI Writing Features"
            - **Help me write:** Generate full email drafts from prompts
            - **Refine my draft:** Improve tone, length, or formality
            - **Available to:** Google Workspace users and select Gmail accounts
            - **Mobile:** Also available in the Gmail mobile app

!!! warning "Best Practices for AI-Drafted Emails"

    - **Always review and edit:** AI-generated emails should be reviewed for accuracy and appropriateness
    - **Verify facts:** Check that all details (dates, names, numbers) are correct
    - **Personalize:** Add personal touches that reflect your voice and relationship with recipients
    - **Sensitive content:** Avoid using AI for highly sensitive, confidential, or legally significant emails
    - **Privacy:** Don't include confidential information in prompts sent to AI services


## Advanced Research Capabilities

Modern AI platforms offer sophisticated research capabilities that go far beyond simple web searches. Four notable approaches are **Extended Thinking** (available in Claude Opus 4.5), **Deep Research** (available in Google Gemini Pro 3.0 and ChatGPT), and **Google Scholar Labs** (an experimental AI-powered academic search tool). Understanding when and how to use these features can dramatically improve your research productivity.

!!! info "What Are Extended Thinking, Deep Research, and Scholar Labs?"

    **Extended Thinking (Claude Opus 4.5)** allows the AI to engage in deeper, more deliberate reasoning before responding. Instead of generating an immediate answer, Claude "thinks through" complex problems step-by-step, similar to how a researcher might work through a difficult problem on a whiteboard before presenting conclusions.

    **Deep Research (Google Gemini Pro 3.0 and ChatGPT)** is an agentic research mode where the AI autonomously searches the web, reads multiple sources, synthesizes information, and produces comprehensive research reports. Both platforms can spend several minutes gathering and analyzing information before delivering results:

    - **Gemini Deep Research:** Produces longer, more formal research reports (~3,500+ words) with extensive sources including news, policy, and academic literature
    - **ChatGPT Deep Research:** Produces concise academic syntheses (~1,000 words) with focus on consensus findings and numerical data from peer-reviewed sources

    **Google Scholar Labs** is an experimental AI-powered search assistant specifically designed for academic research. Unlike traditional keyword-based search, it analyzes complex research questions, identifies key relationships, and surfaces papers based on how well they answer your overall question rather than simple keyword matches.

    All these approaches are designed for tasks that benefit from sustained, careful analysis rather than quick responses.

#### Extended Thinking with Claude Opus 4.5

Extended Thinking is particularly valuable when you need the AI to work through complex reasoning, analyze nuanced problems, or consider multiple perspectives before responding. When enabled, Claude shows you its "thinking" process, making its reasoning transparent and verifiable.

**When to use Extended Thinking:**

- Complex analytical problems requiring multi-step reasoning
- Evaluating arguments with competing perspectives
- Technical problem-solving where you need to see the reasoning process
- Research design and methodology questions
- Ethical dilemmas with multiple stakeholder considerations

??? example "Using Extended Thinking for research methodology"

    **Scenario:** You are designing a mixed-methods study on faculty adoption of AI tools in teaching and want Claude to help you think through potential methodological challenges.

    **Prompt:**

    ```
    I'm designing a mixed-methods study to investigate how faculty at research universities
    are integrating generative AI tools into their teaching practices. The study will combine
    surveys with semi-structured interviews.

    Please think carefully about the methodological challenges I might face and how to
    address them. Consider issues of sampling, bias, validity, and the rapidly changing
    nature of AI technology.
    ```

    **Claude's Extended Thinking Process** (visible to you):

    *Let me think through this systematically...*

    *First, sampling challenges: Faculty who respond to surveys about AI might be those already
    interested in technology - this creates self-selection bias. Also, "research universities"
    varies widely - R1 vs R2, public vs private, STEM-heavy vs liberal arts...*

    *The temporal dimension is tricky. AI tools are evolving so rapidly that practices from
    even 6 months ago may be obsolete. Interview data collected in January might not reflect
    practices by the time the study is published...*

    *Validity concerns: Faculty might overreport AI use due to social desirability, or
    underreport due to institutional policies they're uncertain about...*

    **Claude's Response:**

    Your study design faces several interconnected methodological challenges. Here is my analysis with recommendations:

    **1. Sampling and Selection Bias**

    - **Challenge:** Faculty who volunteer for AI-related studies likely skew toward early adopters, creating non-representative samples
    - **Mitigation:** Use stratified sampling across disciplines, rank, and known technology adoption patterns. Consider incentivizing participation from technology-hesitant faculty. Partner with faculty development offices who can facilitate broader recruitment

    **2. Temporal Validity**

    - **Challenge:** The AI landscape evolves monthly. Data collected now may not reflect practices 6-12 months later when you publish
    - **Mitigation:** Explicitly timestamp your data collection period. Frame findings as capturing a specific moment in a trajectory. Consider a longitudinal design with follow-up interviews. Focus on underlying adoption patterns rather than specific tool usage

    **3. Social Desirability and Institutional Climate**

    - **Challenge:** Faculty may underreport AI use if uncertain about institutional policies, or overreport to appear innovative
    - **Mitigation:** Ensure anonymity in surveys. In interviews, normalize both adoption and non-adoption. Include questions about institutional climate and policy clarity. Consider asking about colleague practices (indirect questioning)

    **4. Defining Key Constructs**

    - **Challenge:** "Integration into teaching" could mean anything from using ChatGPT for lecture prep to teaching students prompt engineering
    - **Mitigation:** Develop a clear taxonomy of AI use in teaching. Pilot your definitions with faculty before full deployment. Include behavioral anchors in survey questions

    **5. Mixed-Methods Integration**

    - **Recommendation:** Use an explanatory sequential design - let quantitative findings guide interview protocol development. This allows you to probe unexpected survey results and achieve genuine triangulation

    Would you like me to elaborate on any of these areas or help develop specific survey items?

!!! tip "Enabling Extended Thinking"

    In Claude (claude.ai or Claude Desktop):

    - Extended Thinking is available with Claude Opus 4.5 for Pro subscribers
    - Click the model selector and choose "Claude Opus 4.5"
    - For complex problems, Claude may automatically engage in extended thinking
    - You can encourage deeper reasoning by asking Claude to "think carefully" or "reason through this step-by-step"
    - The thinking process appears in a collapsible section above the response

#### Deep Research with Google Gemini Pro 3.0

Deep Research transforms Gemini into an autonomous research assistant that can spend several minutes (sometimes longer) exploring a topic across the web. Rather than providing an instant response, Gemini creates a research plan, searches multiple sources, reads and analyzes content, and synthesizes findings into a comprehensive report.

**When to use Deep Research:**

- Literature reviews and background research
- Investigating unfamiliar topics where you need comprehensive coverage
- Comparing multiple products, policies, or approaches
- Fact-finding missions requiring multiple authoritative sources
- Preparing for grant proposals or comprehensive reports

#### Google Scholar Labs

Google Scholar Labs represents a new approach to academic literature search by using AI to understand the multidimensional nature of research questions. Rather than treating your query as a simple keyword search, Scholar Labs analyzes your question, identifies key topics and relationships, and surfaces papers based on their relevance to your overall research question.

**When to use Scholar Labs:**

- Literature reviews requiring nuanced understanding of research questions
- Exploring connections between different research areas or methodologies
- Finding papers that address specific aspects of complex research questions
- Discovering relevant work that might not use your exact keywords
- Getting contextual summaries explaining why each paper is relevant

??? example "Using Scholar Labs for a literature review"

    **Scenario:** You're preparing a literature review for your dissertation on the effectiveness of peer-led instruction in undergraduate STEM courses.

    **Research Question:**

    ```
    What evidence exists about the effectiveness of peer-led instruction (also called
    peer-led team learning or PLTL) in improving learning outcomes for underrepresented
    students in undergraduate STEM courses, particularly in gateway courses like
    introductory biology, chemistry, and physics?
    ```

    **What Scholar Labs Does:**

    Instead of searching for papers that simply contain "peer-led instruction" and "underrepresented students," Scholar Labs:

    1. **Analyzes the question** to identify multiple dimensions:
       - Instructional method: peer-led instruction, PLTL, peer learning
       - Population: underrepresented students, diversity in STEM
       - Context: undergraduate, gateway courses, introductory science
       - Outcomes: learning effectiveness, academic performance, retention

    2. **Searches comprehensively** across these dimensions simultaneously

    3. **Surfaces relevant papers** even if they use different terminology (e.g., "supplemental instruction," "peer teaching," "collaborative learning")

    **Example Results:**

    Scholar Labs might return papers with contextual descriptions like:

    - **"Peer-Led Team Learning in General Chemistry: Implementation and Evaluation"** (Wilson & Varma-Nelson, 2016)
      *This paper reports on PLTL effectiveness in a gateway chemistry course and includes disaggregated data showing differential impacts for first-generation college students.*

    - **"Supplemental Instruction and the Performance of Hispanic Students in Developmental Mathematics"** (Peterfreund et al., 2007)
      *While using different terminology ("supplemental instruction"), this paper addresses peer-led learning with a specific focus on Hispanic students in a foundational STEM course.*

    - **"The Role of Near-Peer Mentoring in STEM Persistence for Underrepresented Students"** (Johnson & Stage, 2018)
      *This study examines peer mentorship structures in biology courses, providing insights into mechanisms that make peer-led instruction effective for underrepresented students.*

    **Follow-up Questions:**

    Scholar Labs allows you to ask follow-up questions to narrow or expand your search:

    ```
    Which of these studies include control groups and experimental designs rather than
    observational studies?
    ```

    ```
    Are there any meta-analyses or systematic reviews synthesizing this evidence?
    ```

    ```
    What critiques or limitations have researchers identified about peer-led instruction
    for diverse student populations?
    ```

!!! tip "Accessing Google Scholar Labs"

    Google Scholar Labs is currently experimental (as of January 2026):

    - Visit [https://scholar.google.com/scholar_labs/search](https://scholar.google.com/scholar_labs/search){target=_blank}
    - Requires logging in with a Google account
    - Currently available to limited users; you may need to join a waitlist
    - Currently supports English-language questions only
    - Results retain all familiar Google Scholar features (citations, "cited by," related articles)
    - You can ask follow-up questions to refine your search

!!! warning "Scholar Labs Limitations"

    As an experimental tool, Scholar Labs has some important limitations:

    - **No citation ranking:** Scholar Labs deliberately ignores citation counts and journal prestige, ranking papers solely by relevance to your question. This can surface valuable but less-cited work, but you'll need to evaluate quality yourself
    - **Limited availability:** Not all Google Scholar users have access yet
    - **Experimental status:** Features and behavior may change as Google refines the tool
    - **Verification needed:** Always read the actual papers—AI-generated summaries may mischaracterize findings
    - **Transparency:** Unlike Deep Research, Scholar Labs doesn't show you its search process or all sources considered

#### Comparing the Research Approaches

!!! note "Deep Research Availability"
    Deep Research is available in both **ChatGPT** and **Gemini**. Both produce comprehensive research reports but differ in length and scope:

    - **ChatGPT Deep Research:** Concise synthesis (~1,000 words), strong consensus focus
    - **Gemini Deep Research:** Longer formal reports (~3,500+ words), broader source diversity

| Aspect | Extended Thinking (Claude) | Deep Research (ChatGPT/Gemini) | Scholar Labs (Google) |
|--------|---------------------------|-------------------------------|----------------------|
| **Primary Purpose** | Deep reasoning and analysis | Comprehensive information gathering | Academic literature discovery |
| **Time Investment** | Seconds to minutes | 3-10 minutes | Seconds (instant results) |
| **Information Source** | Claude's training knowledge | Live web searches | Google Scholar database |
| **Best For** | Analytical problems, methodology, logic | Literature reviews, fact-finding, comparisons | Finding peer-reviewed research papers |
| **Output Style** | Reasoned analysis with visible thinking | Research report with citations | Ranked paper list with contextual summaries |
| **Verification** | Check reasoning logic | Check source links | Read actual papers |
| **Word Count** | Varies | 1,000-3,500+ words | N/A (paper list) |

??? example "Real-world comparison: Researching polar ice melt rates"

    To illustrate the differences between these research tools, here's a side-by-side comparison using the same research question across four different platforms: Scholar Labs, ChatGPT Deep Research, Gemini Deep Research, and Claude.

    **Research Question:**

    ```
    Find recent and highly cited peer-reviewed articles from top-ranked journals that
    report the rate of polar ice melt.
    ```

    ---

    ### Google Scholar Labs Results

    **Processing time:** Instant (seconds)
    **Output:** 10 highly cited papers with contextual summaries

    Scholar Labs returned highly relevant papers with citation metrics and contextual summaries explaining why each is relevant to the query:

    **Key papers found:**

    - **Otosaka et al. (2023)** - *Mass balance of the Greenland and Antarctic ice sheets from 1992 to 2020*
      Earth System Science Data · **Cited by 196**
      Mass loss accelerated from 105 Gt/yr (1992-1996) to 372 Gt/yr (2016-2020)

    - **Edwards et al. (2021)** - *Projected land ice contributions to twenty-first-century sea level rise*
      Nature · **Cited by 441**
      Limiting warming to 1.5°C would halve land ice contribution from 25 to 13 cm by 2100

    - **Hanna et al. (2024)** - *Short-and long-term variability of the Antarctic and Greenland ice sheets*
      Nature Reviews Earth & Environment · **Cited by 68**
      Total polar ice loss: -382 ± 42 Gt/year (2002-2022) = 1.1 mm/year SLE

    - **Greene et al. (2024)** - *Ubiquitous acceleration in Greenland Ice Sheet calving from 1985 to 2022*
      Nature · **Cited by 35**
      AI-powered terminus mapping reveals 20% underestimate of Greenland mass loss

    - **Millan et al. (2023)** - *Rapid disintegration and weakening of ice shelves in North Greenland*
      Nature Communications · **Cited by 35**
      North Greenland ice shelves lost 35% of volume since 1978

    **Strengths:**

    - ✓ Instant results (seconds)
    - ✓ Citation counts immediately visible ("Cited by 441")
    - ✓ Contextual summaries explain *why* each paper is relevant
    - ✓ Direct links to PDFs and institutional library access
    - ✓ 100% peer-reviewed academic sources
    - ✓ Clean interface for literature discovery

    ---

    ### Gemini Deep Research Results

    **Processing time:** ~5-15 minutes

    **Output:** Comprehensive research report (~3,500 words)

    [**View Full Gemini Deep Research Report**](https://gemini.google.com/share/a8db263da4d6){target=_blank}

    **Report Structure:**

    - **Executive Abstract:** High-level synthesis of cryospheric state and committed changes
    - **Methodological Convergence:** Detailed explanation of GRACE, altimetry, and input-output methods
    - **Greenland Analysis:** Greene et al. 20% underestimate, 2023 vs 2024 atmospheric variability, firn degradation
    - **Antarctic Analysis:** WAIS committed collapse (van den Akker et al.), Thwaites tipping point, sea ice regime shift
    - **Global Teleconnections:** AMOC impacts, New Zealand climate effects, Southern Hemisphere circulation
    - **Comparative Tables:** Greenland metrics (2023-2025), polar ice sheet dynamics comparison
    - **25+ Citations:** Nature, Science, The Cryosphere, PNAS, plus news and policy sources

    **Strengths:**

    - ✓ Formal research report structure with executive abstract
    - ✓ 25+ sources including academic papers, government reports, and news
    - ✓ Mathematical equations and technical depth
    - ✓ Comparative tables and data synthesis
    - ✓ Broader context (AMOC impacts, teleconnections, New Zealand climate)
    - ✓ Methodological explanations (GRACE vs. altimetry)
    - ✓ Export-ready format for grant proposals

    ---

    ### Claude Results

    **Processing time:** 5-10 minutes (this example took 6 minutes)

    **Output:** Annotated bibliography with 23 papers organized thematically

    [**View Full Claude Annotated Bibliography**](https://claude.site/artifacts/6defa816-ea1e-4628-82c4-1efd48769a0d){target=_blank}

    **Content Organization:**

    - **Greenland Ice Sheet Studies (7 papers):** IMBIE 2020/2023, Greene et al. calving acceleration, Box et al. committed losses, Briner et al. Holocene context
    - **Antarctic Ice Sheet Studies (6 papers):** Smith et al. 2020, Milillo et al. rapid retreat, Naughten et al. unavoidable warming, Schmidt et al. Thwaites robotic observations
    - **Sea Ice Studies (7 papers):** Arctic ice-free projections (Jahn et al.), Antarctic regime shift (Purich & Doddridge), 2023 record lows (Josey et al.)
    - **Sea Level Rise Studies (3 papers):** Edwards et al. projections, Bamber et al. expert elicitation, IMBIE 2018

    **Strengths:**

    - ✓ Most papers found (23 comprehensive sources)
    - ✓ Excellent thematic organization (Greenland → Antarctica → Sea Ice → SLR)
    - ✓ Citation counts + DOIs + impact metrics included
    - ✓ Balanced technical detail with accessibility
    - ✓ 100% peer-reviewed academic sources
    - ✓ Fast comprehensive synthesis

    ---

    ### ChatGPT Deep Research Results

    **Processing time:** ~3 minutes
    
    **Output:** Structured synthesis (~1,000 words) with in-text citations

    [View ChatGPT Deep Research Results](https://chatgpt.com/s/dr_696c2de0ba6881918bcefec2f0c6da8c){target=_blank}

    **Key findings presented:**

    - **Greenland:** 3,900 ± 340 Gt lost (1992-2018), peaking at 345 ± 66 Gt/yr in 2011
    - **Antarctica:** Loss grew six-fold from ~40 Gt/yr (1979-1990) to 252 Gt/yr (2009-2017)
    - **Combined:** Ice loss quadrupled since 1990s, rising from 105 Gt/yr to 372 Gt/yr (2016-2020)
    - **Methods:** IMBIE consortium data fusion of altimetry, gravimetry, and ice-velocity mapping

    **Strengths:**

    - ✓ Clear numerical data presentation with uncertainties
    - ✓ Strong focus on consensus findings (IMBIE consortium)
    - ✓ In-text citations with superscripts
    - ✓ Accessible academic writing style
    - ✓ Methods explained for each study
    - ✓ 10 peer-reviewed sources from Nature, Science, PNAS
    - ✓ Concise synthesis format

    ---

    ### Four-Way Comparison

    | Aspect | Scholar Labs | ChatGPT Deep Research | Gemini Deep Research | Claude |
    |--------|--------------|----------------------|---------------------|---------|
    | **Papers Found** | 10 | 10 | ~15 academic + 10 other | 23 |
    | **Time to Results** | Instant | ~3 minutes | ~5 minutes | Seconds |
    | **Format** | Annotated list | Academic synthesis | Formal research report | Annotated bibliography |
    | **Word Count** | N/A (list) | ~1,000 words | ~3,500 words | N/A (list) |
    | **Source Types** | Academic only | Academic only | Academic + news + reports | Academic only |
    | **Citation Style** | Visible counts | In-text superscripts | Bibliography | With DOIs |
    | **Organization** | Relevance-ranked | By region/topic | Narrative sections | Thematic sections |
    | **Best For** | Finding papers | Consensus data | Grant proposals | Comprehensive review |

    **Papers all four tools found:**

    - ✓ **Otosaka et al. (2023)** - IMBIE mass balance study (1992-2020)
    - ✓ **Greene et al. (2024)** - Greenland calving acceleration (20% underestimate)
    - ✓ **Edwards et al. (2021)** - Land ice projections
    - ✓ **Smith et al. (2020)** - Science, ICESat altimetry

    **Unique contributions by tool:**

    - **Scholar Labs:** Best citation metrics ("Cited by 441"), fastest access to papers, institutional library links
    - **ChatGPT:** Strong IMBIE consortium focus, clear numerical consensus, concise synthesis (~1,000 words)
    - **Gemini:** Most comprehensive coverage, news sources (Guardian), policy reports (NOAA), teleconnection studies, formal report structure (~3,500 words)
    - **Claude:** Most papers (23), sea ice regime shift studies, expert elicitation (Bamber et al.), thematic organization

    ---

    ### Workflow Recommendation

    For a comprehensive research project, use multiple tools strategically:

    **Quick Start (10 minutes total):**

    1. **Scholar Labs** (instant) → Get 10 high-impact papers with citation counts
    2. **Claude** (30 seconds) → Get 23 papers organized thematically
    3. **ChatGPT Deep Research** (3 min) → Get consensus numerical data and IMBIE focus

    **Comprehensive Research (15-20 minutes total):**

    1. **Scholar Labs** (instant) → Identify highest-impact papers with institutional access
    2. **Claude** (30 seconds) → Get broad academic coverage across all aspects
    3. **ChatGPT Deep Research** (3 min) → Get clear consensus findings with uncertainties
    4. **Gemini Deep Research** (5 min) → Get formal report with news, policy, and broader context

    **Result:** 35+ unique sources spanning peer-reviewed literature, policy reports, news coverage, and consensus data—ready for synthesis into grant proposals, literature reviews, or background sections.

    **Best tool for specific needs:**

    - Need papers NOW? → **Scholar Labs**
    - Writing a grant background? → **Gemini Deep Research**
    - Need consensus numbers? → **ChatGPT Deep Research**
    - Comprehensive literature review? → **Claude**

??? example "Choosing the right approach"

    **Use Extended Thinking when:**

    - You have a complex analytical question: *"What are the trade-offs between different approaches to measuring student engagement in online courses?"*
    - You need to work through methodology: *"Help me think through the validity threats to my proposed quasi-experimental design."*
    - You want transparent reasoning: *"Analyze the arguments for and against requiring AI literacy in general education."*

    **Use Deep Research when:**

    - You need current information: *"What are the latest developments in AI-assisted grading tools?"*
    - You want comprehensive coverage: *"Survey the landscape of open educational resources for teaching data science."*
    - You need citations and sources: *"Find recent studies on the effectiveness of flipped classroom approaches in STEM education."*

    **Use Scholar Labs when:**

    - You need peer-reviewed academic literature: *"Find recent research on the rate of polar ice melt from top-ranked journals."*
    - Your research question has multiple dimensions: *"What evidence exists about peer-led instruction effectiveness for underrepresented students in STEM gateway courses?"*
    - You want papers that address your *specific question* rather than just containing keywords: *"How do community colleges support adult learners returning to higher education after career changes?"*
    - You need to explore connections across subfields: *"What interdisciplinary research exists on climate change communication in K-12 education?"*

    **Combine all three when:**

    - Start with **Scholar Labs** to find relevant peer-reviewed literature on your topic
    - Use **Deep Research** to gather broader context, including grey literature, policy documents, and recent developments not yet in academic journals
    - Apply **Extended Thinking** to synthesize findings, identify gaps, and develop your research questions or methodology
    - **Example workflow:** Use Scholar Labs to find studies on AI in peer review → Use Deep Research to survey publisher policies and recent news → Use Extended Thinking to analyze the ethical implications and design interview questions for journal editors

!!! warning "Verification and Critical Evaluation"

    All three research tools are powerful but require critical evaluation:

    - **Extended Thinking:** The reasoning may be flawed even when it appears logical. Verify key claims and check that the reasoning applies to your specific context
    - **Deep Research:** Sources may be misinterpreted or selectively presented. Always click through to original sources for important claims
    - **Scholar Labs:** AI-generated paper summaries may mischaracterize findings. Always read the actual papers, especially methodology and conclusions sections
    - **None replaces expertise:** These tools augment research but cannot substitute for domain knowledge and scholarly judgment
    - **Cite appropriately:** If using AI-generated research in academic work, follow your institution's guidelines for AI disclosure and citation
    - **Verify recency:** Check publication dates—Scholar Labs and Deep Research may surface older work alongside recent studies


