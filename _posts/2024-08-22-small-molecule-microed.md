---
layout: post
title: Merging Small Molecule MicroED Data
subtitle: Preprint Demonstrates using Careless in Small Molecule MicroED
author: Doris Mai
usemathjax: true
---

### Small Molecule MicroED
<!-- For decades, single-crystal X-ray diffraction (SCXRD) has been the gold standard for structure elucidation for small molecules.  -->
Microcrystal electron diffraction (MicroED), also known as continuous rotational electron diffraction (cRED), is an emerging technique for elucidating small molecule structures from micro- and nano-crystals. 
However, data processing in microED can be challenging and often requires **merging datasets from multiple crystals** due to limited rotation ranges in many transmission electron microscopes (TEMs) and higher noises in intensity measurements than conventional X-ray diffraction (XRD) experiments. 
A common practice in the field is to manually curate datasets and apply scaling programs such as [XDS/XSCALE](https://doi.org/10.1107/S0907444909047337) from rotational XRD, but this could be time-consuming and risks introducing human bias. In this [preprint](https://doi.org/10.26434/chemrxiv-2024-62bmk), we demonstrate that [Careless](https://github.com/rs-station/careless) could be used for merging small molecule microED data and investigate the impact of dataset curation.

### Dataset Curation in Merging
We benchmark Careless with XDS/XSCALE on more than 10 cases of multi-crystal merging and compare the performances between using all datasets and manually curated datasets (curated=True). 
We also explore an extension to Careless ([MC-Careless](https://github.com/DorisMai/careless/tree/multi_xtal_sig)) to automate the curation of datasets. Specifically, an optimal weighting among datasets ($$w$$) is learned jointly with the scaling factors ($$K$$) and structure factor amplitudes ($$F$$). 
This weight modulates the effective uncertainty of the intensities ($$\sigma_I$$) from different crystals to account for the variability of data quality across datasets.

![Schematic of weighting](/assets/posts/2024-08-22-small-molecule-microed/mc-careless-schematic.png){: .blog-image} 
Schematic from the [preprint](https://doi.org/10.26434/chemrxiv-2024-62bmk) of the multi-crystal weighting extension to Careless. [(CC-BY-NC-ND license)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
{: .blog-caption}

In the presented cases, Careless benefits from using all available data, and our multi-crystal weighting extension did not further improve the performance. Manual curation of datasets affects the $$CC_{1/2}$$ in XDS/XSCALE and Careless but has marginal impact on the accuracy with respect to structure factor amplitudes calculated from reference structures and on *ab initio* phasing outcomes. 

![Initial map](/assets/posts/2024-08-22-small-molecule-microed/preliminary-maps.png){: .blog-image} 
Examples from the [preprint](https://doi.org/10.26434/chemrxiv-2024-62bmk) of *ab initio* phasing outcomes from different merging protocols. [(CC-BY-NC-ND license)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
{: .blog-caption}

### Key points and Future Directions
- Careless can merge microED and small molecule crystallography data.
- The variational inference framework implemented in Careless is flexible for methods development as experimented in our [MC-Careless](https://github.com/DorisMai/careless/tree/multi_xtal_sig).
- Additional exploration of the hyperparamter space and the Wilson prior might be helpful for challeging cases with pathologies.
- The common practice of manual dataset curation should be cautioned and deserves future investigation.