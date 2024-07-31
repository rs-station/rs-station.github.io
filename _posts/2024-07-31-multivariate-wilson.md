---
layout: post
title: Multivariate Wilson Priors
subtitle: Pre-prints Demonstrate Multivariate Priors for Time-Resolved Crystallography
author: Kevin Dalton
usemathjax: true
---

<!-- CSS definitions for images -->
{:image: style="margin-right: 25%;margin-left: 25%;width: 50%"}
{:caption: style="display: inline-block;padding: 0 15%;"}

### Comparative Crystallography and Careless
In modern structural biology, we are often more interested in the small differences between related structures rather than the structures themselves. There are many applications of this concept in the domain of comparative crystallography. For instance, equilibrium biophysical perturbations such as multitemperature crystallography, non-equilibrium perturbations like electric-field or temperature jumps, drug fragment screening, and anomalous diffraction all fall under the umbrella of comparative crystallography. While comparative data have been successfully analyzed using conventional tools, the fidelity of experiments are often challenged by the magnitude of systematic errors present in diffraction data. These can be hundreds of times larger than the true structural differences. 

![Systematic errors in rotation data](/assets/posts/2024-08-01-multivariate-wilson/systematic_error.png){: image}
*Example of systematic errors in conventional diffraction data from [Dalton et al](https://doi.org/10.1038/s41467-022-35280-8). [(CC-BY license)](https://creativecommons.org/licenses/by/4.0/)*{: caption}


To address the problem of systematic errors in diffraction data, we built [careless](https://github.com/rs-station/careless), a flexible tool for merging reflection intensities. Careless uses modern concepts from machine learning like variational inference and deep learning to correct the systematic errors. In our original [publication](https://doi.org/10.1038/s41467-022-35280-8) we demonstrated that careless works well for one important application of comparative crystallography which is time-resolved diffraction. Specifically, we showed state of the art inference of time-resolved structural changes in photoactive yellow protein. This week, we're excited to announce a new feature which takes careless to the next level in the comparative crystallography setting. We shared our insights in a series of 3 closely related pre-prints. 

 1. [Sensitive Detection of Structural Differences using a Statistical Framework for Comparative Crystallography.](https://doi.org/10.1101/2024.07.22.604476)
 2. [Resolving DJ-1 Glyoxalase Catalysis Using Mix-and-Inject Serial Crystallography at a Synchrotron](https://doi.org/10.1101/2024.07.19.604369)
 3. [Scaling and Merging Time-Resolved Laue Data with Variational Inference](https://doi.org/10.1101/2024.07.30.605871)

### Multivariate Wilson Prior
In modern structural biology, we are often more interested in the small differences between related structures rather than the structures themselves. There are many applications of this concept in the domain of comparative crystallography. For instance, equilibrium biophysical perturbations such as multitemperature crystallography, non-equilibrium perturbations like electric-field or temperature jumps, drug fragment screening, and of course anomalous diffraction all fall under the umbrella of comparative crystallography. While comparative data have been successfully analyzed using conventional tools, the fidelity of experiments are often challenged by the magnitude of systematic errors present in diffraction data. These can be many hundreds of times larger than the true differences we seek. 

![Applications of the multivariate Wilson prior](/assets/posts/2024-08-01-multivariate-wilson/comparative_xtal_graphs.png){: image}
*Applications of the multivariate Wilson prior from [Hekstra et al.](https://doi.org/10.1101/2024.07.22.604476) [(CC-BY-NC license)](https://creativecommons.org/licenses/by-nc/4.0/)*{: caption}

Hekstra et al. (1) derive a mathematical formalism for comparative crystallography. The key insight in their approach is to add some structure into the Bayesian prior distribution used for merging data in careless. Specifically, the default implementation in careless treats related structures as statistically *independent*. By allowing users to specify that subsequent time-points should be statistically *dependent*, this work is able to tease much more signal out of diffraction data. Specific applications demonstrated in the manuscript include
 - polychromatic anomalous diffraction
 - time-resolved polychromatic diffraction
 - anomalous diffraction at an X-ray free electron laser (XFEL)
 - drug fragment screen

 In every case, the structured prior is able to increase the amount of signal observed in the data. 

### Time-resolved Diffraction of an Enzyme, DJ-1
Zielinski and Dolamore et al. (2) applied the Multivariate Wilson prior to DJ-1, an enzyme involved in Parkinson's disease. In this study, Lois Pollack's [team](https://pollack.research.engineering.cornell.edu/) from Cornell University developed sample mixers which allowed DJ-1 to be rapidly mixed with a substrate, methylglyoxal. Mark Wilson's [group](https://redoxbiologycenter.unl.edu/markwilsonphd) from University of Nebraska Lincoln grew the DJ-1 crystals which were recorded in in a time-resolved fashion at [BioCARS](https://biocars.uchicago.edu/), a polychromatic beamline at the Advanced Photon Source. This configuration allowed the collaborators  to observe the conversion of toxic methylgloxal into non-toxic lactate. The exceptional clarity of the time-resolved difference electron density maps produced by Careless enabled new insights into the catalytic mechanism of DJ-1 including an explanation of the enantio-purity of the products. 

![Stereo chemistry of DJ-1 Lactoyl-cysteine intermediate](/assets/posts/2024-08-01-multivariate-wilson/lc_intermediate.png){: image}
*The mechanism of enantioselective hydrolysis in DJ-1 catalysis as explained by [Zielinski and Dolamore et al.](https://doi.org/10.1101/2024.07.19.604369). Water can only access the Lactoylcysteine intermediate from the solvent-exposed face of the active site. [(CC-BY-NC-ND license)](https://creativecommons.org/licenses/by-nc-nd/4.0/)*{: caption}


![Long-range allostery in DJ-1](/assets/posts/2024-08-01-multivariate-wilson/dj1_allostery.png){: image}
*[Zielinski and Dolamore et al.](https://doi.org/10.1101/2024.07.19.604369) show evidence of long-range allostery between the active site and Cystein-53. [(CC-BY-NC-ND license)](https://creativecommons.org/licenses/by-nc-nd/4.0/)*{: caption}

### Variational Inference Best Practices
Finally, Zielinski et al (3), details the application of Careless to time-resolved data using DJ-1 as an example. This manuscript offers helpful guidance to users seeking to get the most of their time-resolved diffraction data. Furthermore, it contains a thorough ablation study which demonstrates the impact of many components of the model. 

![DJ-1 merging ablation study](/assets/posts/2024-08-01-multivariate-wilson/dj1_ablation_study.png){: style="width: 100%"}
*[Zielinski et al.](https://doi.org/10.1101/2024.07.30.605871) studied the importance of careless model components by conducting ablation studies. Among other important observations, they showed the multivariate Wilson prior accounts for a nearly 10 sigma increase in time-resolved difference signal. [(CC-BY-NC license)](https://creativecommons.org/licenses/by-nc/4.0/)*
