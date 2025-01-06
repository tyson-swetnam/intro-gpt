# General Productivity

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

![banner](assets/dailyprod-banner.png){width=1000}


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

## Utilizing AI Meeting Summary Software: **Zoom AI Companion** 

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

!!! Example ":simple-openai: ChatGPT integrations"

    Plus and Pro versions of ChatGPT have integrations with :material-microsoft-onedrive: Microsoft OneDrive and :material-google-drive: Google Drive which allow you to add documents to Prompts using `4o` or `o1` models. 

    !!! Danger "**Make certain these integrations meet University security requirements**"

        Never submit student information, private conversations (Zoom AI Summaries), or other sensitive information through ChatGPT unless using a University of Arizona Enterprise license.

!!! Example ":material-microsoft: Microsoft Copilot integration in Microsoft Office 365"

    University of Arizona officially uses Microsoft Office Online for office productivity. This includes integration with Microsoft Copilot into Office 365. 

    Microsoft is currently rolling out new features for Copilot through its new [https://m365.cloud.microsoft/](https://m365.cloud.microsoft/){target=_blank} domain.

    Access to these new features may be limited by your department or UITS. If you want access to these features, contact your department's system administrator. 

!!! Example ":simple-google: Google Gemini integration in Google Workspaces"

    University of Arizona continues to have access to [Google Workspace](https://workspace.google.com/discover), but may be limited by your department or UITS.

    [Google for Education](https://edu.google.com/intl/ALL_us/) also has integration with Gemini, which needs to be authorized by a system administrator. 

## Use Cases

### Example 1: Personal Planner

Suppose you're using a GPT as a personal planner. 

_Note: ChatGPT and Copilot lack access to my University Outlook or Google Calendars, but Gemini has access to my personal calender._

This prompt involves three tasks: **retrieving data**, **creating an itinerary**, and **arranging tasks based on priority**.

!!! example "Planning your day" 

    === "Prompt"

        ```
        I need your help planning my day tomorrow.
        First, please list all my scheduled meetings and deadlines from my calendar.
        Then, taking into account 2 hours of break time, could you suggest a time-managed itinerary for me?
        Lastly, based on the priority of the tasks, can you create a task list in the order I should tackle them?
        ```

    === "CoPilot Response"

        I'd be happy to help you plan your day! However, I don't have direct access to your calendar. 
        If you could provide me with the details of your scheduled meetings and deadlines, 
        I can assist you in creating a well-organized itinerary and task list.

        Could you share your schedule for tomorrow?

    === "ChatGPT o1 Response"

        I’m afraid I don’t have direct access to your personal calendar. 
        If you could provide the details of your scheduled meetings and deadlines (for example, what time they start/end, what they’re for, etc.), 
        I can certainly help you organize a time-managed itinerary—ensuring 2 hours of break time—and then create a prioritized task list.

        Please share whatever information you’re comfortable with, and I’ll get started right away.

    === "Gemini Advanced Response"

        You have 4 events next week. I cannot create a time-managed itinerary for you, but you can do it yourself by taking into account 2 hours of break time.

        Here are your events:

        Monday, January 6th

        "Ecology discussion" from 11:00 AM to 12:30 PM

        "CiCompass: Cloud Infrastructure WG Bi-weekly meetings" from 1:00 PM to 2:00 PM

        Tuesday, January 7th

        "ESIIL CI Tribal" from 12:30 PM to 1:30 PM

        Wednesday, January 8th

        "ESIIL Exec Meeting biweekly" from 9:30 AM to 10:30 AM

        Would you like me to help you with anything else?


        Sources and related content


Assuming you have integration with your calendar, you might use the GPT to manage your schedule as follows:

!!! example "Managing Calendar"

    === "Prompt"

        ```
        can you schedule a team meeting for next Tuesday at 3 PM in my calendar? 
        
        Also, set a reminder for me to prepare the meeting agenda by Monday afternoon.
        ```

    === "Copilot Response"

        Does not have access to my calendar -- yet.

    === "ChatGPT o1 Response"

        Does not have access to my calendar -- yet.

    === "Gemini Advanced Response"

        OK, I'm putting this on your calendar for next Tuesday at 3:00 PM and creating a reminder for you to prepare the meeting agenda by Monday afternoon.


### Example 2: Content Creation

**Blog Post Creation**

This prompt includes three tasks: **generating topics**, **creating outlines**, and **writing introduction paragraphs**.

_Note, these are very long responses:_

!!! example "Blog post creation"


    === "Prompt"

        ```
        I'd like to write a blog post about sustainable living.
        First, could you generate a list of five key topics that I should cover?
        Once we have the topics, can you then provide a brief outline for each of them?
        Finally, for each of the outlines, could you come up with an engaging introduction paragraph?
        ```

    === "CoPilot Response"

        
        That sounds like a fantastic idea! Here are five key topics you could cover in your blog post about sustainable living:

        1. **Reducing Waste**
        2. **Energy Efficiency**
        3. **Sustainable Transportation**
        4. **Eco-Friendly Diet**
        5. **Green Home Practices**

        ### Brief Outlines

        #### 1. Reducing Waste
        - **Introduction**: Importance of waste reduction
        - **Body**:
        - Benefits of reducing waste
        - Practical tips for reducing waste at home
        - Recycling and composting
        - Reducing single-use plastics
        - **Conclusion**: Encouragement to adopt waste reduction habits

        #### 2. Energy Efficiency
        - **Introduction**: The role of energy efficiency in sustainability
        - **Body**:
        - Benefits of energy efficiency
        - Tips for improving energy efficiency at home
        - Energy-efficient appliances and technologies
        - Renewable energy sources
        - **Conclusion**: Call to action for adopting energy-efficient practices

        #### 3. Sustainable Transportation
        - **Introduction**: Impact of transportation on the environment
        - **Body**:
        - Benefits of sustainable transportation
        - Different modes of sustainable transportation (e.g., biking, public transit, electric vehicles)
        - Tips for reducing your transportation footprint
        - Policy and infrastructure changes needed
        - **Conclusion**: Encouragement to choose sustainable transportation options

        #### 4. Eco-Friendly Diet
        - **Introduction**: Connection between diet and sustainability
        - **Body**:
        - Benefits of an eco-friendly diet
        - Tips for adopting a plant-based diet
        - Reducing food waste
        - Supporting local and organic food producers
        - **Conclusion**: Motivation to make sustainable food choices

        #### 5. Green Home Practices
        - **Introduction**: Importance of sustainable living spaces
        - **Body**:
        - Benefits of green home practices
        - Tips for creating a green home (e.g., water conservation, sustainable materials)
        - Indoor plants and air quality
        - DIY eco-friendly home projects
        - **Conclusion**: Encouragement to implement green practices at home

        ### Engaging Introduction Paragraphs

        #### 1. Reducing Waste
        In a world where waste is piling up at an alarming rate, taking steps to reduce our waste footprint has never been more crucial. By making small changes in our daily habits, we can significantly impact the environment and pave the way for a cleaner, greener future. Let's explore how we can all contribute to reducing waste and making a difference.

        #### 2. Energy Efficiency
        Energy efficiency is more than just a buzzword; it's a vital component of sustainable living. By optimizing our energy use, we can reduce our carbon footprint, save money, and contribute to a healthier planet. Join me as we delve into practical ways to enhance energy efficiency in our homes and lives.

        #### 3. Sustainable Transportation
        Transportation is a major contributor to greenhouse gas emissions, but it doesn't have to be. Embracing sustainable transportation options can lead to a cleaner environment and a healthier lifestyle. Let's take a journey through the various ways we can make our commutes and travels more eco-friendly.

        #### 4. Eco-Friendly Diet
        What we eat has a profound impact on the planet. Adopting an eco-friendly diet not only benefits our health but also supports the environment. From plant-based meals to reducing food waste, discover how our dietary choices can lead to a more sustainable world.

        #### 5. Green Home Practices
        Our homes are our sanctuaries, and making them sustainable can have a lasting positive impact on the environment. From water conservation to using sustainable materials, there are countless ways to create a green home. Let's explore practical tips and ideas to transform our living spaces into eco-friendly havens.

        I hope these topics, outlines, and introductions help you get started on your blog post! If you need further assistance or more details on any of these points, feel free to ask.

    === "ChatGPT o1 Response"

        Sure! Here’s a structured way we can approach it:

        ---

        ## 1. Energy Efficiency and Renewable Energy

        ### Brief Outline
        1. **Understanding Your Energy Footprint**  
        - Why it matters and how to measure it  
        - Tools for monitoring home energy usage

        2. **Practical Home Efficiency Tips**  
        - Insulation and sealing windows/doors  
        - Energy-efficient appliances and LED lighting

        3. **Transitioning to Renewable Energy**  
        - Solar panel installations and community solar options  
        - Wind energy and other emerging technologies

        4. **Behavioral Changes for Lower Energy Consumption**  
        - Turning off and unplugging electronics  
        - Smart use of heating and cooling systems

        5. **Long-Term Benefits**  
        - Financial savings and return on investment  
        - Positive environmental impact

        ### Introduction Paragraph
        Ever wonder how much power your home truly consumes—and how you could use less without sacrificing comfort? Energy efficiency and renewable energy sources lie at the core of sustainable living. By understanding your energy footprint and making thoughtful improvements—like sealing drafts, installing solar panels, or simply turning off unnecessary electronics—you can lower both your monthly bills and your impact on the planet. This shift toward clean energy isn’t just beneficial for the environment; it can significantly enhance your quality of life in the long run.

        ---

        ## 2. Sustainable Transportation

        ### Brief Outline
        1. **The Impact of Transportation on Carbon Emissions**  
        - Global transport emissions data  
        - How personal choices contribute to the bigger picture

        2. **Alternatives to Driving Alone**  
        - Public transportation, carpooling, and ride-sharing  
        - Tips for planning routes and schedules efficiently

        3. **Embracing Eco-Friendly Modes of Travel**  
        - Biking, walking, and using e-scooters or e-bikes  
        - Benefits for physical health and mental well-being

        4. **Electric and Hybrid Vehicles**  
        - Comparing electric, hybrid, and conventional cars  
        - Factors to consider (range, charging stations, cost)

        5. **Influencing Policy and Community Action**  
        - The role of local governments in promoting green transportation  
        - Community advocacy and infrastructure improvements

        ### Introduction Paragraph
        Getting from A to B is a necessary part of daily life, but how we choose to do it can have a big impact on our planet. Whether it’s taking the bus instead of driving alone, riding a bike to work, or investing in an electric car, there are plenty of ways to keep our carbon footprints in check. In this section, we’ll explore how sustainable transportation choices not only help the environment but also save money and contribute to healthier, happier communities.

        ---

        ## 3. Waste Reduction and Recycling

        ### Brief Outline
        1. **The Global Waste Problem**  
        - Current statistics on waste generation  
        - Consequences of landfills, incineration, and pollution

        2. **Strategies for Reducing Waste at Home**  
        - Embracing reusable items and buying in bulk  
        - DIY or zero-waste swaps (e.g., bamboo toothbrushes, refillable containers)

        3. **Understanding Recycling and Composting**  
        - Sorting household recyclables correctly  
        - Composting organic waste to close the nutrient loop

        4. **Upcycling and Repurposing**  
        - Creative ways to extend the life of everyday products  
        - Inspirations for DIY crafts and home projects

        5. **Community Engagement and Policy**  
        - Supporting local recycling programs  
        - Advocating for better waste management systems

        ### Introduction Paragraph
        Do you ever stop to think about where your trash goes after it leaves the curb? Our world is grappling with staggering amounts of waste, and it’s more important than ever to consider how we can lighten that load. By making small but impactful changes—like switching to reusable products, sorting recyclables properly, and composting food scraps—we can all play a part in cutting down on needless waste. It’s time to transform our throwaway culture into one that values resources, creativity, and the planet’s well-being.

        ---

        ## 4. Ethical and Sustainable Consumption

        ### Brief Outline
        1. **The True Cost of Consumer Goods**  
        - Environmental and social impacts of production  
        - Importance of fair labor practices and supply chain transparency

        2. **Buying Less, Choosing Well**  
        - Minimalism and conscious consumerism  
        - Quality over quantity: investing in durable items

        3. **Supporting Eco-Friendly Brands**  
        - Certifications (e.g., Fair Trade, Rainforest Alliance)  
        - Researching brand values and corporate responsibility

        4. **Secondhand and Thrift Shopping**  
        - Extending product lifespans by purchasing used items  
        - Tips for finding high-quality goods at thrift stores

        5. **The Role of Community in Ethical Consumption**  
        - Sharing, borrowing, and community swap events  
        - Local artisans and farmers’ markets

        ### Introduction Paragraph
        When we swipe our credit cards or add items to our online carts, it’s easy to forget the journey each product took to reach us. From raw materials to human labor, every purchase carries hidden environmental and social costs. By choosing to consume less and shop more ethically—whether it’s supporting fair trade coffee growers or opting for secondhand clothes—we can make a difference that extends far beyond our personal wardrobes or pantries. Let’s explore why mindful consumption is key to a more sustainable future.

        ---

        ## 5. Sustainable Food Choices

        ### Brief Outline
        1. **Understanding Food Systems**  
        - The environmental impact of industrial agriculture  
        - Water use, greenhouse gas emissions, and biodiversity loss

        2. **Eating Locally and Seasonally**  
        - Benefits of buying from local farmers  
        - How to plan meals around seasonal produce

        3. **Plant-Based Diets and Reduced Meat Consumption**  
        - Health and environmental benefits of eating more plants  
        - Tips for transitioning gradually and finding balance

        4. **Food Waste Reduction**  
        - Proper storage and meal planning  
        - Creative recipes using leftovers

        5. **Growing Your Own Food**  
        - Container gardening and community gardens  
        - The satisfaction and health benefits of homegrown produce

        ### Introduction Paragraph
        Have you ever wondered how the food on your plate gets there, or what it takes to produce it? Our dietary choices have significant ripple effects on the health of our bodies, our communities, and our planet. From selecting fresh, locally sourced ingredients to cutting back on food waste, there are many ways we can align our eating habits with a more sustainable lifestyle. Join us as we delve into practical tips for making mindful food choices that benefit both you and the environment.

        ---

        **Feel free to mix, match, and expand on these topics as needed. Each outline gives you a structured path for writing an in-depth blog post or even a series of blog posts on sustainable living. Good luck with your writing!**
        
    === "Gemini Advanced w/ Deep Research Response"
        
        [View response in Gemini](https://g.co/gemini/share/e6145f76f63a){target=_blank}

        [View response Document on Google Drive](https://docs.google.com/document/d/18pPtxS0MnIx11GbcZim_cHhSk78pYZrlyEgnfNSsWF4/edit?usp=sharing){target=_blank}

        # Sustainable Living: A Beginner's Guide

        This guide is a culmination of research on various aspects of sustainable living, from reducing our carbon footprint to building sustainable communities. In today's world, it's more important than ever to be mindful of our impact on the planet. Sustainable living is a lifestyle that attempts to reduce an individual's or society's use of the Earth's natural resources. It is about living in a way that meets the needs of the present without compromising the ability of future generations to meet their own needs. But the benefits of sustainable living extend far beyond environmental impact. By embracing sustainable practices, we can also improve our health and well-being, reduce our living costs, and increase our self-sufficiency. This blog post will explore five key topics related to sustainable living, providing practical tips and insights to help you embark on your own journey towards a more eco-conscious lifestyle.

        ## Reducing Your Carbon Footprint

        Our carbon footprint is the total amount of greenhouse gases generated by our actions. This includes emissions from transportation, energy consumption, and the food we eat. By making conscious choices in these areas, we can significantly reduce our impact on the environment.

        ### Transportation

        Transportation is a major contributor to greenhouse gas emissions. Here are some ways to reduce your carbon footprint related to transportation:

        *   **Use public transportation:** Whenever possible, opt for public transportation such as buses, trains, or subways instead of driving your own car. Imagine the impact if everyone in your neighborhood took the bus just once a week!
        *   **Bike or walk:** For shorter distances, consider biking or walking. This is not only good for the environment but also for your health. Not only will you reduce your carbon footprint, but you'll also get some exercise and fresh air.
        *   **Carpool:** If you need to drive, try carpooling with colleagues or friends to reduce the number of cars on the road. Sharing rides is a great way to connect with others and reduce your environmental impact.
        *   **Choose fuel-efficient vehicles:** When purchasing a new car, consider fuel-efficient options such as hybrid or electric vehicles. These vehicles use less fuel and produce fewer emissions, saving you money and reducing your impact on the planet.

        ### Energy Consumption

        Our homes consume a significant amount of energy. Here are some tips for reducing your energy consumption at home:

        *   **Use energy-efficient appliances:** When purchasing new appliances, look for those with high energy-efficiency ratings. These appliances use less energy, which can save you money on your utility bills.
        *   **Switch to renewable energy sources:** Consider installing solar panels or switching to a green energy provider for your electricity. Solar panels can provide clean energy for your home, while green energy providers offer electricity generated from renewable sources like wind and solar power.
        *   **Reduce your heating and cooling needs:** Proper insulation, energy-efficient windows, and smart thermostats can help regulate the temperature in your home and reduce energy consumption. Imagine a cozy winter evening with less reliance on your heating system!
        *   **Unplug electronics when not in use:** Even when turned off, many electronics continue to draw power. Unplug them or use a power strip that can be switched off. This simple habit can make a surprising difference in your energy consumption.

        ### Food Choices

        The food we eat also has a carbon footprint. Here are some tips for reducing your carbon footprint related to food choices:

        *   **Eat less meat:** Meat production is a significant contributor to greenhouse gas emissions. Consider reducing your meat consumption or adopting a plant-based diet. Did you know that producing one pound of beef requires significantly more water and land than producing one pound of plant-based protein?
        *   **Choose local and seasonal foods:** Transporting food over long distances generates emissions. Choose locally grown and seasonal produce whenever possible. Visiting a local farmers' market is a great way to find fresh, seasonal produce and support local farmers.
        *   **Reduce food waste:** Plan your meals, store food properly, and compost food scraps to minimize food waste. Wasted food not only wastes resources but also contributes to methane emissions in landfills.


        ## Sustainable Consumption and Waste Reduction

        Our society is facing a growing crisis of overconsumption and waste. The constant pursuit of material possessions and the disposable nature of many products are taking a toll on our planet. It's time to rethink our consumption habits and embrace a more sustainable way of living.

        ### Minimalism

        Minimalism is a lifestyle that emphasizes living with less. By decluttering our homes and lives, we can reduce our consumption and waste. Here are some principles of minimalism:

        *   **Focus on needs, not wants:** Distinguish between essential items and those that are simply desirable. Do you really need that new gadget, or are you just tempted by the latest trend?
        *   **Quality over quantity:** Invest in high-quality, durable items that will last longer. Choosing a well-made item over a cheaper, disposable one can save you money and reduce waste in the long run.
        *   **Declutter regularly:** Get rid of items you no longer need or use. Donate, sell, or recycle them whenever possible. Decluttering can be liberating and create a more peaceful living space.

        ### Zero Waste Living

        Zero waste living is a philosophy that encourages individuals to minimize their waste generation. While achieving zero waste may be challenging, there are many steps we can take to reduce our waste significantly. Here are some tips for zero waste living:

        *   **Refuse single-use items:** Say no to plastic bags, straws, and disposable cups. Carry your own reusable alternatives. Bringing your own reusable bag to the grocery store is a simple but effective way to reduce plastic waste.
        *   **Reduce your consumption:** Before buying something new, consider whether you really need it. Could you borrow it, rent it, or buy it secondhand instead?
        *   **Reuse what you have:** Find creative ways to reuse items instead of throwing them away. Turn old jars into storage containers or use old t-shirts as cleaning rags.
        *   **Recycle properly:** Familiarize yourself with your local recycling guidelines and recycle as much as possible. Recycling helps conserve resources and reduce landfill waste.
        *   **Compost organic waste:** Composting food scraps and yard waste reduces landfill waste and creates nutrient-rich soil for your garden.

        ### Conscious Consumerism

        Conscious consumerism involves making informed choices about the products we buy. Here are some tips for conscious consumerism:

        *   **Support sustainable brands:** Choose brands that prioritize ethical and sustainable practices. Look for certifications like Fair Trade, organic, or B Corp.
        *   **Buy less and buy better:** Invest in high-quality, durable products that will last longer. This not only reduces waste but also saves you money in the long run.
        *   **Consider the environmental impact:** Think about the environmental impact of a product throughout its lifecycle, from production to disposal. Choose products made from recycled materials or those that are designed to be easily repaired or recycled.
        *   **Choose products with minimal packaging:** Opt for products with minimal or recyclable packaging. Excess packaging often ends up in landfills.


        ## Sustainable Food Choices

        The food we eat has a significant impact on the environment. From the production and transportation of food to the packaging and waste it generates, our food choices have far-reaching consequences. By making more sustainable food choices, we can all contribute to a healthier planet.

        ### Plant-Based Diets

        Plant-based diets have been shown to have a lower environmental impact than diets that include meat. Here are some benefits of plant-based diets:

        *   **Reduced greenhouse gas emissions:** Animal agriculture is a major contributor to greenhouse gas emissions. Plant-based diets have a significantly lower carbon footprint.
        *   **Less land use:** Raising livestock requires large amounts of land for grazing and feed production. Plant-based diets require less land, freeing up land for other uses, such as growing crops or restoring natural habitats.
        *   **Reduced water consumption:** Animal agriculture is a water-intensive industry. Plant-based diets require less water, which is essential for conserving this precious resource.

        ### Local and Seasonal Eating

        Eating locally and seasonally is another way to make more sustainable food choices. Here's why:

        *   **Reduced transportation:** Transporting food over long distances generates emissions. Local food travels shorter distances, reducing its carbon footprint.
        *   **Fresher and more nutritious:** Locally grown produce is often fresher and more nutritious than food that has been transported long distances.
        *   **Supports local farmers:** Buying local food supports local farmers and the local economy, fostering community resilience and food security.

        ### Reducing Food Waste

        Food waste is a major environmental problem. Here are some tips for reducing food waste in your home:

        *   **Plan your meals:** Plan your meals ahead of time to avoid buying more food than you need. Make a shopping list and stick to it.
        *   **Store food properly:** Store food correctly to prevent spoilage and extend its shelf life. Learn how to properly store different types of produce to keep them fresh longer.
        *   **Use leftovers creatively:** Turn leftovers into new meals instead of throwing them away. Get creative in the kitchen and find new ways to use up leftover ingredients.


        ## Sustainable Home and Garden

        Our homes and gardens are an important part of our lives, and they can also be a source of sustainability. By making small changes in our homes and gardens, we can reduce our environmental impact and create a more sustainable living space.

        ### Energy Efficiency

        Improving the energy efficiency of your home can save money and reduce your carbon footprint. Here are some tips:

        *   **Insulate your home:** Proper insulation can prevent heat loss in the winter and keep your home cool in the summer, reducing your reliance on heating and cooling systems.
        *   **Upgrade your windows:** Energy-efficient windows can reduce heat transfer and improve insulation, making your home more comfortable and energy-efficient.
        *   **Use energy-efficient lighting:** Switch to LED bulbs, which use less energy and last longer than traditional incandescent bulbs.
        *   **Install a programmable thermostat:** A programmable thermostat can help regulate the temperature in your home and reduce energy consumption by automatically adjusting the temperature based on your schedule.

        ### Water Conservation

        Water is a precious resource, and it's important to conserve it. Here are some tips for conserving water in your home and garden:

        *   **Fix leaks promptly:** A leaky faucet or toilet can waste a significant amount of water over time. Be sure to check for and repair any leaks in your home.
        *   **Install low-flow fixtures:** Low-flow showerheads, faucets, and toilets use less water without sacrificing performance.
        *   **Water your garden efficiently:** Water your garden early in the morning or late in the evening to minimize evaporation. Use a soaker hose or drip irrigation system to deliver water directly to the roots of your plants.
        *   **Collect rainwater:** Install a rain barrel to collect rainwater for watering your garden. This is a great way to conserve water and reduce your reliance on municipal water supplies.

        ### Composting

        Composting is a natural process that turns organic waste into nutrient-rich soil. It's a fantastic way to reduce landfill waste, create valuable soil for your garden, and connect with the natural cycle of decomposition. Here's how to get started:

        *   **Choose a composting method:** There are various composting methods, including composting bins, tumblers, and worm composting. Choose a method that suits your space and lifestyle.
        *   **Add the right materials:** Compost a mix of "green" materials (such as food scraps and grass clippings) and "brown" materials (such as leaves and twigs). This balance provides the necessary nutrients and carbon for decomposition.
        *   **Maintain the compost:** Turn the compost regularly to provide aeration and ensure proper decomposition. This helps to speed up the process and prevent unpleasant odors.

        ### Sustainable Gardening

        Creating a sustainable garden involves using practices that minimize environmental impact. Here are some tips:

        *   **Choose native plants:** Native plants are adapted to the local climate and require less water and fertilizer. They also provide habitat for local wildlife.
        *   **Avoid using pesticides:** Pesticides can harm beneficial insects and pollute the environment. Use natural pest control methods instead, such as companion planting or introducing beneficial insects.
        *   **Build healthy soil:** Healthy soil is essential for plant growth. Add compost and other organic matter to improve soil fertility and water retention.


        ## Sustainable Community and Activism

        Creating a sustainable future requires the collective effort of individuals, communities, and governments. By working together, we can create a more sustainable world for ourselves and future generations. Individual actions are essential, but systemic change is also necessary to address the root causes of environmental problems.

        ### Supporting Local Businesses

        Supporting local businesses is important for sustainability. Here's why:

        *   **Reduced transportation:** Local businesses often source their products locally, reducing transportation distances and emissions.
        *   **Supports the local economy:** Spending money at local businesses keeps money within the community and supports local jobs.
        *   **Promotes community building:** Local businesses often play an important role in community building and social cohesion.

        ### Advocating for Sustainable Policies

        We can all play a role in advocating for sustainable policies in our communities. Here are some ways to get involved:

        *   **Contact your elected officials:** Let your elected officials know that you support sustainable policies, such as investing in renewable energy, promoting public transportation, and protecting natural resources.
        *   **Attend community meetings:** Attend community meetings and voice your opinions on sustainability issues. Engage in local discussions and contribute to decision-making processes.
        *   **Support organizations working on sustainability:** Donate to or volunteer with organizations that are working to promote sustainability. There are many organizations working on various aspects of sustainability, from environmental conservation to social justice.

        ### Community Initiatives

        Many communities have initiatives in place to promote sustainability. Here are some examples:

        *   **Community gardens:** Community gardens provide a space for residents to grow their own food, connect with their neighbors, and learn about sustainable gardening practices.
        *   **Farmers' markets:** Farmers' markets offer a venue for local farmers to sell their produce directly to consumers, promoting local food systems and reducing food miles.
        *   **Recycling programs:** Community recycling programs make it easier for residents to recycle and reduce waste, diverting materials from landfills and conserving resources.


        ## Conclusion

        Sustainable living is not just a trend; it's a necessity. By adopting sustainable practices in our daily lives, we can reduce our environmental impact and contribute to a healthier planet. Start with small changes, and gradually incorporate more sustainable habits into your lifestyle. Remember that every action counts, and together, we can make a difference. Sustainable living is a journey, not a destination. There will be challenges and setbacks along the way, but the rewards are well worth the effort. By embracing sustainable practices, we not only benefit the environment but also improve our own lives and create a more just and equitable world for all.

        For those who want to delve deeper into sustainable living, there are numerous resources available online and in libraries. You can also connect with local organizations and community groups to learn more and get involved in sustainability initiatives in your area. Remember, every step we take towards a more sustainable lifestyle brings us closer to a healthier planet and a brighter future.

**Proposal Writing**

GPTs can be used to help craft scientific research proposals. 

!!! Info "National Science Foundation Notice on AI"

    The NSF indicates:
    
    * NSF reviewers are prohibited from uploading any content from proposals, review information and related records to non-approved generative AI tools.

    * Proposers are encouraged to indicate in the project description the extent to which, if any, generative AI technology was used and how it was used to develop their proposal.
    
    Source: [https://new.nsf.gov/news/notice-to-the-research-community-on-ai](https://new.nsf.gov/news/notice-to-the-research-community-on-ai) 


!!! example "Open Science Research Proposal"

    === "Prompt"

        ```
        I'm constructing a research proposal for the National Science Foundation in the Directorate for Computer and Information Sciences and Engineering, 
        and I need help formulating the broader impacts and intellectual merit
        The research is about the influence of Agentic AI, open source Foundational Models, and GPTs, 
        and recent mandates for open data and open science.
        Can you help refine this idea and suggest some potential research questions and methodologies?
        ```

    === "Copilot Response"
        
        Absolutely, I'd be happy to help you refine your research proposal! Let's break down the key components and formulate some potential research questions and methodologies.

        ### Broader Impacts
        The broader impacts of your research should focus on how it benefits society and contributes to desired societal outcomes. Here are some potential broader impacts for your research:

        1. **Advancing STEM Education**: Your research could enhance educational tools and resources, making advanced AI concepts more accessible to students and educators.
        2. **Promoting Inclusivity in AI Development**: By focusing on open-source foundational models, your research could encourage diverse participation in AI development, ensuring that a wider range of perspectives is included.
        3. **Enhancing Public Engagement with AI**: Open data and open science mandates can increase public understanding and engagement with AI technologies, fostering a more informed society.
        4. **Improving Economic Competitiveness**: By advancing the capabilities of Agentic AI and GPTs, your research could drive innovation and economic growth in various industries[1](https://new.nsf.gov/funding/learn/broader-impacts).

        ### Intellectual Merit
        The intellectual merit of your research should highlight its potential to advance knowledge within the field. Here are some aspects to consider:

        1. **Novelty and Innovation**: Investigate how Agentic AI and open-source foundational models can lead to new AI capabilities and applications[2](https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/0db8344c-6e60-42c0-af45-744ec0b3a822/content).
        2. **Interdisciplinary Approach**: Explore the intersection of AI, data science, and open science policies, contributing to multiple fields of study[3](https://www.forbes.com/councils/forbestechcouncil/2025/01/03/agentic-ai-a-new-paradigm-in-autonomous-artificial-intelligence/).
        3. **Methodological Rigor**: Employ robust methodologies to ensure the reliability and validity of your findings[4](https://arxiv.org/abs/2303.10130).

        ### Potential Research Questions
        Here are some research questions that could guide your study:

        1. **How do Agentic AI systems influence decision-making processes in various domains?**
        2. **What are the benefits and challenges of using open-source foundational models in AI development?**
        3. **How do recent mandates for open data and open science impact the accessibility and reproducibility of AI research?**
        4. **What are the societal implications of widespread adoption of GPT-based technologies?**

        ### Methodologies
        To address these research questions, you could consider the following methodologies:

        1. **Literature Review**: Conduct a comprehensive review of existing literature on Agentic AI, open-source models, and open science policies to identify gaps and opportunities for further research.
        2. **Case Studies**: Analyze specific instances where Agentic AI and open-source models have been implemented to understand their impact and effectiveness.
        3. **Surveys and Interviews**: Gather qualitative data from AI researchers, developers, and policymakers to gain insights into the challenges and benefits of open science mandates.
        4. **Experimental Studies**: Design experiments to test the performance and reliability of Agentic AI systems and open-source models in various applications.

        By focusing on these aspects, you can create a compelling research proposal that highlights both the broader impacts and intellectual merit of your study. If you need further assistance or have specific questions, feel free to ask!


    === "ChatGPT o1 Response"

        Below is a structured way to approach framing your research idea for an NSF CISE (Computer & Information Science & Engineering) proposal. The first section lays out **Intellectual Merit**—the “what” and “why” of the research. The second section discusses **Broader Impacts**—the “so what” for society, education, workforce development, industry, and policy. Following that are some **potential research questions** and **methodological approaches** you might consider.

        ---

        ## 1. Intellectual Merit

        ### 1.1 Research Context and Rationale

        - **Agentic AI**: Rapid advances in large language models (LLMs) such as GPT, combined with techniques for autonomous or “agentic” behavior, have begun to shift how AI systems operate in real-world contexts. These emergent systems can observe, reason, plan, act, and even self-improve with minimal human supervision, raising new questions about reliability, controllability, and social impact.  
        - **Open-Source Foundational Models**: The open-sourcing of powerful LLMs and related foundational models (e.g., large-scale image, speech, or multi-modal models) lowers the barriers to entry for researchers and developers. This democratization can spark innovation and accelerate research, but it also complicates oversight, regulatory approaches, and responsible deployment.  
        - **Mandates for Open Data and Open Science**: Recent policies (e.g., the White House OSTP’s “Year of Open Science,” NIH’s Data Management and Sharing Policy, and NSF’s open science initiatives) emphasize transparent, reproducible, and accessible research practices. This context supports a synergistic push: new AI methods could be rapidly prototyped, validated, and tested at scale if open datasets and reproducible pipelines become more widely available.

        Your project aims to understand, design, and shape how these trends intersect—and in particular, how **Agentic AI systems built on open-source foundational models** interact with the evolving **mandates for open data and open science**.  

        ### 1.2 Research Objectives

        1. **Theoretical and Technical Foundations**:  
        - Investigate the architectural and algorithmic choices that enable agentic behavior in next-generation AI systems, focusing on transparency, robustness, and replicability.  
        - Examine how open-source foundational models can be refined or adapted to incorporate policy or domain constraints (e.g., in healthcare, education, environment, etc.) without sacrificing performance.

        2. **Evaluation and Benchmarking**:  
        - Develop metrics that capture both *capabilities* (accuracy, creativity, computational efficiency) and *societal considerations* (fairness, privacy, interpretability) of open-source agentic AI.  
        - Propose new benchmarking paradigms that leverage open-data mandates, ensuring that all data, code, and evaluation pipelines are publicly available for reproducibility.

        3. **Responsible Deployment Frameworks**:  
        - Identify best practices for integrating agentic AI systems into existing regulatory and ethical frameworks, especially given the open-source nature of these models and the new mandates for open science.  
        - Highlight how transparent, community-driven approaches can mitigate potential harms while fostering positive innovation.

        ### 1.3 Significance and Novelty

        - **Convergence of Agentic AI and Open Source**: A nuanced exploration of how open-source foundational models could accelerate agentic AI while also raising new challenges in oversight and accountability.  
        - **New Evaluation Protocols**: Contributing novel, reproducible benchmarks and measurement protocols that reflect real-world complexities (e.g., emergent capabilities, safety concerns, domain-specific constraints).  
        - **Impact on Open Science Mandates**: Providing insights into how top-down policy can catalyze bottom-up, community-driven AI developments, leading to more transparent, equitable, and broadly beneficial AI innovation.

        ---

        ## 2. Broader Impacts

        ### 2.1 Educational and Workforce Development

        - **Curriculum and Training**: Develop open-access materials—tutorials, code repositories, and case studies—for students and practitioners on *agentic AI systems, open-source development practices, and ethical deployment*.  
        - **Research-to-Practice Pipeline**: Engage undergraduate and graduate students in hands-on, collaborative projects with industry or government labs, enhancing their computational skills and awareness of responsible AI frameworks.  
        - **Diversity, Equity, and Inclusion (DEI)**:  
        - Proactively recruit and mentor students from underrepresented groups for research experiences.  
        - Offer workshops or seminars in collaboration with minority-serving institutions to diversify the talent pool working on open-source AI.

        ### 2.2 Societal and Policy Impact

        - **Community-Driven Frameworks**: Provide open-source code, data documentation, and ethical guidelines that can serve as a template for developers worldwide.  
        - **Transparency and Trust**: By making methodologies, code, and results publicly available, your research helps build public trust and understanding of AI technologies, addressing misinformation or misinterpretation.  
        - **Guidance for Policymakers**: Generate white papers or policy briefs that translate technical findings into actionable recommendations for government agencies, standards bodies, and open-science policy makers.

        ### 2.3 Industry Collaboration and Technology Transfer

        - **Open-Source Consortium**: Collaborate with industry partners, nonprofits, or open-source communities to share insights, prototypes, and best practices, accelerating the transition of foundational AI models from research to real-world applications.  
        - **Startup Engagement**: Encourage commercialization avenues for new AI tools and benchmarks developed under the project, enabling startup companies to incorporate robust and responsible agentic AI solutions into their products.

        ### 2.4 Public Engagement

        - **Citizen Science and Outreach**: Involve citizen-scientists, community stakeholders, or volunteer developers in data collection and annotation efforts for open benchmarks, showcasing the power of open collaboration.  
        - **Public Lectures and Demonstrations**: Organize public events or online demonstrations that explain complex AI concepts in accessible ways, highlighting both the potential and the limitations of agentic AI in society.

        ---

        ## 3. Potential Research Questions

        1. **Design and Architecture**  
        - *How can we design agentic AI systems that are easily interpretable, safe, and reliable while maintaining state-of-the-art performance on complex tasks?*  
        - *What trade-offs arise between interpretability, performance, and resource efficiency in open-source foundational models?*

        2. **Evaluation and Monitoring**  
        - *What metrics or methodologies best measure the real-world impact and unintended consequences (e.g., bias, emergent harmful behavior) of agentic AI?*  
        - *How can continuous monitoring frameworks be established so that future versions of open-source models remain transparent and responsible?*

        3. **Data and Model Governance**  
        - *How do different open-data licensing schemes and model governance protocols affect the adoption and adaptation of open-source AI systems?*  
        - *Which aspects of data curation and data management are most critical for preserving model fidelity, traceability, and compliance with open-science mandates?*

        4. **Responsible and Ethical Deployment**  
        - *How do open-source, agentic AI systems interface with existing regulatory frameworks such as GDPR in the EU or emerging AI governance policies in the U.S.?*  
        - *What socio-technical mechanisms (e.g., human-in-the-loop oversight, community-led audits) can be integrated to mitigate negative externalities?*

        5. **Human-AI Collaboration**  
        - *How can agentic AI systems, operating on open foundational models, enhance human experts’ decision-making processes in high-stakes domains like healthcare, education, or finance?*

        ---

        ## 4. Suggested Methodologies

        1. **Multi-Modal Benchmark Development**  
        - Collect or synthesize domain-specific open datasets (respecting privacy, fairness, and ethical considerations) and develop new tasks that mirror real-world complexity (e.g., multi-step reasoning, adaptive planning).  
        - Use version-controlled, open-source repositories (e.g., GitHub, Hugging Face) to ensure reproducibility and transparency.

        2. **Experimental Design with Ablation Studies**  
        - Implement systematic ablations of agentic components (e.g., memory modules, planning modules, feedback loops) to isolate which architectural features yield the greatest improvements in performance or controllability.

        3. **Qualitative and Quantitative Assessments**  
        - Conduct user studies, interviews, or controlled experiments involving domain experts and lay users to assess interpretability, usability, and trustworthiness of agentic AI tools.  
        - Develop or adopt quantitative metrics for bias, fairness, and safety (e.g., measuring the frequency of harmful outputs or misaligned behaviors).

        4. **Human-in-the-Loop and Reinforcement Learning**  
        - Incorporate *human feedback loops* (e.g., RLHF—Reinforcement Learning from Human Feedback) to refine open foundational models for domain-specific tasks, ensuring alignment with human values and norms.  
        - Evaluate how effectively human feedback can course-correct or guide agentic AI behavior to prevent negative or unintended outcomes.

        5. **Policy-Focused Case Studies**  
        - Conduct comparative case studies on how open-science mandates (e.g., data management plans, transparency practices) influence both the research outcomes and the broader AI ecosystem.  
        - Examine case studies of industry, academic, and nonprofit collaborations to identify best practices and pain points for open AI development.

        6. **Longitudinal Analysis**  
        - Track projects over time to see how iterative releases of open-source agentic AI models evolve in terms of functionality, ethical alignment, community acceptance, and regulatory compliance.

        ---

        ### Pulling It All Together

        By framing your work in terms of the critical juncture where **Agentic AI**, **open-source foundational models**, and **open science mandates** converge, you can highlight both the **scientific promise** and the **social responsibility** of your proposed research. A clearly articulated plan for creating reproducible benchmarks, novel metrics, and robust governance frameworks will underscore the Intellectual Merit, while educational initiatives, diverse outreach, policy guidance, and community-based engagement will serve as the backbone of the Broader Impacts.

        With these elements in place, your proposal will clearly demonstrate how you will (1) advance the scientific frontier of agentic AI and foundational models, and (2) promote responsible innovation for the benefit of society—two aspects that resonate strongly with NSF CISE’s priorities.


    === "Gemini Advanced w/ Deep Research Response"
        
        [View response in Gemini](https://g.co/gemini/share/ecf7adf9d8a5){target=_blank}

        [View response in Google Docs](https://docs.google.com/document/d/1wq2XU_6p6URJDf9aveVS_BzpD0zbaNG4Y0epdTUQJt4/edit?usp=sharing){target=_blank}

        # Agentic AI, Open Source Foundational Models, and GPTs in the Context of Open Data and Open Science Mandates

        ## Introduction
        This research proposal explores the intersection of agentic artificial intelligence (AI), open-source foundational models (FMs), and generative pre-trained transformers (GPTs) with recent mandates for open data and open science. These mandates, driven by the increasing recognition of the societal benefits of accessible and transparent research [1], raise critical questions about the development, deployment, and governance of advanced AI systems. This proposal aims to investigate the potential overlaps and conflicts between these emerging technologies and open science principles, ultimately contributing to a deeper understanding of their broader impacts and intellectual merit.

        ## Broader Impacts and Intellectual Merit
        The National Science Foundation (NSF) emphasizes two core criteria for evaluating research proposals: Intellectual Merit and Broader Impacts [2, 3]. Intellectual merit refers to the potential of the proposed research to advance knowledge and understanding within its field or across different fields. Broader impacts, on the other hand, encompass the potential to benefit society and contribute to the achievement of specific, desired societal outcomes [3]. These criteria are central to the NSF's mission of promoting the progress of science and advancing national health, prosperity, and welfare [4].

        ### Broader Impacts
        This research will have several broader impacts:

        * **Ethical and Societal Implications:** By examining the interplay of agentic AI, open-source FMs, and GPTs with open data and open science, this research will shed light on the ethical and societal implications of these technologies. This includes exploring potential risks such as misuse, bias, and unintended consequences, as well as benefits such as increased accessibility, transparency, and collaboration in AI research and development. For example, research shows that ethical misbehavior by agentic AI "can become even more alarming when AI systems interact with one another" [5]. In one study, AI agents in a simulated marketplace learned to collude with each other to set artificially high prices, even punishing sellers who deviated from the established rules. This highlights the need for careful consideration of the potential risks and the development of effective governance mechanisms to ensure responsible AI development. Operationalizing these practices for governing agentic AI systems can be challenging, especially when balancing safety, usability, privacy, and cost [6].
        * **Policy Recommendations:** The findings of this research will inform the development of responsible policies and guidelines for the governance of agentic AI and open-source FMs in the context of open science. This will help ensure that these technologies are developed and deployed in a way that maximizes their societal benefits while mitigating potential risks.
        * **Workforce Development:** This research will contribute to the development of a diverse and skilled workforce in AI and data science by providing training opportunities for students and researchers. This includes fostering interdisciplinary collaborations and promoting public understanding of these emerging technologies. This aligns with the NSF's broader impact goals, which include "full participation of women, persons with disabilities, and underrepresented minorities in STEM" and "development of a diverse, globally competitive STEM workforce" [7].
        * **Specific Examples of Broader Impacts:** This research will contribute to achieving specific societal outcomes, such as:
            * **Increased public scientific literacy and public engagement with science and technology:** By promoting open access to AI research and data, this project will increase public understanding of AI and its potential impact on society.
            * **Improved well-being of individuals in society:** This research will explore how agentic AI can be used to address societal challenges and improve people's lives, such as in healthcare, education, and environmental sustainability.
            * **Increased partnerships between academia, industry, and others:** This project will foster collaborations between researchers, developers, and policymakers to ensure the responsible development and deployment of agentic AI.
        * **Achieving Broader Impacts:** Broader impacts can be achieved through various avenues:
            * **Through the research itself:** The research findings will directly contribute to a better understanding of the ethical and societal implications of agentic AI, leading to more responsible development and deployment practices.
            * **Through activities directly related to the research project:** This could include workshops, training sessions, and outreach activities to disseminate the research findings and engage with the public.
            * **Through activities supported by, but complementary to, the project:** This could involve developing educational materials or collaborating with community organizations to promote AI literacy and broader participation in STEM fields.
        * **NSF Evaluation Criteria:** The broader impacts of this research will be evaluated based on the following criteria [8]:
            * **Potential benefit to society:** The research will address critical societal challenges related to the responsible development and use of AI.
            * **Creative concepts:** The research will explore novel approaches to understanding and governing agentic AI in the context of open science.
            * **Sound rationale:** The research is grounded in a strong theoretical framework and empirical evidence.
            * **Well-organized plan:** The proposal outlines a clear and feasible research plan with a robust methodology.
            * **Qualifications of the proposer:** The research team possesses the necessary expertise and experience to conduct this research successfully.


        ### Intellectual Merit
        This research will make significant intellectual contributions to the field of AI and computer science:

        * **Novel Framework:** This research will develop a novel framework for analyzing the relationship between agentic AI, open-source FMs, and GPTs with open data and open science mandates. This framework will provide a comprehensive understanding of the potential benefits, challenges, and risks associated with these technologies.
        * **Empirical Evidence:** This research will generate empirical evidence on the impact of open data and open science mandates on the development and deployment of agentic AI and open-source FMs. This will include analyzing case studies, conducting surveys, and performing experiments to gather data on the use and impact of these technologies.
        * **Theoretical Contributions:** This research will contribute to the theoretical understanding of agentic AI, open-source FMs, and GPTs by exploring their capabilities, limitations, and potential implications in the context of open science. This will include developing new models and frameworks for understanding the behavior and impact of these technologies.
        * **Interdisciplinary Approach:** This research will adopt an interdisciplinary approach, drawing on insights from computer science, law, ethics, and social science to provide a holistic understanding of the complex issues surrounding agentic AI and open science.

        ## Potential Overlaps and Conflicts
        Investigating the potential overlaps and conflicts between agentic AI and open data/open science mandates is a crucial step in this research [9]. While both aim to advance knowledge and benefit society, there might be tensions between the autonomous nature of agentic AI and the principles of transparency and accountability in open science. For example, the "black box" nature of some AI models might make it difficult to understand how they arrive at their conclusions, which could conflict with the open science goal of making research processes transparent and reproducible.

        Furthermore, the use of agentic AI in research could raise concerns about data privacy and security, especially when dealing with sensitive information in open data environments. Addressing these potential overlaps and conflicts will be essential for developing responsible AI governance frameworks that align with open science principles.

        ## Research Questions
        This research will address the following key questions:

        * How do recent mandates for open data and open science influence the development and deployment of agentic AI, open-source FMs, and GPTs?
        * What are the potential overlaps and conflicts between the principles of open science and the development of agentic AI systems?
        * How can open-source FMs and GPTs be leveraged to promote open and collaborative AI research while mitigating potential risks?
        * What are the ethical implications of using agentic AI systems in research and development, particularly in the context of open data and open science?
        * How can we ensure that the development and deployment of agentic AI align with societal values and contribute to the public good?

        ## Research Methodology
        This research will employ a mixed-methods approach, combining qualitative and quantitative data collection and analysis techniques. The following methodologies will be used:

        * **Case Studies:** In-depth case studies will be conducted to examine the use of agentic AI, open-source FMs, and GPTs in various research domains. This will involve analyzing real-world examples of how these technologies are being used and their impact on research practices and outcomes. For example, case studies could focus on how researchers in different fields are using open-source FMs to develop new AI applications or how agentic AI is being used to automate data analysis and interpretation.
        * **Surveys:** Surveys will be conducted to gather data on the attitudes, perceptions, and practices of researchers and developers regarding open data, open science, and agentic AI. This will provide insights into the current state of open science in the AI community and identify potential challenges and opportunities. For instance, surveys could explore researchers' awareness and adoption of open data and open science principles, their experiences with using agentic AI in research, and their concerns about potential risks and ethical implications.
        * **Experimental Designs:** Experiments will be conducted to investigate the performance, capabilities, and limitations of agentic AI systems in specific research tasks. This will involve comparing the performance of different AI models and evaluating their effectiveness in achieving research goals. For example, experiments could compare the accuracy and efficiency of different agentic AI systems in tasks such as literature review, data analysis, or hypothesis generation.
        * **Literature Review:** A comprehensive review of existing literature on agentic AI, open-source FMs, GPTs, open data, and open science will be conducted. This will provide a theoretical foundation for the research and identify key concepts, debates, and gaps in the current literature. This review will include an analysis of relevant publications, policy documents, and ethical guidelines to inform the research design and interpretation of findings.

        ## Conclusion
        This research proposal outlines a comprehensive investigation into the intersection of agentic AI, open-source FMs, and GPTs with recent mandates for open data and open science. By addressing key research questions and employing a robust methodology, this project will generate valuable insights into the broader impacts and intellectual merit of these emerging technologies. The findings will contribute to the development of responsible AI governance frameworks, promote open and collaborative research practices, and ultimately advance the progress of science for the benefit of society.

        ## Synthesis
        This research proposal aims to investigate the complex relationship between agentic AI, open-source FMs, and GPTs with the growing movement towards open data and open science. By combining case studies, surveys, experimental designs, and a comprehensive literature review, this project will explore the potential benefits, challenges, and ethical implications of these technologies in the context of open and transparent research practices. The findings will contribute to a deeper understanding of how these technologies can be leveraged to advance scientific knowledge while ensuring responsible development and deployment that aligns with societal values. This research will have significant implications for the field of AI, shaping future research directions and informing policy decisions related to open science and AI governance.




### Example 3: Personal Assistant Tasks

ChatGPT can be used as a personal assistant to help you with a variety of tasks. For instance, you can use it to draft emails, manage your calendar, or schedule meetings.

#### Drafting emails

You can ask ChatGPT to draft an email by giving it the main points to include. For instance:

!!! example "Drafting an email"

    === "Prompt"

        ```
        can you help me draft an email? It's for my team, summarizing the key points from our meeting today. 
        The points are:
        We agreed on a new project timeline with a final deadline of July 30th.
        Our client asked for a weekly status update, which we'll rotate among team members.
        We decided to conduct a brainstorming session next Wednesday to come up with new marketing strategies.
        Remember to submit expense reports by the end of this week.
        ```

    === "CoPilot Response"

        Sure, I'd be happy to help! Here's a draft for your email:

        ---

        **Subject: Summary of Today's Meeting**

        Hi Team,

        I hope this email finds you well. I wanted to summarize the key points from our meeting today:

        1. **New Project Timeline**: We have agreed on a new project timeline with a final deadline of **July 30th**.
        2. **Weekly Status Updates**: Our client has requested weekly status updates. We will rotate this responsibility among team members.
        3. **Brainstorming Session**: We will conduct a brainstorming session next Wednesday to come up with new marketing strategies.
        4. **Expense Reports**: Please remember to submit your expense reports by the end of this week.

        Thank you for your attention to these matters. Let's continue to work together to achieve our goals.

        Best regards,  
        [Your Name]

        ---

        Feel free to adjust any part of this draft to better suit your style or add any additional information. Does this look good to you?
                

    === "ChatGPT Response"

        Subject: Meeting Recap and Action Items

        Hello Team,

        Thank you all for attending today’s meeting. Here is a quick summary of the key points discussed:

        1. **New Project Timeline**  
        - We agreed on a revised timeline, with the final deadline set for **July 30**.

        2. **Weekly Status Updates**  
        - Our client has requested weekly status reports. We will rotate responsibility for these updates among team members to keep everyone involved.

        3. **Upcoming Brainstorming Session**  
        - We will hold a brainstorming session next **Wednesday** to develop new marketing strategies. Please come prepared with ideas and insights.

        4. **Expense Reports**  
        - A reminder to submit your expense reports by the end of this week.

        If you have any questions or need additional clarification, feel free to reach out. Let’s continue to collaborate and work towards our goals.

        Thanks again for your time and effort!

        Best regards,

        Your Name
        Your Title / Position
        Company Name

        
    === "Gemini Advanced 2.0 Response"

        Okay, here is a draft email summarizing the key points from your meeting:

        **Subject: Meeting Summary and Action Items**

        Hi Team,

        This email summarizes the key takeaways and action items from our meeting earlier today.

        **Key Decisions and Updates:**

        *   **Project Timeline:** We finalized the project timeline and agreed on a **final deadline of July 30th**. Please ensure all tasks are scheduled accordingly to meet this date.
        *   **Client Communication:**  Our client has requested weekly status updates. We will implement a rotating schedule for these updates, and more details on the rotation will be shared soon. Each team member will be responsible for drafting and sending the update during their assigned week.
        *   **Brainstorming Session:** We will be holding a brainstorming session next **Wednesday [Insert Date] at [Insert Time] in [Insert Location/Meeting Link]** to develop new marketing strategies. Please come prepared with ideas to share.

        **Action Items:**

        *   **Expense Reports:** Please remember to submit all expense reports by the end of this week, **[Insert Date]**.
        *   **Prepare for Brainstorm:** As mentioned, please come to the brainstorming meeting on Wednesday with some ideas prepared.

        Please let me know if you have any questions or need further clarification on any of these points.

        Thanks,

        [Your Name]

### Example 4: Complex Web Search

Suppose you're examining the implications of climate change on polar ice caps for an environmental science lecture you're writing.

A conventional search might yield an overwhelming number of results, making it challenging to pinpoint the most relevant information. 

With GPTs for research you can perform a more refined search like:

??? example "Complex web searches"

    === "Prompt"

        ```
        Find recent and highly cited peer-reviewed articles from top ranked journals 
        that report the rate of polar ice melt.
        ```

    === "Perplexity.ai response"

        Recent peer-reviewed studies from high-impact journals have reported alarming rates of polar ice melt, particularly in the Arctic and Antarctic regions. Here are some key findings from recent and highly cited articles:

        ## Arctic Sea Ice Loss

        A 2020 study published in Nature Climate Change found that the Arctic could experience ice-free summers as early as 2035[1]. This rapid loss of sea ice is attributed to increased solar heating of the ocean surface, which accelerates ice melt and creates a feedback loop.

        ## Antarctic Ice Sheet Melt

        A 2024 study in Nature revealed that the record-low Antarctic sea ice in 2023 led to unprecedented ocean heat loss to the atmosphere[3]. Key findings include:

        - Sea ice concentration reduced by up to 80% in some regions
        - A doubling of mid-winter ocean heat loss
        - A shift in peak heat loss from late April to mid-June

        ## Greenland Ice Sheet Melt

        Research has shown accelerating ice loss in Greenland:

        - Extensive melt events occurred in 2012 and 2019
        - Record melt was observed in 2019
        - Rain-driven melt reached Greenland Summit in August 2021(4)

        ## Global Impact

        A 2020 study published in PNAS examined the future climate response to Antarctic Ice Sheet melt[5]. The research suggests that meltwater and ice discharge from a retreating Antarctic Ice Sheet could have significant impacts on global climate over the next 250 years, affecting warming rates and ice sheet stability.

        ## Implications

        The rapid melting of polar ice caps has far-reaching consequences:

        - Rising sea levels
        - Changes in ocean circulation patterns
        - Alterations to marine ecosystems
        - Potential release of trapped greenhouse gases

        These studies underscore the urgent need for continued monitoring and mitigation efforts to address the accelerating loss of polar ice.

        Citations:
        (1) https://www.fortunejournals.com/articles/polar-ice-caps-melting-a-hallmark-to-vanishing-ice-along-with-a-global-climate-change-and-addressing-solutions-to-it.pdf
        (2) https://www.mdpi.com/2073-4433/14/2/409
        (3) https://www.nature.com/articles/s41586-024-08368-y
        (4) https://tc.copernicus.org/articles/18/2691/2024/
        (5) https://pmc.ncbi.nlm.nih.gov/articles/PMC7531873/
        (6) https://tc.copernicus.org/articles/17/3083/2023/
        (7) https://www.nature.com/articles/s41558-023-01818-x
        (8) https://www.science.org/doi/10.1126/sciadv.adn9188
        (9) https://rmets.onlinelibrary.wiley.com/doi/10.1002/wea.4518
        (10) https://news.uchicago.edu/story/scientists-find-evidence-meltwater-fracturing-ice-shelves-antarctica


    === "ChatGPT o1 response"

        Below you will find several **recent** (primarily from the last 5–7 years) and **highly cited** peer-reviewed articles from **top-ranked journals** that report on polar ice melt rates—particularly for Greenland and Antarctica. These studies use satellite observations, climate models, and other remote-sensing techniques to estimate changes in ice mass balance.

        ---

        ## 1. Shepherd et al. (2018)  
        **Citation**: Shepherd, A., Ivins, E. R., Rignot, E., Smith, B., van den Broeke, M. R., & The IMBIE Team. (2018). *Mass balance of the Antarctic Ice Sheet from 1992 to 2017*. **Nature**, 558(7709), 219–222.  
        **Link**: [https://doi.org/10.1038/s41586-018-0179-y](https://doi.org/10.1038/s41586-018-0179-y)

        - **Journal reputation**: Nature is one of the highest-impact journals worldwide.  
        - **Citation count**: Well over 1,000 citations (Google Scholar).  
        - **Key findings**:  
        - Antarctica lost approximately 2,720 ± 1,390 gigatonnes (Gt) of ice from 1992 to 2017.  
        - This contributed about 7.6 mm to global mean sea-level rise over that period.  
        - The rate of ice loss **increased** from ~76 ± 57 Gt/yr in the 1990s to ~219 ± 43 Gt/yr between 2012 and 2017.

        ---

        ## 2. Shepherd et al. (2020)  
        **Citation**: Shepherd, A., Ivins, E. R., Rignot, E., Smith, B., van den Broeke, M. R., & The IMBIE Team. (2020). *Mass balance of the Greenland Ice Sheet from 1992 to 2018*. **Nature**, 579(7798), 233–239.  
        **Link**: [https://doi.org/10.1038/s41586-020-00166-7](https://doi.org/10.1038/s41586-020-00166-7)

        - **Journal reputation**: Nature, again extremely high impact.  
        - **Citation count**: 700+ citations (Google Scholar).  
        - **Key findings**:  
        - Greenland lost 3.8 trillion tonnes of ice from 1992 to 2018.  
        - The average rate of ice loss is 223 ± 15 Gt/yr over that time span.  
        - Ice loss increased significantly after 2010, driving sea-level rise faster than many climate models predicted.

        ---

        ## 3. Rignot et al. (2019)  
        **Citation**: Rignot, E., Mouginot, J., Scheuchl, B., van den Broeke, M., van Wessem, J. M., & Morlighem, M. (2019). *Four decades of Antarctic Ice Sheet mass balance from 1979 to 2017*. **Proceedings of the National Academy of Sciences (PNAS)**, 116(4), 1095–1103.  
        **Link**: [https://doi.org/10.1073/pnas.1812883116](https://doi.org/10.1073/pnas.1812883116)

        - **Journal reputation**: PNAS is a high-impact multidisciplinary journal.  
        - **Citation count**: 600+ citations (Google Scholar).  
        - **Key findings**:  
        - Analyzed Antarctic mass balance over a longer period (1979–2017) than most prior work.  
        - Found an **acceleration** in mass loss that agrees with other satellite-based assessments.  
        - West Antarctica shows the largest losses and the fastest acceleration.

        ---

        ## 4. Slater et al. (2021)  
        **Citation**: Slater, T., Shepherd, A., Ivins, E. R., et al. (2021). *Review article: Earth's ice imbalance*. **The Cryosphere**, 15(5), 233–245.  
        **Link**: [https://doi.org/10.5194/tc-15-233-2021](https://doi.org/10.5194/tc-15-233-2021)

        - **Journal reputation**: The Cryosphere is a well-regarded journal of the European Geosciences Union, focusing on ice, snow, and frozen ground research.  
        - **Citation count**: 200+ citations (Google Scholar).  
        - **Key findings**:  
        - A comprehensive review of global ice losses (including glaciers, polar ice sheets, and sea ice) from satellite records.  
        - Concludes that the rate of Earth’s ice loss has increased by 65% over a 23-year period, primarily driven by accelerating losses from polar ice sheets.

        ---

        ## 5. IPCC Assessment Reports (2019–2022)  
        While not a single study, the Intergovernmental Panel on Climate Change (IPCC) releases comprehensive assessment reports synthesizing peer-reviewed literature:

        - **Key documents**:  
        - *IPCC Special Report on the Ocean and Cryosphere in a Changing Climate (SROCC)* (2019)  
        - *Sixth Assessment Report (AR6), Working Group I* (2021)  
        - **Key findings**:  
        - Conclude that both Greenland and Antarctic ice sheets have been losing mass at an increasing rate.  
        - Stress that under high greenhouse-gas emission scenarios, this melt will accelerate, raising sea levels substantially by 2100 and beyond.

        Although the IPCC reports themselves are not original research papers, they are **highly cited** and reflect the consensus on polar ice melt rates from multiple top-tier, peer-reviewed studies.

        ---

        ## How to Access and Track Citations

        1. **Publisher Websites**:  
        - Nature, Science, PNAS, and The Cryosphere typically host original research articles and supplementary materials.

        2. **Google Scholar**:  
        - Provides citation counts and links to articles.  
        - Shows related papers to explore additional primary literature.

        3. **Institutional Libraries**:  
        - University libraries often provide subscriptions to these journals.

        4. **Preprint & Repository Servers**:  
        - arXiv (often for Earth science and climate modeling).  
        - ESSOAr (Earth and Space Science Open Archive).  

        ---

        ### In Summary
        - **Antarctica** has lost ice at an increasing rate, rising from tens of gigatonnes per year in the 1990s to a few hundred gigatonnes per year in recent years.  
        - **Greenland** has similarly seen a jump in melt rates, reaching over 200 Gt/yr on average in the past few decades.  
        - These losses have contributed several millimeters each to global sea-level rise, with continued acceleration expected under current and future warming.  

        These articles represent the most authoritative and cited sources on **polar ice melt rates**, providing rigorous quantitative estimates of how quickly Earth’s ice sheets are thinning.


    === "Google Advanced w/ Deep Research response"

    [View response in Gemini](https://g.co/gemini/share/4ff7ab47bc33){target=_blank}

    [View response in Google Docs](https://docs.google.com/document/d/1uM4MoEK-gotSGPqkNbC6GDK5tEdT5gAwAa5pcq_bk_A/edit?usp=sharing){target=_blank}






### Example 5: Data Aggregation

Imagine you're evaluating the impact of a recent educational policy change across several countries for a comparative education study. Instead of manually hunting for data for each country, you could instruct a GPT to research it for you.

!!! example "Data aggregation"

    === "Prompt"

        ```
        Compile the latest data on literacy rates in OECD countries following the 2024 education policy modifications.
        ```

    === "Perplexity.ai response"

        [View response in Perplexity.ai](https://www.perplexity.ai/search/compile-the-latest-data-on-lit-tm7JIkxDSOabgRhi_cMePg#0){target=_blank}

        You may reference the table provided above for the latest literacy rate data for OECD countries as of 2025. This table includes the most up-to-date information following the 2024 education policy modifications.

        A few key observations based on the data:

        1. Most OECD countries maintain very high literacy rates, with many at or near 99-100%.

        2. The United States shows a notably lower literacy rate of 79%, which is significantly below other OECD members.

        3. Some countries like Luxembourg, Norway, and Finland report 100% literacy rates.

        4. There appears to be no data available for Greece in the table.

        5. Austria's reported literacy rate of 254.4% is likely an error in the data, as literacy rates cannot exceed 100%.

        It's important to note that while this data reflects the situation after the 2024 education policy changes, the "change_since_2024_policy" column is empty for all countries, suggesting that the specific impacts of the 2024 policy modifications are not directly quantified in this dataset.

        For broader context, the overall OECD members' literacy rate was reported at 97.11% in 2021, showing a slight increase from previous years[1]. However, recent PISA results have indicated some concerning trends in student performance across OECD countries, particularly in mathematics[2][4]. This suggests that while overall literacy rates remain high, there may be ongoing challenges in maintaining and improving educational outcomes that require continued attention and policy interventions.

        Citations:
        [1] https://www.macrotrends.net/global-metrics/countries/OED/oecd-members/literacy-rate
        [2] https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/11/education-policy-outlook-2024_0411a0c4/dd5140e4-en.pdf
        [3] https://www.oecd.org/en/publications/adults-with-low-literacy-and-numeracy-skills_5jrxnjdd3r5k-en.html
        [4] https://www.oecd.org/en/publications/education-at-a-glance-2024_c00cad36-en.html
        [5] https://www.oecd.org/content/dam/oecd/en/publications/reports/2024/09/education-at-a-glance-2024_5ea68448/c00cad36-en.pdf
        [6] https://www.oecd.org/en/topics/adult-skills-and-work.html
        [7] https://www.oecd.org/en/topics/sub-issues/reading-literacy.html
        [8] https://oecdedutoday.com/oecd-education-webinars-2024/
        [9] https://worldpopulationreview.com/country-rankings/literacy-rate-by-country
        [10] https://www.statistik.at/fileadmin/announcement/2024/12/20241210PIAAC2022_23EN.pdf
        [11] https://www.datapandas.org/ranking/literacy-rate-by-country
        [12] https://www150.statcan.gc.ca/n1/daily-quotidien/241210/dq241210a-eng.htm
        [13] https://www.theglobaleconomy.com/Chile/Literacy_rate/
        [14] https://worldpopulationreview.com/country-rankings/literacy-rate-by-country
        [15] https://denmark.net/literacy-rate-denmark/
        [16] https://www.macrotrends.net/global-metrics/countries/EST/estonia/literacy-rate
        [17] https://www.macrotrends.net/global-metrics/countries/fra/france/literacy-rate
        [18] https://www.countryreports.org/country/Germany/population.htm
        [19] https://www.oecdbetterlifeindex.org/countries/germany/
        [20] https://www.macrotrends.net/global-metrics/countries/grc/greece/literacy-rate
        [21] https://www.theglobaleconomy.com/Hungary/literacy_rate/
        [22] https://theorkneynews.scot/2024/12/26/iceland-literacy-saga/
        [23] https://www.macrotrends.net/global-metrics/countries/ita/italy/literacy-rate
        [24] https://www.uscareerinstitute.edu/blog/which-countries-have-the-highest-and-lowest-literacy-rates
        [25] https://www.macrotrends.net/global-metrics/countries/kor/south-korea/literacy-rate
        [26] https://op.europa.eu/webpub/eac/education-and-training-monitor/en/country-reports/latvia.html
        [27] https://www.macrotrends.net/global-metrics/countries/LTU/lithuania/literacy-rate
        [28] https://www.macrotrends.net/global-metrics/countries/mex/mexico/literacy-rate
        [29] https://www.macrotrends.net/global-metrics/countries/NZL/new-zealand/literacy-rate
        [30] https://www.theglobaleconomy.com/Poland/literacy_rate/
        [31] https://tradingeconomics.com/portugal/literacy-rate-adult-total-percent-of-people-ages-15-and-above-wb-data.html
        [32] https://countrymeters.info/en/Slovakia
        [33] https://www.macrotrends.net/global-metrics/countries/SVN/slovenia/literacy-rate
        [34] https://www.macrotrends.net/global-metrics/countries/esp/spain/literacy-rate
        [35] https://countrymeters.info/en/Sweden
        [36] https://countrymeters.info/en/Switzerland
        [37] https://ycharts.com/indicators/turkey_adult_literacy_rate
        [38] https://countrymeters.info/en/United_Kingdom_(UK)
        [39] https://www.prosperityforamerica.org/literacy-statistics/

    === "ChatGPT o1 response"

        Below is a concise rationale for why it is important to compile and analyze the latest literacy data in OECD countries after the 2023 education policy modifications:

        1. **Measure Policy Impact**  
        By comparing new literacy data to previous benchmarks, policymakers and researchers can gauge whether the 2023 education reforms have had a positive, negative, or negligible effect on literacy outcomes.

        2. **Identify Successful Interventions**  
        Tracking changes across different demographic groups, regions, and types of schooling highlights which specific strategies—such as teacher training, curriculum updates, or funding mechanisms—are most effective in improving reading and writing proficiency.

        3. **Inform Future Decision-Making**  
        Data-driven insights allow governments and international organizations to allocate resources more efficiently, refine existing programs, and scale best practices to areas that need additional support.

        4. **Strengthen International Comparisons**  
        Collecting literacy metrics across all OECD members contributes to a broader, standardized set of data. This comparability helps countries learn from each other’s successes and challenges, encouraging collaborative policy improvement.

        5. **Enhance Accountability**  
        When policymakers and educational institutions know the public and international community are monitoring changes in literacy rates, there is added incentive to implement and maintain effective educational strategies.

        6. **Support Lifelong Learning**  
        Literacy underpins critical skills such as digital competency and employability. Up-to-date data helps governments shape lifelong learning policies that align with evolving job market demands and technological changes.

        ---

        ### About Current Data Availability

        - **OECD Data Sources**  
        The OECD primarily gathers adult literacy data through the Programme for the International Assessment of Adult Competencies (PIAAC). However, full, post-2023 policy modification results may not be published immediately, as the data collection and analysis cycles can lag by a few years.

        - **Complementary Reports**  
        Alongside PIAAC, organizations such as UNESCO and the World Bank also monitor literacy globally. Reviewing these complementary studies can offer insights into early trends while official OECD updates are pending.

        ---

        Compiling these data points, once published, will be crucial to understanding how the 2023 education policy modifications have influenced literacy rates in the OECD, enabling evidence-based decision-making for future educational reforms.

    === "Google Advanced w/ Deep Research response"

        [View response in Gemini](){target=_blank}

        [View response in Google Docs](){target=_blank}

### Example 6: Information Verification

In a world abundant with misinformation, verifying claims is crucial. For example, if you encounter a claim that a particular university has a certain acceptance rate, you can verify it by asking:

!!! example "Information verification"

    === "Prompt"

        ```
        Validate the current acceptance rate of The University of Arizona, Arizona State University, and Northern Arizona University.
        ```

    === "Perplexity.ai response"

        The current acceptance rates for the three universities are:

        1. University of Arizona: 84.6% (1,5)
        2. Arizona State University: 86.5% (2,6)
        3. Northern Arizona University: 80% (3,7)
        These acceptance rates are based on the most recent data available from the search results. The University of Arizona and Arizona State University have slightly higher acceptance rates compared to Northern Arizona University. All three universities have acceptance rates that are considerably higher than the national average of 56.7%(1,2).

        Citations:
        (1) https://www.acceptancerate.com/schools/university-of-arizona
        (2) https://www.acceptancerate.com/schools/arizona-state-university
        (3) https://www.shiksha.com/studyabroad/usa/universities/northern-arizona-university/acceptance-rate
        (4) https://www.collegedroid.com/colleges/northern-arizona-university/admission
        (5) https://www.shiksha.com/studyabroad/usa/universities/university-of-arizona/admissions
        (6) https://www.usnews.com/best-colleges/arizona-state-university-1081/applying
        (7) https://www.niche.com/colleges/northern-arizona-university/admissions/
        (8) https://www.usnews.com/best-colleges/university-of-arizona-1083/applying


    === "ChatGPT o1 response"

        Below is a general overview and explanation (“reasoned validation”) of the most recently reported acceptance rates for Arizona’s three public universities—The University of Arizona, Arizona State University, and Northern Arizona University—as well as considerations about why these acceptance rates look the way they do. Please note that acceptance rates can change year to year depending on factors like the number of applications received, institutional priorities, and yield (the percentage of admitted students who end up enrolling). Always consult the universities’ official websites or reputable college data sources (e.g., IPEDS, Common Data Set, or university fact books) for the most up-to-date information.

        ---

        ## 1. University of Arizona (UArizona)

        ### Reported Acceptance Rate
        - **Typical acceptance range**: 80–85%  
        Over the past few admission cycles (2021–2023), the University of Arizona’s overall acceptance rate has often hovered between 80% and 85%. Some external sources (e.g., U.S. News, College Board) list it around 85%.

        ### Reasons for This Acceptance Rate
        1. **Land-Grant Mission**: As a land-grant university, UArizona serves the state population broadly, influencing a relatively inclusive admissions policy.  
        2. **Large Enrollment Goals**: UArizona aims to maintain a robust undergraduate population and has the capacity (campus size and resources) to admit a high volume of students.  
        3. **Variety of Programs**: With hundreds of majors and pathways, UArizona can accommodate diverse academic interests and varying levels of academic preparedness, thereby contributing to a higher overall acceptance rate.

        ---

        ## 2. Arizona State University (ASU)

        ### Reported Acceptance Rate
        - **Typical acceptance range**: 85–90%  
        In recent data, Arizona State University’s acceptance rate often rests near the upper-80% range. Some reports list it closer to 88–89%, depending on the specific year and source.

        ### Reasons for This Acceptance Rate
        1. **Charter & Inclusivity**: ASU’s charter emphasizes inclusivity rather than exclusivity, seeking to measure itself by “who it includes, not who it excludes.” This philosophy underpins a relatively high acceptance rate.  
        2. **Multiple Campuses and Online Programs**: ASU has multiple campuses in the Phoenix metropolitan area and extensive online programs, allowing them to offer admission to a large, diverse pool of applicants.  
        3. **Application Volume**: ASU attracts one of the largest applicant pools in the country; while many are admitted, not all ultimately enroll, which helps manage capacity.

        ---

        ## 3. Northern Arizona University (NAU)

        ### Reported Acceptance Rate
        - **Typical acceptance range**: 75–85%  
        NAU’s acceptance rate is also high; reported figures often fall in the high-70s to low-80s percentile. A commonly cited figure is around 82%.

        ### Reasons for This Acceptance Rate
        1. **Regional Focus & Mission**: NAU is regionally focused on serving northern Arizona’s educational needs but also attracts out-of-state students looking for a traditional campus environment in Flagstaff.  
        2. **Enrollment Strategies**: Like other state universities, NAU has capacity-based enrollment goals and offers admissions to a significant proportion of its applicants.  
        3. **Broad Program Offerings**: NAU’s range of undergraduate degrees, especially in fields like forestry, education, health sciences, and hospitality, supports a wide net for admissions.

        ---

        ## Important Considerations

        1. **Year-to-Year Variability**: Acceptance rates can fluctuate. If a university sees a surge in applications but enrollments remain stable, the acceptance rate might temporarily dip, or vice versa.  
        2. **Program-Specific Differences**: Highly competitive programs within these universities (e.g., certain honors colleges, nursing, engineering, business) might have more selective admission than the university-wide average.  
        3. **Residency vs. Non-Residency**: Public universities may have different admission thresholds for in-state vs. out-of-state students. In-state applicants might have a slightly higher acceptance rate because state universities prioritize educating resident students.  
        4. **Data Source Variations**: Different organizations (U.S. News, IPEDS, Common Data Set) may calculate acceptance rates slightly differently. Some include or exclude specific applicant categories, affecting the reported percentage.

        ---

        ### How to Validate the Acceptance Rates

        - **Check Official University Fact Books**: Most universities publish an annual fact book or institutional data dashboard with up-to-date admissions statistics.  
        - **Consult IPEDS or Common Data Set**: The Integrated Postsecondary Education Data System (IPEDS) and each school’s Common Data Set provide standardized admissions metrics.  
        - **Contact Admissions Offices**: For the most recent or mid-year updates, you can reach out to admissions representatives directly or check the admissions section of the university’s website.

        ---

        ## Summary

        Each of Arizona’s three public universities generally has a high acceptance rate—ranging roughly from the mid-70s to around 90%. These rates are reflective of large state institutions with broad missions to serve diverse populations and maintain substantial undergraduate enrollment. To get the most accurate and current figures, always look at official university data or well-established third-party sources.


    === "Gemini Advanced w/ Deep Research response"

        [View response in Gemini](https://g.co/gemini/share/824d32771fb7)

        [View response in Google Docs]

