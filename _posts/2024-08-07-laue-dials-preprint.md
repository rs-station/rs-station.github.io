---
layout: post
title: Laue-DIALS for Pink-Beam Crystallography
subtitle: New Preprint for Laue-DIALS Software
author: Rick A. Hewitt
---

### Introduction
Crystallography has often been limited to monochromatic light sources because of the complications a pink beam brings for data analysis. While some software, including [PinkIndexer](https://journals.iucr.org/a/issues/2020/02/00/ae5078/index.html), [Precognition](https://biocars.uchicago.edu/facilities/software/precognition-documentation/), and the [Daresbury Laue Suite](https://doi.org/10.1107/S1600577521001326) can be used to analyze these data, we are lacking a modern, open-source package for polychromatic data analysis. Here we present a new package called [Laue-DIALS](https://rs-station.github.io/laue-dials/) which fills this gap. Polychromatic crystallography has characteristics that make it particularly apt for time-resolved experiments and can help to maximize signal with fewer images. It can also render partiality a non-issue by capturing full reflections on single still images. We hope that the use of the (free and open-source!) Laue-DIALS software will encourage and enable the use of polychromatic crystallography experiments. You can find the recently published preprint [on bioRxiv](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1)!

![Reciprocal lattice points in the Laue case](/assets/posts/2024-08-07-laue-dials-preprint.md/laue_rlp.png){: .blog-image-wide}
*Full reflections from Laue pink-beam crystallography vs monochromatic stills and rotations from [Hewitt et al](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1). [(CC-BY-NC license)](https://creativecommons.org/licenses/by/4.0/)*{: .blog-caption}

Laue-DIALS is currently able to handle single-crystal fixed-target datasets, with development to extend to serial crystallography rapidly underway! Laue-DIALS can be installed using `pip` after [installing the DIALS diffraction analysis package](https://dials.github.io/installation.html).

### Quick Tutorial
Laue-DIALS has a variety of tutorial notebooks. Each analysis in the preprint was performed with a notebook that can be found [in the associated deposition on Zenodo](https://zenodo.org/records/12761162). Experimental data are available from [SBGrid](https://sbgrid.org). A routine data analysis pipeline is described by the following figure:

![Laue-DIALS Pipeline](/assets/posts/2024-08-07-laue-dials-preprint.md/laue-dials-pipeline.png){: .blog-image-narrow}
*Basic Laue-DIALS analysis pipeline from [Hewitt et al](https://www.biorxiv.org/content/10.1101/2024.07.23.604358v1). [(CC-BY-NC license)](https://creativecommons.org/licenses/by/4.0/)*{: .blog-caption}

There are also useful command-line utilities like `laue.plot_wavelengths` and `laue.compute_rmsds`, which are particularly useful as benchmark tools for quality after geometric refinement. The full Laue-DIALS command-line interface is described with all arguments [in our online documentation](https://rs-station.github.io/laue-dials/cli/functions.html). The nature of these programs also make them easy to apply to several passes of data via bash scripting (as seen in the deposition tutorials). 

### Get Involved!
As we mentioned: Laue-DIALS is fully open source! We'd love to get your participation as a user, and even as a contributor. Any bug reports or feature requests can be made on the [Laue-DIALS Github Issues page](https://github.com/rs-station/laue-dials/issues). We look forward to seeing you there! If you would like to contribute source code or documentation, you can find guidelines at our [online documentation](https://rs-station.github.io/laue-dials/contributing.html).
