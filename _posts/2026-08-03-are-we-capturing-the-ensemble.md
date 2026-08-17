---
layout: post
title: Are We Capturing the Ensemble?
subtitle: What structural biology experiments preserve, blur, or discard about molecular distributions
author: Minhuan Li, F. Emil Thomasen, Pilar Cossio
contact: "{minhuanli,fthomasen,pcossio}@flatironinstitute.org"
usemathjax: true
---

![Two ways an experiment can encode a conformational ensemble]({{ '/assets/posts/2026-08-03-are-we-capturing-the-ensemble/measurement_types.png' | relative_url }}){: .blog-image-hero}
Two ways in which an experiment can encode a conformational ensemble. Ensemble-averaged measurements combine contributions from many molecules into each observable. In single-particle or single-molecule measurements, each observation arises from an individual molecule, and the ensemble is represented statistically across many observations.
{: .blog-caption-wide}

Structural biology is increasingly being asked to answer questions about ensembles rather than single structures. But two opposite intuitions can lead us astray. In cryo-electron microscopy (cryo-EM), a fuzzy or weak region of a reconstructed map is sometimes treated as if it were direct evidence of an ensemble: blur becomes dynamics. In the other direction, an experiment such as X-ray diffraction may be dismissed as incapable of constraining an ensemble because its measurements average over many molecules.
{: .post-lead}

These intuitions seem contradictory, but they make the same mistake. Both infer what an experiment can tell us about a molecular distribution from the appearance of its final representation, rather than from how the data were generated. A blurred map is not itself a probability distribution. But neither does averaging an observable necessarily collapse a distribution to a single structure.

The more useful question is therefore not whether a dataset "contains an ensemble." It is which differences between molecular distributions remain observable after the measurement process—and after the processing applied to the data. Two distinct ensembles may produce measurably different signals, or they may become indistinguishable once projected through experimental noise, limited observables, nuisance variables, finite sampling, or data reduction. Understanding that distinction has to come before choosing an ensemble-inference method.

To make this question precise, we first need to distinguish the distribution we want to learn from the one the experiment actually sees.

### What distribution enters the experiment?

Before asking what information the measurement preserves, we should first be clear about what distribution is being measured. Let $$p_{\mathrm{target}}(x)$$ denote the molecular distribution relevant to the scientific question, and $$p_{\mathrm{src}}(x)$$ the distribution actually present in the prepared sample when the measurement is made. Often we hope that $$p_{\mathrm{src}}$$ faithfully represents $$p_{\mathrm{target}}$$, but the two need not be identical.

The distinction is especially concrete in cryo-EM, where vitrification is itself a physical process acting on the ensemble. Recent work by Clark et al. examined how rapid cooling can perturb conformational populations and how equilibrium populations might subsequently be inferred from the vitrified ensemble [6]. More generally, temperature, chemical environment, sample preparation, and experimental timescales can all affect the relationship between the distribution of biological interest and the one presented to the instrument.

The possible difference between $$p_{\mathrm{target}}$$ and $$p_{\mathrm{src}}$$ is important, but it is not the problem we will pursue here. We will take the source distribution as the object presented to the experiment and ask what happens next:

$$
p_{\mathrm{src}}\longrightarrow\text{measurements}\longrightarrow\text{processed data}.
$$

Which distinctions within $$p_{\mathrm{src}}$$ survive this chain?

### How experiments constrain the source distribution

Different experiments encode $$p_{\mathrm{src}}$$ in different ways. Broadly, there are two useful cases. In an ensemble-averaged measurement, each observable combines contributions from many molecules. In a single-molecule measurement, individual observations arise from individual molecules, and the distribution appears statistically across many observations. These are not rankings of how much "ensemble information" an experiment contains. They are different ways of constraining the same underlying distribution.

For an ensemble-average measurement, the observable can be written as

$$
\int m(x)\,p_{\mathrm{src}}(x)\,dx + \varepsilon,
$$

where $$m(x)$$ is the forward model for the observable and $$\varepsilon$$ represents measurement uncertainty. The experiment does not reveal the conformation of any individual molecule. Instead, it reports an expectation of the observable over the source distribution.

Importantly, averaging in **observable space** is not the same as averaging in **conformational space**. Suppose two conformations, $$x_A$$ and $$x_B$$, occur with probabilities $$p_A$$ and $$p_B$$. The measured signal is $$p_A m(x_A)+p_B m(x_B)$$ not, in general, $$m\left(p_A x_A+p_B x_B\right)$$. This distinction matters. If the observable responds differently to the two conformations, their contributions can remain separately constrained even though the measurement averages over many molecules. An X-ray scattering pattern, for example, need not correspond to a fictitious structure halfway between two populated conformations. Spatially distinct states can leave distinct contributions to the measured density. "Averaged" therefore does not mean "only informative about an average structure."

Single-molecule experiments preserve a different kind of information. We can describe an individual observation as arising from a latent molecular state,

$$
x_n \sim p_{\mathrm{src}}(x),
$$

together with experimental nuisance variables $$z_n$$, followed by a measurement process,

$$
y_n \sim K(\,\cdot \mid x_n,z_n).
$$

In single-molecule FRET, repeated observations of the same molecule can additionally reveal transitions between coarse conformational states. In single-particle cryo-EM, time is not preserved: each particle contributes a noisy projection of one molecular configuration, and the ensemble appears through variation across many different particles.

For independent observations, their marginal distribution is

$$
\int K(y\mid x,z)\cdot\pi(z)\cdot p_{\mathrm{src}}(x)\,dz\,dx.
$$

Because molecule-to-molecule variation has not been collapsed immediately into a small set of ensemble averages, such data can in principle retain rich information about heterogeneity. But molecule-resolved does not mean that the underlying distribution is directly observed. Noise, unknown nuisance variables, limited sampling, and the dimensionality of conformational variation can make distinct molecular states difficult—or impossible—to distinguish.

The important point is therefore not that one class of experiment "measures ensembles" while the other does not. Both impose constraints on $$p_{\mathrm{src}}$$, but they preserve different distinctions within it. The next question is the one that matters for ensemble inference: **which differences between two possible source distributions would these measurements actually allow us to resolve?**

### The question of ensemble resolution

Just as spatial resolution asks when nearby features blur together, we can ask when two source distributions become experimentally indistinguishable. We use *ensemble resolution* to refer to this question: which differences between molecular distributions remain distinguishable after passing through the measurement process, given the uncertainty of the data?

The analogy to spatial resolution is useful, but it only goes so far. Ensembles can differ in more than one way, so there is no reason to expect a single number to summarize their resolution. Two distributions might contain the same major conformations but assign them different populations; one might contain a rare state absent from the other; or they might show similar fluctuations individually but differ in how those motions are correlated. An experiment may distinguish one of these differences while being nearly blind to another. What can be resolved therefore depends not only on the experiment, but also on what aspect of the distribution we are asking it to distinguish.

In a more controlled inference setting, we are beginning to see how this question can be formalized. Ensemble reweighting, for example, starts from a specified set of candidate conformations and asks how experimental measurements constrain their populations. Once the possible states are fixed, one can ask more precisely which differences in population are supported by a given set of measurements and their uncertainties [7]. General ensemble inference is harder: both the conformations themselves and their probabilities may be unknown. How to characterize ensemble resolution in that setting remains a much broader open problem.

We do not need a universal metric, however, to see that ensemble resolution can change as data are processed. A representation derived from an experiment may preserve some distinctions within $$p_{\mathrm{src}}$$ while suppressing or discarding others. Cryo-EM makes this especially clear, because the particle images and the reconstructed map are different stages of the same experimental pipeline—and they need not preserve the same information about the source distribution.

### Cryo-EM: from particles to maps

Cryo-EM makes the distinction between spatial and ensemble resolution especially concrete. Each particle image is a noisy two-dimensional projection of one molecule in the frozen sample. The usual analysis then selects particles, estimates their poses, separates or models heterogeneity, and combines many observations into three-dimensional reconstructions. These steps are essential for recovering high-resolution structural detail. But they also transform the information available about the source distribution.

A reconstruction can gain spatial resolution while losing ensemble resolution. A three-dimensional map may define a selected conformational state with remarkable detail, while no longer preserving all of the population information present across the particle images from which it was reconstructed. Particle selection can remove observations; classification can partition continuous variation into discrete groups; and a consensus reconstruction can combine heterogeneous particles into a single representation. These operations can therefore change which differences within $$p_{\mathrm{src}}$$ remain distinguishable.

This is also why weak or fuzzy density should not, by itself, be interpreted as an ensemble. Such density can arise from conformational heterogeneity, but also from imperfect alignment, limited signal, local resolution, occupancy, or other sources of uncertainty. **But even if the blur genuinely comes from conformational heterogeneity, heterogeneity alone does not specify a distribution**. The same diffuse density could arise from different sets of conformations, populations, or correlated motions across the particles. A map can therefore provide evidence for structural variability without identifying the underlying $$p_{\mathrm{src}}$$.

If the scientific target is a conformational distribution, particle-level observations are therefore the more natural place to begin. They retain molecule-to-molecule variation before it is compressed into a consensus or a small number of reconstructed states. Recovering an ensemble from those images remains a difficult inverse problem: particle-level data do not make the ensemble directly visible. They preserve molecule-to-molecule distinctions that later processing may remove.

The point is not that maps are the wrong output of cryo-EM. They are extraordinarily effective when the goal is high-resolution structure determination. The appropriate representation depends on the scientific question: if the goal is a conformational distribution, we must ask which steps in the pipeline preserve that distribution and which reshape, compress, or discard it.

### The takeaway

Before arguing for an ensemble-inference method, ask how the data were generated, what transformations they underwent, and which distinctions within the source distribution remain observable. An averaged measurement can still constrain multiple states; a molecule-resolved experiment does not make the ensemble directly visible; and a high-resolution reconstruction can preserve less population information than the particles from which it was built.

Thinking in terms of ensemble resolution shifts the question from whether an experiment "contains an ensemble" to a more useful one: what aspects of the molecular distribution can this dataset actually distinguish?

*Thanks to TJ Lane and Alisia Fadini for reading earlier drafts and for their thoughtful feedback.*

### Further reading

For readers who want the technical background, the short bibliography below points to work on structural ensemble determination, the limits of averaged data, cryo-EM heterogeneity, Bayesian reconstruction, and image-level ensemble inference.

 1. Bonomi et al. *Principles of protein structural ensemble determination*. Current Opinion in Structural Biology, 2017.
 2. Ravera et al. *A critical assessment of methods to recover information from averaged data*. Physical Chemistry Chemical Physics, 2016.
 3. Tang et al. *Conformational heterogeneity and probability distributions from single-particle cryo-electron microscopy*. Current Opinion in Structural Biology, 2023.
 4. Scheres. *A Bayesian view on cryo-EM structure determination*. Journal of Molecular Biology, 2012.
 5. Sánchez-Espinosa et al. *Cryo-EM as a stochastic inverse problem*. arXiv, 2025.
 6. Clark et al. *Cooling fast and slow: Characterising the effects of vitrification in cryo-EM and the subsequent recovery of equilibrium populations*. bioRxiv, 2026.
 7. Mattingly et al. *Measurement-limited learning of conformational heterogeneity in cryo-electron microscopy*. arXiv, 2026.
