# :simple-googlegemini: Google Gemini

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## Creating a Gemini account

There are multiple ways to access and use Google Gemini:

**1. Through the Gemini Web Application:**

   *   Visit [gemini.google.com](https://gemini.google.com/){target=_blank}.
   *   Sign in with your Google Account. If you don't have one, create one at [accounts.google.com](https://accounts.google.com/){target=_blank}.
   *   You can start interacting with Gemini through the chat interface. The free tier includes Gemini 2.5 Flash (unlimited) and limited Gemini Pro access.

!!! Info "Gemini Pricing & Comparisons"
    **Subscription Options:**

    - **Free:** Gemini 2.5 Flash unlimited
    - **AI Pro ($19.99/mo):** Gemini 2.5 Pro access, NotebookLM Plus, 2TB storage - **Free for university students (1 year)**
    - **AI Ultra ($249.99/mo):** Gemini 2.5 Pro unlimited, Deep Think, Veo 3 video generation

    **Compare with other AI platforms:** See [Choosing the Right AI Platform](choose.md) for detailed comparisons

**2. Through Google AI Studio (for Developers):**

   *   Go to [aistudio.google.com](https://aistudio.google.com){target=_blank}
   *   Sign in with your Google Account.
   *   There you can access the Gemini API and experiment with different model sizes and parameters. You'll get a certain number of free API calls per month.

**3. Integrated into Google Products:**

   *   Gemini features are gradually rolling out to Google Workspace, Google Search, and other products.
   *   [NotebookLM](https://notebooklm.google.com/){target=_blank} is a document based chat interface that allows you to load your own knowledge base and have chatbot conversations. 

**4. On Android Devices:**

   *   Gemini Nano will be available on select Android devices, enabling on-device AI capabilities.

## Troubleshooting Sign-In Issues

If you encounter issues signing in to your Google Account, follow the steps outlined in Google's [support documentation](https://support.google.com/accounts/answer/7682439){target=_blank}.

## Availability

Google Gemini is continuously expanding its availability in [more countries and languages](https://support.google.com/gemini/answer/14525875){target=_blank}.

For University managed accounts (`netid@arizona.edu`), Gemini access may depend on whether UArizona administrators have enabled it for the Google Workspace.  You can also use Gemini through a personal `name@gmail.com` address.

## What is Gemini?

Gemini is designed to understand and generate text, code, images, audio, and video. 

While Google initially launched Bard as its conversational AI, it has since been rebranded and significantly upgraded as **Gemini**.  The Gemini models are being integrated into various Google products and services, including:

*   [**Google AI Studio:**](https://aistudio.google.com/){target=_blank} A web-based IDE for developers to prototype and build with generative AI models.
*   [**Google Search:**](https://google.com){target=_blank} Enhancing search results with AI-generated summaries and insights.
*   [**Google Workspace:**](https://workspace.google.com/solutions/ai/){target=_blank} AI features to Google Docs, Sheets, Slides, Gmail, and Meet. (Similar to [Microsoft's Copilot](https://copilot.microsoft.com/){target=_blank} integration with Office 365).
*   **Android:** [Gemini Nano](https://deepmind.google/technologies/gemini/nano/){target=_blank} will power on-device AI features in Android devices.

!!! tip "Setting up your Gemini API Key"

    To use the Gemini API in your own applications, you'll need an API key. This key is linked to a Google Cloud project. Here’s how to set one up:

    1.  **Go to the Google Cloud Console:**
        *   Open your web browser and navigate to [console.cloud.google.com](https://console.cloud.google.com/){target=_blank}.
        *   Sign in with your Google Account.

    2.  **Create or Select a Google Cloud Project:**
        *   At the top of the page, click the project selector dropdown menu (it might show an existing project name).
        *   In the "Select a project" window that appears, click **"New Project"**.
        *   Give your project a descriptive name (e.g., `gemini-api-project`) and click **"Create"**.

    3.  **Enable the Gemini API:**
        *   Once your project is created and selected, use the navigation menu (&#9776;) on the left to go to **"APIs & Services"** > **"Enabled APIs & services"**.
        *   Click on **"+ ENABLE APIS AND SERVICES"**.
        *   In the search bar, type `Gemini API` and press Enter.
        *   Select the **"Gemini API"** from the search results (it may also be listed as "Generative Language API").
        *   Click the **"Enable"** button. It might take a few moments to complete.

    4.  **Get Your API Key from Google AI Studio:**
        *   Now, go to [aistudio.google.com](https://aistudio.google.com){target=_blank}.
        *   Click on **"Get API key"** in the top left corner.
        *   A new window will open. Click on **"Create API key in new project"** or select the project you created earlier.
        *   Your new API key will be generated and displayed. **Copy this key and store it securely.** You will need it to make calls to the Gemini API.

    Your API key is now ready to use! Remember to keep it confidential and not expose it in client-side code or public repositories.
