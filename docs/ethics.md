# Ethics of Artificial Intelligence

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

## [:material-scale-balance: Ethical and Legal Considerations](legal.md)

## [:material-mirror: Transparency & Accountability](transparency.md)

## [:simple-weightsandbiases: Bias & Discrimination](bias.md)

## History

In 1956 a small group of scientists gathered at [Dartmouth](https://home.dartmouth.edu/about/artificial-intelligence-ai-coined-dartmouth){target=_blank} for a [Summer Research Project on Artificial Intelligence](https://spectrum.ieee.org/dartmouth-ai-workshop){target=_blank}. 

A new field of Science had begun. 

<figure>
<a href="https://spectrum.ieee.org/dartmouth-ai-workshop" target="_blank" rel="noopener noreferrer">
    <img src="https://spectrum.ieee.org/media-library/close-up-of-a-black-and-white-photo-of-seven-smiling-men-sitting-on-a-lawn.jpg?id=33603729&width=1800&quality=85" alt="Dartmouth AI Workshop, 1956" width="700">
</a>
<figcaption><a href="https://spectrum.ieee.org/dartmouth-ai-workshop" target="_blank" rel="noopener noreferrer">Dartmouth Summer Research Project on Artificial Intelligence, 1956. Credit: IEEE Spectrum, The Minsky Family</a></figcaption>
</figure>

Over the next 70 years, Artificial Intelligence persisted mainly in [the minds of science fiction writers](legal.md#science-fiction-or-philosophical-theory) and the small group of industry researchers and academics who continued to work toward creating the digital infrastructure needed for Artificial Intelligence to bloom, and to one day achieve the ultimate goal of [Artificial General Intelligence (AGI)(:simple-wikipedia:)](https://en.wikipedia.org/wiki/Artificial_general_intelligence){target=_blank}. 

## Using AI ethically

As consumers of GPTs and other AI platforms, we must consider in what ways can we use AI both effectively, and ethically.

**When can you use a GPT for research and education?**

``` mermaid
graph TB
  A((Start)) --> B("Does it matter if the outputs are true?");
  B -->| No | F("Safe to use GPT");
  B -->| Yes | C("Do you have the ability to verify output truth and accuracy?");
  C -->| Yes | D("Understand legal and moral responsibility of your errors?");
  C -->| No | E("Unsafe to use GPT");
  D -->| Yes | F("Safe to use GPT");
  D -->| No | E("Unsafe to use GPT");

  style A fill:#2ECC71,stroke:#fff,stroke-width:2px,color:#fff
  style B fill:#F7DC6F,stroke:#fff,stroke-width:2px,color:#000
  style C fill:#F7DC6F,stroke:#fff,stroke-width:2px,color:#000
  style D fill:#F7DC6F,stroke:#fff,stroke-width:2px,color:#000
  style E fill:#C0392B,stroke:#fff,stroke-width:2px,color:#fff
  style F fill:#2ECC71,stroke:#fff,stroke-width:2px,color:#fff
```

Figure credit: :fontawesome-brands-creative-commons-by: [ChatGPT and Artificial Intelligence in Education, UNESCO 2023 :fontawesome-regular-file-pdf:](https://www.iesalc.unesco.org/wp-content/uploads/2023/04/ChatGPT-and-Artificial-Intelligence-in-higher-education-Quick-Start-guide_EN_FINAL.pdf){target=_blank}

</br></br>

!!! Danger "The :ox: :poop: Bullshit Machines"

    Professors Carl T. Bergstrom and Jevin D. West teach a course at University of Washington titled "Calling Bullshit", they have written an e-book on GPTs called:

    ["Modern-Day Oracles or Bullshit Machines?"](https://thebullshitmachines.com/table-of-contents/index.html){target=_blanks}

    Their website provides online lesson vignettes and materials for instructors.


## Assessment

??? Question "Can you explain the difference between "Ethics of AI" and "Ethical AI?""

    Hint: Refer to how [Siau and Wang (2020)](#ethics-of-artificial-intelligence) define each term

    ??? Success "Ethics of AI"

        * **Ethics of AI** refers to principles and regulations

    ??? Success "Ethical AI"

        * **Ethical AI** focuses on how AI behaves

??? Question "How does Asimov's Three Laws of Robotics relate to modern ethical concerns of AI?"

    ??? Success "Do no harm"

        Asmiov emphasizes preventing harm to humans and how that concept informs current AI safety practices.

??? Question "True or False: The Turing Trap suggests that efforts to make AI more human-like will empower workers' economic and political power."

    ??? Failure "False"

        The Turing Trap warns against replacing humans with AI, and that AI could be used to drive down wages and to a loss of economic and political power. 

??? Question "Name at least one major declaration or agreement on AI Ethics"

    Hint: See [Table 2](#table-2-international-ai-agreements)

    ??? Success "International Agreements"
             
        * Council of Europe Framework Convention on Artificial Intelligence and human rights

        * Political Declaration on Responsible Military Use of Artificial Intelligence and Autonomy

        * G20 AI Principles
    
    ??? Success "Principles and Ethics"

        * Asilomar AI Principles

        * UNESCO Recommendation on the Ethics of Artificial Intelligence

        * OECD AI Principles

        * Toronto Declaration

??? Question "True or False: It is okay to use a GPT to write a research proposal on a topic you have no experience in?"

    Hint: Review ["Using AI Ethically"](#using-ai-ethically)

    ??? Failure "False"

        If you do not have the ability to verify output truthfully or accurately, it is not safe to use a GPT for research.
