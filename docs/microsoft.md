---
type: Setup Guide
title: Microsoft Copilot
description: >-
  Use Copilot Chat and Microsoft 365 Copilot with a work or school account:
  September 2026 plans, education pricing, and Microsoft Foundry for
  developers.
resource: https://tyson-swetnam.github.io/intro-gpt/microsoft/
tags: [setup, microsoft, pricing]
sources:
  - resource: https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
    title: Microsoft 365 Copilot pricing
  - resource: https://www.microsoft.com/en-us/education/products/copilot-in-education
    title: Microsoft 365 Copilot in education
  - resource: https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/enable-copilot-chat-for-learners
    title: Enable Copilot Chat for learners
  - resource: https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry
    title: What is Microsoft Foundry
  - resource: https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products
    title: Compare all Microsoft 365 products
generated:
  by: human:tswetnam
  at: "2026-09-30T00:00:00Z"
verified:
  - by: human:tswetnam
    at: "2025-01-05T17:51:57-07:00"
status: stable
stale_after: "2027-03-01T00:00:00Z"
---

# :material-microsoft: Microsoft Copilot

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a>.

Microsoft attaches the name "Copilot" to several different products, and which one you get depends on the account you sign in with. This page sorts out which Copilot is which, what each costs as of September 2026, how education accounts get access, and how to sign in with your institutional (work or school) account so that Enterprise Data Protection covers your prompts. For the coding assistant, see the [GitHub Copilot guide](copilot.md) instead.

## Which "Copilot"?

- **Copilot app** ([copilot.microsoft.com](https://copilot.microsoft.com/){target=_blank}) - the free consumer chat app for personal Microsoft accounts. The paid consumer tier **Copilot Pro** has been retired (support ended August 1, 2026); its successor is **Microsoft 365 Premium** ($19.99/mo), which bundles Copilot into the Office apps for individuals.
- **Microsoft 365 Copilot Chat** ([copilot.cloud.microsoft](https://copilot.cloud.microsoft/){target=_blank}) - web chat included at no extra cost with an eligible Microsoft 365 work or school account, covered by [Enterprise Data Protection](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection){target=_blank}. This is where most university users should start.
- **Microsoft 365 Copilot** - a paid per-user add-on that puts Copilot inside Word, Excel, PowerPoint, Outlook, and Teams and lets it draw on your organisation's files, mail, and meetings.
- **GitHub Copilot** - the AI coding assistant for VS Code and other editors, sold separately with its own plans. See the [GitHub Copilot guide](copilot.md).
- **Microsoft Foundry** ([ai.azure.com](https://ai.azure.com){target=_blank}) - the developer platform for building on hosted models, formerly known as Azure AI Studio, Azure AI Foundry, and the Azure OpenAI Service. It serves OpenAI models and, since June 29, 2026, Anthropic's Claude models as generally available.

## Plans and pricing (September 2026)

| Plan | Price | Notes |
|------|-------|-------|
| **Microsoft 365 Copilot Chat** | $0 | Included with an eligible Microsoft 365 work or school plan; Enterprise Data Protection |
| **Microsoft 365 Copilot** (enterprise add-on) | $30/user/mo annual; $31.50 paid monthly | Copilot in Word, Excel, PowerPoint, Outlook, and Teams; requires a qualifying Microsoft 365 plan |
| **Microsoft 365 Copilot Business** (SMB add-on) | $21/user/mo annual; $25.20 paid monthly | $18/user/mo first-year promotion through December 31, 2026; requires a Microsoft 365 Business plan |
| **Business Standard + Copilot** | $23.50/user/mo annual; $28.20 paid monthly | Microsoft 365 Business Standard bundled with Copilot Business |
| **Business Premium + Copilot** | $32/user/mo annual; $38.40 paid monthly | Microsoft 365 Business Premium bundled with Copilot Business |
| **Microsoft 365 Copilot for Education** | **$18/user/mo** | Faculty, staff, and students age 13 and up; licensed by the institution |
| **Microsoft 365 Premium** (consumer) | $19.99/mo | Personal Microsoft accounts; the replacement for Copilot Pro |

These are US list prices from the [Microsoft 365 Copilot pricing page](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing){target=_blank}, the [Copilot in education page](https://www.microsoft.com/en-us/education/products/copilot-in-education){target=_blank}, and the [consumer comparison page](https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products){target=_blank}. Institutional pricing is negotiated, so the figure your campus pays may differ. To compare with other vendors, see [Choosing the Right AI Platform](choose.md).

## Education access

- **Copilot Chat** is included with Microsoft 365 Education (A1, A3, and A5) accounts. Higher-education students and staff have it turned on by default; for K-12 learners aged 13 to 17 it stays off until an administrator enables it, and users under 13 are blocked. Details are in [Enable Copilot Chat for learners](https://learn.microsoft.com/en-us/microsoft-365/education/guide/1-reference/enable-copilot-chat-for-learners){target=_blank}.
- **Microsoft 365 Copilot** (the in-app version) is a per-user licence that your institution buys and assigns; individuals cannot add it to a school account themselves. The academic price is $18/user/mo for faculty, staff, and students 13 and up.
- Whether your account has Copilot Chat only, or a full Microsoft 365 Copilot licence, is decided by your institution; check with your campus IT rather than assuming either. UNM users: see [CARC](https://carc.unm.edu/){target=_blank}.

## Sign in with your institutional account

1. Sign in to Microsoft 365 in your browser with your institutional (work or school) account, for example through [Outlook on the web](https://outlook.office.com/mail/){target=_blank} or [microsoft365.com](https://www.microsoft365.com/){target=_blank}.
2. Open [copilot.cloud.microsoft](https://copilot.cloud.microsoft/){target=_blank}, or open [m365.cloud.microsoft](https://m365.cloud.microsoft){target=_blank} and choose **Copilot** from the app launcher.
3. If prompted, choose **Work or school account**, not a personal Microsoft account.
4. Confirm the green :material-shield-check: shield icon next to your name. It indicates [Enterprise Data Protection](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection){target=_blank}: your prompts and responses are not used to train Microsoft's models and stay inside your organisation's Microsoft 365 tenant.

!!! warning "No shield, no protection"

    If the shield is missing, you are signed in to the consumer Copilot app with a personal account. Sign out and sign back in with your institutional account before entering anything about unpublished research, student records, or other sensitive data.

## Copilot inside Microsoft 365 apps

With a Microsoft 365 Copilot licence assigned to your account, a Copilot button appears in the desktop, web, and mobile versions of the Office apps:

- **Word** - draft, rewrite, and summarise documents, and ask questions about a file's content.
- **Excel** - generate formulas, analyse tables, and create charts from natural-language prompts.
- **PowerPoint** - build a deck from a Word document or an outline, then restyle and summarise slides.
- **Outlook** - summarise long threads, draft replies, and get coaching on tone.
- **Teams** - recap meetings (when transcription is on), surface action items, and answer questions about chats and channels.

Without the licence, the same apps show only the free Copilot Chat side pane, or no Copilot at all, depending on your tenant's settings.

## For developers: Microsoft Foundry

[Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry){target=_blank} is Microsoft's developer platform for calling and deploying hosted models through an Azure subscription. It absorbed Azure AI Studio, Azure AI Foundry, and the Azure OpenAI Service, so older tutorials that use those names are describing the same portal at [ai.azure.com](https://ai.azure.com){target=_blank}. It offers OpenAI models, Anthropic's Claude models (generally available since June 29, 2026), and open-weight models, billed per token to your Azure subscription; check with your campus IT whether an institutional Azure agreement covers that spend. For current per-token rates, see the [API pricing table in Choosing the Right AI Platform](choose.md#api-pricing-for-developers).
