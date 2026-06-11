# Environmental & Health Impacts of AI

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Every prompt has a physical footprint. The chatbots, copilots, and image generators that feel weightless on screen run on warehouse-scale **data centers** — buildings packed with power-hungry chips that have to be manufactured, powered, and cooled around the clock. As the AI build-out accelerates, the bill is coming due in two currencies: the **natural environment** (electricity, water, land, and materials) and **human health** (the air pollution, heat, and disruption borne by the communities living next to the infrastructure).

This lesson surveys both — and the trade-offs every AI user and institution should weigh.

!!! Abstract "The short version"

    - AI is driving the **fastest surge in electricity demand in a generation**: global data-center power use is projected to **more than double to ~945 TWh by 2030** — roughly **3% of the world's electricity**, about what Japan consumes today.
    - Meeting that demand is **delaying the retirement of coal and gas plants**, spurring a wave of new gas turbines, and reopening nuclear reactors — while Big Tech's own emissions **rise** despite net-zero pledges.
    - Data centers **consume water** — directly for cooling and indirectly through the power plants feeding them — increasingly in **drought-stressed regions**.
    - The pollution carries a measurable **human toll**: U.S. data-center air pollution is projected to cause on the order of **1,300 premature deaths and ~\$20 billion in health damages per year by 2030**, concentrated in the low-income and minority communities sited next to the turbines.

## A footprint you can't see on screen

The mental model that AI is "just software" hides a heavy industrial reality. Behind every model are three physical demands that grow with use:

- **Compute** — racks of GPUs/TPUs that must be **manufactured** (mining, chip fabrication) and eventually **discarded**.
- **Energy** — electricity to run the chips, around the clock, at very high power density.
- **Cooling** — water and/or still more electricity to carry away the heat those chips produce.

Training a frontier model is expensive, but the larger and growing cost is **inference** — answering billions of everyday queries. A single AI-generated answer can use [several times the energy of a traditional web search](https://www.iea.org/reports/energy-and-ai){target=_blank}, and that small per-query cost multiplies across billions of prompts a day.

## Energy demand and the grid

### How much electricity?

The International Energy Agency's [*Energy and AI*](https://www.iea.org/reports/energy-and-ai){target=_blank} report projects that global **data-center electricity use will reach about 945 TWh by 2030** — roughly **3% of all electricity worldwide** and more than double 2024 levels.

- Data-center demand grows about **15% per year** through 2030 — **four times faster** than total electricity demand from every other sector combined.
- The growth is **AI-specific**: electricity for "accelerated servers" (the GPU clusters that run AI) climbs ~**30% per year**.
- In the **United States** alone, data centers add about **240 TWh** by 2030 (a **130% increase**).
- In the IEA's higher-growth scenario, global data-center demand exceeds **1,700 TWh by 2035** (~4.4% of world electricity).

### Where that power comes from — and who pays

A demand spike this fast outruns the clean-energy build-out, with knock-on effects:

- **Fossil lock-in.** Utilities are **postponing the retirement of coal and gas plants** and fast-tracking new **gas turbines** to serve data-center load — slowing, not speeding, the energy transition.
- **A nuclear scramble.** Tech firms are signing deals to reopen reactors (Microsoft and Constellation's **Three Mile Island** restart) and to build **small modular reactors** (Google–Kairos, Amazon, Meta) — but new nuclear arrives slowly and won't cover near-term demand.
- **Rising emissions.** Despite net-zero pledges, the largest AI firms report **growing** greenhouse-gas emissions — Google's were up roughly **48%** and Microsoft's nearly **30%** against their baselines as the build-out accelerated.
- **Cost-shifting onto households.** Grid upgrades and generating capacity to serve hyperscale campuses can **raise electricity bills for ordinary ratepayers**, who effectively subsidize the build-out.

!!! Warning "The efficiency paradox"
    Chips and data centers keep getting more efficient *per computation* — but demand is growing faster than efficiency, so **total** energy use keeps climbing. The savings are spent on **doing much more AI**, not on using less power: a classic [Jevons paradox](https://en.wikipedia.org/wiki/Jevons_paradox){target=_blank}.

## Impacts on the natural environment

### Water

Data centers are **thirsty**. They consume fresh water two ways: **directly**, through evaporative cooling that boils off water to shed heat, and **indirectly**, through the water-cooled power plants that supply their electricity (often **80% or more** of the total). The UC Riverside study [*Making AI Less "Thirsty"*](https://arxiv.org/abs/2304.03271){target=_blank} estimated that:

- A short ChatGPT exchange of **10–50 questions** can consume roughly **500 ml of water** (a 16-oz bottle) once cooling and the regional power mix are counted.
- Training **GPT-3** in U.S. data centers consumed on the order of **5.4 million liters** of water.

The deeper problem is **where** this happens: hyperscale campuses are frequently sited in **hot, water-stressed regions** (the U.S. Southwest, Chile, Spain), putting them in direct competition with farms and households for scarce fresh water.

### Land, materials, and electronic waste

- **Construction & land.** Each campus is a large industrial footprint — concrete, steel, and graded land (with embodied carbon and habitat loss) plus substations and transmission corridors.
- **Materials.** The chips depend on **mined** silicon, copper, and rare-earth elements and on water- and energy-intensive **semiconductor fabrication**.
- **E-waste.** AI hardware is replaced on a fast cycle. A 2024 *Nature Computational Science* analysis, [*Modeling the increase of electronic waste due to generative AI*](https://www.nature.com/articles/s43588-024-00726-0){target=_blank}, estimated generative AI could add a cumulative **1.2–5.0 million tonnes of e-waste between 2020 and 2030** — much of it laden with lead and other toxics — though circular-economy strategies could cut that by **16–86%**.

## Impacts on human health

The costs above are not abstract — they land on **human bodies**, and not evenly.

### Air pollution and its body count

To meet deadlines and bridge grid shortfalls, data centers lean on **on-site fossil generation**: diesel **backup generators** and, increasingly, **gas turbines**. These emit fine particulate matter (**PM2.5**), nitrogen oxides (**NOₓ**), and sulfur dioxide — pollutants linked to asthma, heart disease, lung cancer, and premature death. The 2024 UC Riverside–Caltech report [*The Unpaid Toll*](https://arxiv.org/abs/2412.06288){target=_blank} quantified the U.S. health burden using EPA methods:

- Approximately **1,300 premature deaths per year by 2030**.
- About **600,000 asthma-symptom cases**.
- Total public-health costs approaching **~\$20 billion per year** — a hidden subsidy paid in clinic visits, missed school, and lost lives.

### Environmental justice: who lives next to the turbines

Pollution and water stress are **disproportionately sited** in low-income communities and communities of color — the same environmental-justice pattern as older heavy industry.

!!! Danger "Case study — xAI's *Colossus*, Memphis"

    Elon Musk's **xAI** powered its **Colossus** supercomputer in **Boxtown**, a historically Black neighborhood of South Memphis, by running a fleet of **methane gas turbines** — for a time **without the required Clean Air Act permits**. As the build-out expanded toward a second site in **Southaven, Mississippi**, residents and regulators counted **dozens of unpermitted turbines** capable of emitting on the order of **2,500 tons of NOₓ a year** — likely the **single largest industrial source of smog-forming pollution in greater Memphis**, an area that already fails federal smog standards.

    In 2026 the **NAACP**, represented by [**Earthjustice**](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus){target=_blank} and the [Southern Environmental Law Center](https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/){target=_blank}, sued xAI for Clean Air Act violations — seeking to halt the unpermitted turbines and force best-available pollution controls. It is among the first major legal tests of who bears the health cost of the AI build-out.

### Heat, noise, and local stress

Beyond air and water, neighbors of a large data center contend with the **constant low-frequency hum** of cooling systems and generators, **waste heat**, and **competition for local water and grid capacity** — quality-of-life and health stressors that rarely appear in a model's "cost."

## What responsible use looks like

The footprint is real, but it is not a reason to abandon AI — it is a reason to use it **deliberately** and to demand accountability.

- **Right-size the model.** Use the **smallest model that does the job**; reserve frontier models for tasks that need them. Don't fire off a giant model for a one-line answer.
- **Batch and reuse.** Cache and reuse results; avoid needless re-runs and "let me regenerate that ten more times" habits.
- **Favor accountable providers.** Prefer vendors that **disclose** energy, water, and carbon per workload and that **match clean energy** on the same grid and hour — not just buy distant offsets.
- **Ask where the campus is.** Support siting that uses **recycled/non-potable water and closed-loop cooling**, avoids water-stressed basins, and does not concentrate pollution in already-overburdened communities.
- **Push for transparency and regulation.** Disclosure standards, honest accounting, and real permitting — rather than the [fast-tracked federal permitting carve-outs for data centers](legal.md#current-legislation) — are what turn "use a smaller model" from a personal gesture into structural change.

!!! Question "Is 'use a smaller model when you can' enough?"
    A recurring debate in AI ethics: is individual restraint a meaningful environmental ethic, or a **personal-virtue dodge** that lets the system off the hook — the AI equivalent of "use less plastic"? Both can be true. Personal choices matter at the margin; **disclosure, clean-energy siting, and enforceable permits** are what move the needle at scale.

## Further reading

- [IEA — *Energy and AI*](https://www.iea.org/reports/energy-and-ai){target=_blank} — the authoritative global outlook on AI electricity demand.
- [*The Unpaid Toll*: Quantifying the Public Health Impact of Data Centers](https://arxiv.org/abs/2412.06288){target=_blank} (UC Riverside & Caltech, 2024).
- [*Making AI Less "Thirsty"*](https://arxiv.org/abs/2304.03271){target=_blank} — AI's water footprint (UC Riverside, 2023).
- [*Modeling the increase of electronic waste due to generative AI*](https://www.nature.com/articles/s43588-024-00726-0){target=_blank} (*Nature Computational Science*, 2024).
- [Earthjustice — NAACP v. xAI](https://earthjustice.org/case/xai-illegal-gas-power-plant-data-center-colossus){target=_blank} — the Memphis Clean Air Act case.

## Assessment

??? Question "Name the two ways a data center consumes water, and which is usually larger."
    ??? Success "On-site cooling vs. the power supply"
        **Direct** (on-site evaporative cooling) and **indirect** (water used by the power plants generating its electricity). The **indirect** share is usually larger — often **80% or more** of total water use — so a data center's water footprint depends heavily on how clean and water-efficient its **grid** is.

??? Question "Why is the health burden of AI data centers an environmental-justice issue, not just an environmental one?"
    ??? Success
        The **gas turbines and diesel generators** that bridge grid shortfalls emit PM2.5 and NOₓ, and these facilities are **disproportionately sited in low-income communities and communities of color** (e.g., xAI's turbines in Boxtown, South Memphis). Those neighbors breathe the pollution and bear the asthma, heart-disease, and premature-death costs, while the benefits of the compute accrue elsewhere.

??? Question "True or False: because chips keep getting more efficient, AI's total energy use is falling."
    ??? Failure "False"
        Efficiency *per computation* is improving, but **total** demand is rising faster because we keep doing far more AI — a **Jevons paradox**. The IEA projects data-center electricity use to **more than double by 2030**.

## Related lessons

## [:material-scale-balance: Ethical & Legal Considerations](legal.md)

## [:material-brain: Ethics of AI](ethics.md)
