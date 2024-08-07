---
layout: post
title: Laue-DIALS for Pink-Beam Crystallography
subtitle: New Preprint for Laue-DIALS Software
author: Rick A. Hewitt
usemathjax: true
---

### Introduction
Crystallography has often been limited to monochromatic light sources because of the complications a pink beam brings for data analysis. Some software, including tools like [PinkIndexer](https://journals.iucr.org/a/issues/2020/02/00/ae5078/index.html) and [Precognition](https://biocars.uchicago.edu/facilities/software/precognition-documentation/) have been used to analyze these data in the past, but here we present a new package called [Laue-DIALS](https://rs-station.github.io/laue-dials/), and you can find the recently published preprint [on bioRxiv](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1)! Polychromatic crystallography has characteristics that make it particularly apt for time-resolved experiments and can help to maximize signal with fewer images. It can also render partiality a non-issue by capturing full reflections on single still images. We hope that the use of the (free and open-source!) Laue-DIALS software will encourage and enable the use of polychromatic crystallography experiments.

{:image: style="margin-right: 25%;margin-left: 25%;width: 50%"}
{:caption: style="display: inline-block;padding: 0 15%;"}

![Reciprocal lattice points in the Laue case](/assets/posts/2024-08-07-laue-dials-preprint.md/laue_rlp.png){: image}
*Full reflections from Laue pink-beam crystallography vs monochromatic stills and rotations from [Hewitt et al](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1). [(CC-BY license)](https://creativecommons.org/licenses/by/4.0/)*{: caption}

Laue-DIALS is currently able to handle single-crystal fixed-target datasets, with development to extend to serial crystallography rapidly underway! Installing Laue-DIALS just requires a [DIALS installation](https://dials.github.io/installation.html) and then running `pip install laue-dials`. All of the analyses in the preprint were performed using `DIALS v3.17.0` and `Laue-DIALS v0.4`. 

### Quick Tutorial
Laue-DIALS has a variety of tutorial notebooks. Each analysis in the preprint was performed with a notebook that can be found [in the associated deposition on Zenodo](https://zenodo.org/records/12761162). A data download script is provided to download any desired raw data from [SBGrid](https://sbgrid.org) (simulated data is high-volume and available on request!). A routine data analysis pipeline is described by the following figure:

{:image: style="margin-right: 25%;margin-left: 25%;width: 50%"}
{:caption: style="display: inline-block;padding: 0 15%;"}

![Laue-DIALS Pipeline](/assets/posts/2024-08-07-laue-dials-preprint.md/laue-dials-pipeline.png){: image}
*Basic Laue-DIALS analysis pipeline from [Hewitt et al](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1). [(CC-BY license)](https://creativecommons.org/licenses/by/4.0/)*{: caption}

There are also useful command-line utilities like `laue.plot_wavelengths` and `laue.compute_rmsds`, which are particularly useful as benchmark tools for quality after geometric refinement. The full Laue-DIALS command-line interface is described with all arguments [in our online documentation](https://rs-station.github.io/laue-dials/cli/functions.html). The nature of these programs also make them easy to apply to several passes of data via bash scripting (as seen in the deposition tutorials). 

### Get Involved!
As we mentioned: Laue-DIALS is fully open source! We'd love to get your participation as a user, and even as a contributor. Any bug reports or feature requests can be made either on the [Laue-DIALS Github Issues page](https://github.com/rs-station/laue-dials/issues) or raised in the `laue-dials` channel on the [Reciprocal Space Station Slack Workspace](). You can get in contact with the developers either way, and we look forward to seeing you there! If you would like to contribute source code or documentation, you can find guidelines at our [online documentation](https://rs-station.github.io/laue-dials/contributing.html).
