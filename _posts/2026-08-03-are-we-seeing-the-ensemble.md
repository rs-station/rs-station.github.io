---
layout: post
title: Fitting ensembles from cryoEM data, an exciting – and tricky! – frontier
subtitle: How structural biology experiments preserve, blur, or lose molecular ensembles
author: Minhuan Li, F. Emil Thomasen, Pilar Cossio
contact: "{minhuanli,fthomasen,pcossio}@flatironinstitute.org"
usemathjax: true
---

![Two ways an experiment can encode a conformational ensemble]({{ '/assets/posts/2026-08-03-are-we-seeing-the-ensemble/measurement_types.png' | relative_url }}){: .blog-image-hero}
Two ways in which an experiment can encode a conformational ensemble. Ensemble-averaged measurements combine contributions from many molecules into each observable. In single-particle or single-molecule measurements, each observation arises from an individual molecule, and the ensemble is represented statistically across many observations.
{: .blog-caption-wide}

Ensemble-inference approaches are rapidly becoming a research frontier across structural biology. The prospect of visualizing not only a single snapshot, but the structural fluctuations biomolecules make as they function, is one of the most exciting steps forward structural biology is poised to make.

But asking a biophysical experiment for a distribution has some fundamental differences from asking it for a structure. Here we discuss a few of the challenges involved, and potential solutions, with single-particle cryoEM as our focus. The topics discussed, however, cut across structural biology and are not intrinsically unique to cryoEM.
{: .post-lead}

### Biomolecules as thermodynamic ensembles

Many structural models represent a biomolecule with a single set of coordinates. To perform their biological function, however, biomolecules populate a range of conformations: pockets deform to bind ligands, ion channels transition between open and closed states, and viral spike proteins  undergo large-scale openings to infect host cells. Can we image these important and interesting motions, capturing them in the form of an ensemble?

An ensemble is more than the observation that molecules move. It describes both which conformations are accessible and how frequently they occur – a probability distribution. In the familiar language of thermodynamics, we say that for a given temperature $$T$$, the equilibrium ensemble is given by Boltzmann's distribution,

$$
p_{\mathrm{th}}(x) = \frac{1}{Z}\exp\!\left(-\frac{E(x)}{k_B T}\right),
\tag{1}
$$

where $$x$$ is a molecular conformation, $$E(x)$$ is its potential energy, $$k_B$$ is Boltzmann's constant and $$Z$$ is the partition function (a normalizing factor). Knowing $$p_{\mathrm{th}}(x)$$ is just the probability that we encouter any conformation $$x$$, including rare or transition states. Together with an appropriate forward model, it would also allow us to predict any measurement of the system when it's at equilibrium.

When the distribution is skewed so that one conformation is overwhelmingly more likely than the others, a single deposited structure might be a useful summary of this landscape. But questions about molecular flexibility can only be addressed with the ensemble distribution: how populated is an alternative conformation? How often does a cryptic pocket open? Which states are stabilized by a drug? Which motions disappear after a mutation? 

For these questions, we leave structure determination behind and enter the land of ensemble inference – and a few things can go awry!

### Experimental design dictates the ensemble

First, while we might care about the protein in one particular condition – perhaps a buffer that mimics the cytosol held at 37 $^{\circ}$C – experimental realities might mean the protein sample needs to be prepared under different conditions. For example, cryoEM requires the samples to be flash frozen! 

Accordingly, the Boltzmann distribution we want to measure might not correspond to the *source distribution*, $$p_{\mathrm{src}}$$, present in the prepared sample under the conditions of measurement. 

Sample purity, temperature, chemical environment, and the fact the molecules might not be in equilibrium – but, like in cryoEM, trapped in a glass! – can all separate this distribution from an ensemble we actually wish to study.

This gap applies to every modality, not only to cryo-EM. Ensemble inference therefore has two layers: recovering $$p_{\mathrm{src}}$$ from the data, and deciding how faithfully $$p_{\mathrm{src}}$$ represents $$p_{\mathrm{th}}$$. 

**TJ comment.** You don't discuss the implications. What should you do if you have a different distribution from the one you care about? At least you should think through the exprimental design. It also could be possible -- in certain ideal situations -- to reweight the source to a different distribution you care more about. Elaborate.


## Averaged data _can_ yield meaningful ensembles... but not always

Proteins are small and radiation-sensitive: they can only produce blurry pictures. Historically, structural biology experiments have gotten around this and achieved high-resolution by averaging signals over many proteins: from all the proteins in a crystal, from many classified cryoEM particles, the plethora in an NMR tube, _etc._.

For an ensemble-average measurement, we can write a simple model of the data,

$$
y_i = \int m_i(x)\,p_{\mathrm{src}}(x)\,dx + \varepsilon_i,
\tag{2}
$$

where $$m_i(x)$$ is the forward model for observable $$i$$ and $$\varepsilon_i$$ is measurement noise. The experiment does not hand us individual conformations; it hands us a weighted average of the observable over the source distribution. How much ensemble information survives depends on what was averaged, how many independent constraints remain, and at what spatial resolution they were measured.

Averaging an observable is not the same as measuring the average structure. For two conformations $$A$$ and $$B$$, with source probabilities $$p^A_{\mathrm{src}}$$ and $$p^B_{\mathrm{src}}$$, respectively, what is measured is $$p^A_{\mathrm{src}}\,m(x_A) + p^B_{\mathrm{src}}\,m(x_B)$$, not $$m(p^A_{\mathrm{src}} x_A + p^B_{\mathrm{src}} x_B)$$. When the observable is close to linear in structural space, two spatially separated conformations can leave two separable traces rather than one fictitious midpoint. Averaged data can still contain ensemble information; the question is how much of it remains distinguishable.

## Single-molecule experiments provide a more direct access to an ensemble

**TO DO Introduction.**

Single-molecule experiments come in more than one form. Some follow the same molecule over time. In single-molecule FRET, for example, a time trace may be divided into coarse conformational states and used to estimate transitions; under stationary conditions, the distribution of that model estimates their populations. Such trajectories contain kinetic information as well as population information.

Cryo-EM preserves molecular individuality without preserving time. Each particle contributes a single noisy projection of one conformation, so the ensemble must be inferred from variation across many images rather than from transitions within a trajectory. Despite this difference, both experiments can be described as noisy observations of latent molecular states:

$$
\begin{aligned}
x_n &\sim p_{\mathrm{src}}(x), \\
z_n &\sim \pi(z), \\
y_n &\sim K(\,\cdot\mid x_n, z_n),
\end{aligned}
\tag{3}
$$

where $$x_n$$ is the molecular state, $$z_n$$ collects nuisance variables, and $$K$$ is the measurement kernel relating a latent state to an observation. For a trajectory experiment, this is only the marginal observation model; a complete description must also specify how states evolve in time. In cryo-EM, the index $$n$$ instead runs over different particles, while $$z_n$$ includes projection direction, translation, and microscope effects.

For independent snapshots — or for the marginal observation at one time point — the distribution of observations is

$$
q(y) = \iint K(y \mid x, z)\,\pi(z)\,p_{\mathrm{src}}(x)\,dz\,dx.
\tag{4}
$$

Unlike Equation (2), this distribution retains molecule-to-molecule variation rather than reducing it immediately to selected averages. Yet recovering $$p_{\mathrm{src}}$$ from $$q(y)$$ remains an inverse problem. In cryo-EM, low contrast, unknown poses, microscope effects, and the high dimensionality of conformational variation can make that problem extremely difficult. Molecule-resolved does not mean easily recoverable, just as ensemble-averaged does not mean devoid of ensemble information. The two measurement routes therefore lose information differently. To compare them, we need to ask how different two source distributions must be before an experiment can distinguish them.

### Ensemble resolution

We call this limit *ensemble resolution*. Just as spatial resolution asks when nearby features blur together, ensemble resolution asks when distinct source distributions become experimentally indistinguishable. More precisely, two distributions cannot be distinguished when, after passing through the measurement process, they produce observables that agree within the uncertainty of the data.

An experiment can therefore contain ensemble information and still have low ensemble resolution. It may distinguish open from closed but not resolve a continuum between them, detect a rare state but not determine its occupancy, or report a broad fluctuation without identifying the correlated motions that produced it. For averaged measurements, the limit is set by the number and spatial specificity of the independent constraints. For molecule-resolved measurements, it is set by how well different latent states remain distinguishable through noise, nuisance variables, finite sampling, and the inference model. In cryo-EM, this criterion exposes a second distinction: particle images and reconstructed maps sit at different stages of information loss.

### Cryo-EM: two targets, structure or ensemble?

The crucial change occurs during reconstruction. Particle images that began as separate molecular observations are picked, curated, aligned, classified, masked, and averaged into a three-dimensional map. This processing is essential for high-resolution structure determination, but it also changes the inferential target.

A reconstructed map can be an excellent structural target. It may define a selected conformational state with impressive detail, and local heterogeneity can still appear as weak or diffuse density. But the map is not itself a molecule-resolved sample from $$p_{\mathrm{src}}$$. It is a derived estimate conditioned on which particles were selected, how they were aligned and classified, and what priors entered the reconstruction. If a rare state was removed upstream, or continuous variation was forced into a small number of classes, no analysis of the resulting map can restore that lost population information.

For questions about the distribution represented by the collected particles, particle-level data are therefore the more natural starting point. They retain the variation across individual observations before it is collapsed into a consensus reconstruction. This does not make image-level ensemble inference easy: an algorithm must separate conformational variation from pose, microscope effects, noise, and finite sampling, often through a low-dimensional representation of molecular motion.

Cryo-EM therefore makes the central diagnostic concrete: before asking whether an inference method is powerful enough, ask whether its target still contains the distributional information of interest. Consensus maps are appropriate targets when the goal is a detailed structure. When the goal is to infer the distribution represented by the collected particles, however, a consensus map alone is not enough; inference should begin from particle-level data. In future pieces, we will apply the same framework to other modalities: what did the experiment preserve, what did it compress, and what did the analysis pipeline discard?

### Further reading

For readers who want the technical background, the short bibliography below points to work on structural ensemble determination, the limits of averaged data, cryo-EM heterogeneity, Bayesian reconstruction, and image-level ensemble inference.

 1. Bonomi et al. *Principles of protein structural ensemble determination*. Current Opinion in Structural Biology, 2017.
 2. Ravera et al. *A critical assessment of methods to recover information from averaged data*. Physical Chemistry Chemical Physics, 2016.
 3. Tang et al. *Conformational heterogeneity and probability distributions from single-particle cryo-electron microscopy*. Current Opinion in Structural Biology, 2023.
 4. Scheres. *A Bayesian view on cryo-EM structure determination*. Journal of Molecular Biology, 2012.
 5. Sánchez-Espinosa et al. *Cryo-EM as a stochastic inverse problem*. arXiv, 2025.
 6. Clark et al. *Cooling fast and slow: Characterising the effects of vitrification in cryo-EM and the subsequent recovery of equilibrium populations*. bioRxiv, 2026.
