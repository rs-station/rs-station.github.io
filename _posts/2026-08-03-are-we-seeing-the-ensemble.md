---
layout: post
title: Fitting ensembles from cryo-EM data, an exciting – and tricky! – frontier
subtitle: How structural biology experiments preserve, blur, or lose molecular ensembles
author: Minhuan Li, F. Emil Thomasen, Pilar Cossio
contact: "{minhuanli,fthomasen,pcossio}@flatironinstitute.org"
usemathjax: true
---

![Two ways an experiment can encode a conformational ensemble]({{ '/assets/posts/2026-08-03-are-we-seeing-the-ensemble/measurement_types.png' | relative_url }}){: .blog-image-hero}
Two ways in which an experiment can encode a conformational ensemble. Ensemble-averaged measurements combine contributions from many molecules into each observable. In single-particle or single-molecule measurements, each observation arises from an individual molecule, and the ensemble is represented statistically across many observations.
{: .blog-caption-wide}

Ensemble-inference approaches are rapidly becoming a research frontier across structural biology. The prospect of visualizing not only a single snapshot, but the structural fluctuations biomolecules make as they function, is one of the most exciting steps forward structural biology is poised to make.

But asking a biophysical experiment for a distribution has some fundamental differences from asking it for a structure. Here we discuss a few of the challenges involved, and potential solutions, with single-particle cryo-EM as our focus. The topics discussed, however, cut across structural biology and are not intrinsically unique to cryo-EM.
{: .post-lead}

### Biomolecules as thermodynamic ensembles

Many structural models represent a biomolecule with a single set of coordinates. To perform their biological function, however, biomolecules populate a range of conformations: pockets deform to bind ligands, ion channels transition between open and closed states, and viral spike proteins undergo large-scale openings to infect host cells. Can we image these important and interesting motions, capturing them in the form of an ensemble?

An ensemble is more than the observation that molecules move. It describes both which conformations are accessible and how frequently they occur – a probability distribution. In the familiar language of thermodynamics, we say that for a given temperature $$T$$, the equilibrium ensemble is given by Boltzmann's distribution,

$$
p_{\mathrm{th}}(x) = \frac{1}{Z}\exp\!\left(-\frac{E(x)}{k_B T}\right),
\tag{1}
$$

where $$x$$ is a molecular conformation, $$E(x)$$ is its potential energy, $$k_B$$ is Boltzmann's constant and $$Z$$ is the partition function (a normalizing factor). $$p_{\mathrm{th}}(x)$$ is just the probability that we encounter any conformation $$x$$, including rare or transition states. Together with an appropriate forward model, knowing this distribution would also allow us to predict any measurement of the system at equilibrium.

When the distribution is skewed so that one conformation is overwhelmingly more likely than the others, a single deposited structure might be a useful summary of this landscape. But questions about molecular flexibility can only be addressed with the ensemble distribution: how populated is an alternative conformation? How often does a cryptic pocket open? Which states are stabilized by a drug? Which motions disappear after a mutation?

For these questions, we leave structure determination behind and enter the land of ensemble inference – and a few things can go awry!

### Experimental design dictates the ensemble

First, while we might care about the protein in one particular condition – perhaps a buffer that mimics the cytosol held at 37 °C – experimental realities might mean the protein sample needs to be prepared under different conditions. For example, cryo-EM requires the samples to be flash-frozen!

Accordingly, the Boltzmann distribution we want to measure might not correspond to the *source distribution*, $$p_{\mathrm{src}}$$, present in the prepared sample under the conditions of measurement.

Sample purity, temperature, chemical environment, and the fact that the molecules might not be in equilibrium – but, like in cryo-EM, trapped in a glass! – can all separate this distribution from the ensemble we actually wish to study.

This gap applies to every modality, not only to cryo-EM. Ensemble inference therefore has two layers: recovering $$p_{\mathrm{src}}$$ from the data, and deciding how faithfully $$p_{\mathrm{src}}$$ represents $$p_{\mathrm{th}}$$.

**TJ comment.** You don't discuss the implications. What should you do if you have a different distribution from the one you care about? At least you should think through the exprimental design. It also could be possible -- in certain ideal situations -- to reweight the source to a different distribution you care more about. Elaborate.

### Averaged data _can_ yield meaningful ensembles

Proteins are small and radiation-sensitive, meaning that in X-ray, cryo-EM, and NMR experiments, each individual molecule produces a signal that is too weak to yield an atomically resolved structure. Historically, structural biology experiments have gotten around this and achieved high resolution by averaging signals over many proteins: from all the proteins in a crystal, from many classified cryo-EM particles, the ensemble in an NMR tube, _etc._

We can write a simple model of that averaging process,

$$
y_i = \int m_i(x)\,p_{\mathrm{src}}(x)\,dx + \varepsilon_i,
\tag{2}
$$

where $$m_i(x)$$ is the forward model for observable $$i$$ and $$\varepsilon_i$$ is measurement noise. In words, the experiment produces data that are a weighted average of the observable over the source distribution. How much ensemble information survives depends on (i) that source distribution, (ii) how many independent constraints remain, and (iii) at what spatial resolution they were measured.

Importantly, the averaged experimental observable is not the same as the average coordinate structure. One way to see this clearly is to consider the simplest possible ensemble: there are only two discrete conformations $$A$$ and $$B$$, with source probabilities $$p^A_{\mathrm{src}}$$ and $$p^B_{\mathrm{src}}$$, respectively. Experimentally, one observes $$p^A_{\mathrm{src}}\,m(x_A) + p^B_{\mathrm{src}}\,m(x_B)$$, not $$m(p^A_{\mathrm{src}} x_A + p^B_{\mathrm{src}} x_B)$$. This also makes it clear that when the forward model is close to linear in structural space, two spatially distinct conformations can produce a superposition that is interpretable as two separate structures: alternative conformations of sidechains, which often show well-separated features in electron density and electrostatic potential maps, are a familiar example. On the other hand, highly overlapping structural features, such as subtle backbone motions, are often challenging to disentangle and interpret as separate, discrete coordinate models. Thus, averaged data _can_ still contain ensemble information; the question is how much of it remains distinguishable – and that is protein- and experiment-specific.

### Single-molecule experiments provide a more direct, but still lossy, view of an ensemble

Amongst the commonly used tools in structural biology, cryo-EM is unique in that the raw data provide atomically resolved images of individual, single molecules. While averaging to boost signal-to-noise is standard in cryo-EM single particle analysis, that averaging is done computationally, not experimentally. Each particle averaged is a sample from $$p_{\mathrm{src}}$$, which enables a much more powerful approach to recovering that source distribution.

Mathematically, each particle contributes a single noisy projection of one conformation:

$$
\begin{aligned}
x_n &\sim p_{\mathrm{src}}(x), \\
z_n &\sim \pi(z), \\
y_n &\sim K(\,\cdot\mid x_n, z_n),
\end{aligned}
\tag{3}
$$

Generically, for any single-particle experiment, $$x_n$$ is the molecular state, $$z_n$$ collects nuisance variables, and $$K$$ is the measurement kernel relating a latent state to an observation. In cryo-EM specifically, the index $$n$$ runs over different particles, while $$z_n$$ includes projection direction, translation, and microscope effects.

For independent snapshots, the distribution of observations is

$$
q(y) = \iint K(y \mid x, z)\,\pi(z)\,p_{\mathrm{src}}(x)\,dz\,dx.
\tag{4}
$$

Unlike Equation (2), this distribution retains molecule-to-molecule variation rather than reducing it immediately to an average. Yet, unfortunately, information is lost: recovering $$p_{\mathrm{src}}$$ from $$q(y)$$ remains an inverse problem. In cryo-EM, low contrast, unknown poses, microscope effects, and the high dimensionality of conformational variation can make that problem extremely difficult.

A single-molecule experiment does not immediately yield an ensemble, just as an ensemble-averaged experiment is not devoid of ensemble information. The two measurement routes lose information through different mechanisms. That leads to a natural, pragmatic question: can we quantify the ensemble information that any one experiment might produce, so we can assess these different strategies in a clear-eyed way?

### Ensemble resolution

One way to sharpen this question is to ask: how well can a given experiment distinguish different proposals for the source distribution, $$p_{\mathrm{src}}$$? One could imagine that a powerful experiment could validate one $$p_{\mathrm{src}}$$ while rejecting a related $$p_{\mathrm{src}}'$$, whereas a less informative experiment could not distinguish between the two. Turning this around: the degree of similarity at which an experiment can no longer say that the evidence for one distribution is significantly greater than for the other *is* a measure of  ensemble information.

To capture this idea, we propose the concept of an *ensemble resolution*. Just as spatial resolution asks when nearby features blur together and become indistinguishable, ensemble resolution should measure when distinct source distributions become experimentally indistinguishable. More precisely, two distributions cannot be distinguished when, after passing through the measurement process, they produce observables that agree within the uncertainty of the data.

An experiment can therefore contain ensemble information and still have low ensemble resolution. Consider a concrete example: a cryo-EM experiment may distinguish open from closed states for an ion channel, but not resolve a continuum between them. Or an experiment might be able to detect a rare state but not determine its occupancy precisely, or report a broad fluctuation without the ability to quantitatively infer the correlated motions that produced it.

For averaged measurements, the ensemble resolution will be set by the number and spatial specificity of the independent constraints. For single-molecule measurements, it is set by how well different latent states remain distinguishable through noise, nuisance variables, finite sampling, and the inference model.

Cryo-EM is a particularly interesting case study, as today ensembles are being inferred from cryo-EM data in two different ways: either by analyzing single particles statistically, or by computationally averaging to a single electrostatic potential map and building an ensemble model into that averaged signal. A sharp and functional definition of ensemble resolution should let us evaluate the merits of these two strategies in an objective fashion.

### Cryo-EM: structure or ensemble?

The crucial change occurs during reconstruction. Particle images that began as separate molecular observations are picked, curated, aligned, classified, masked, and averaged into a three-dimensional map. This processing is essential for high-resolution structure determination, but it also changes the inferential target.

A reconstructed map can be an excellent structural target. It may define a selected conformational state with impressive detail, and local heterogeneity can still appear as weak or diffuse density. But the map is not itself a molecule-resolved sample from $$p_{\mathrm{src}}$$. It is a derived estimate conditioned on which particles were selected, how they were aligned and classified, and what priors entered the reconstruction. If a rare state was removed upstream, or continuous variation was forced into a small number of classes, no analysis of the resulting map can restore that lost population information.

For questions about the distribution represented by the collected particles, particle-level data are therefore the more natural starting point. They retain the variation across individual observations before it is collapsed into a consensus reconstruction. This does not make image-level ensemble inference easy: an algorithm must separate conformational variation from pose, microscope effects, noise, and finite sampling, often through a low-dimensional representation of molecular motion.

Cryo-EM therefore makes the central diagnostic concrete: before asking whether an inference method is powerful enough, ask whether its target still contains the distributional information of interest. Consensus maps are appropriate targets when the goal is a detailed structure. When the goal is to infer the distribution represented by the collected particles, however, a consensus map alone is not enough; inference should begin from particle-level data. In future pieces, we will apply the same framework to other modalities: what did the experiment preserve, what did it compress, and what did the analysis pipeline discard?

### Further reading

We want to end by highlighting a few works that shaped our thinking and that readers might find interesting! This is not a comprehensive review, but an intentionally biased selection that covers the limits of averaged data, cryo-EM heterogeneity, Bayesian reconstruction, and image-level ensemble inference.

 1. Bonomi et al. *Principles of protein structural ensemble determination*. Current Opinion in Structural Biology, 2017.
 2. Ravera et al. *A critical assessment of methods to recover information from averaged data*. Physical Chemistry Chemical Physics, 2016.
 3. Tang et al. *Conformational heterogeneity and probability distributions from single-particle cryo-electron microscopy*. Current Opinion in Structural Biology, 2023.
 4. Scheres. *A Bayesian view on cryo-EM structure determination*. Journal of Molecular Biology, 2012.
 5. Sánchez-Espinosa et al. *Cryo-EM as a stochastic inverse problem*. arXiv, 2025.
 6. Clark et al. *Cooling fast and slow: Characterising the effects of vitrification in cryo-EM and the subsequent recovery of equilibrium populations*. bioRxiv, 2026.
