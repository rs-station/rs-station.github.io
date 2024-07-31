---
layout: post
title: Multivariate Wilson Priors
subtitle: New Pre-prints Demonstrate Multivariate Priors for Time-Resolved Crystallography
author: Kevin Dalton
usemathjax: true
---

### Careless
Diffraction data are heavily contaminated with systematic errors which frustrates the inference of time-resolved changes. To address this problem, we built [careless](https://github.com/rs-station/careless), a flexible tool for merging diffraction data which supports both monochromatic and Laue (polychromatic) time-resolved measurements. Careless uses modern concepts from machine learning such as variational inference and deep learning to correct the systematic errors which can be much larger than time-resolved changes. In the original [publication](https://doi.org/10.1038/s41467-022-35280-8) we demonstrated that careless works well for time-resolved Laue diffraction data collected at the Advanced Photon Source. This week, we're excited to announce a new feature which takes careless to the next level in this application domain. 

 1) [Sensitive Detection of Structural Differences using a Statistical Framework for Comparative Crystallography.](https://doi.org/10.1101/2024.07.22.604476)
 2) [Resolving DJ-1 Glyoxalase Catalysis Using Mix-and-Inject Serial Crystallography at a Synchrotron](https://doi.org/10.1101/2024.07.19.604369)
 3) [Scaling and Merging Time-Resolved Laue Data with Variational Inference](https://doi.org/???????/?????????????????)

### Multivariate Wilson Prior
In modern structural biology, we are often more interested in the small differences between related structures rather than the structures themselves. There are many applications of this concept in the domain of comparative crystallography. For instance, equilibrium biophysical perturbations such as multitemperature crystallography, non-equilibrium perturbations like electric-field or temperature jumps, drug fragment screening, and of course anomalous diffraction all fall under the umbrella of comparative crystallography. While comparative data have been successfully analyzed using conventional tools, the fidelity of experiments are often challenged by the magnitude of systematic errors present in diffraction data. These can be many hundreds of times larger than the true differences we seek. 

In Reference 1, Hekstra et al. derive a mathematical formalism for comparative crystallography. The key insight in their approach is to add some structure into the Bayesian prior distribution used for merging data in careless. Specifically, the default implementation in careless treats related structures as statistically __independent__. By allowing users to specify that subsequent time-points should be statistically related, this work is able to tease much more signal out of diffraction data. Specific applications demonstrated in the manuscript

### Time-resolved Diffraction of an Enzyme, DJ-1
