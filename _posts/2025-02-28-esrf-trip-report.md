---
layout: post
title: ESRF Trip Report
subtitle: Mix and Inject Serial Crystallography at ESRF
author: Kevin Dalton
---

![ESRF](/assets/posts/2025-02-28-esrf-trip-report/esrf_view.jpg){: .blog-image-wide} 
Image of ESRF from the [Bastille, Grenoble](https://en.wikipedia.org/wiki/Bastille_(Grenoble)) courtesy of Kara Zielinksi. [(CC-BY-NC-ND license)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
{: .blog-caption-wide}

I spent last week at the European Synchrotron Radiation Facility (ESRF) in Grenoble, France. I was supporting beam time for Kara Zielinski and other friends of the Station. Apart from being a little remote, Grenoble is a cool place to visit. It's situated in the French Alps and is accessible from the Lyon or Geneva airports. Unlike most synchrotrons in the States, ESRF is close to the city center and well-connected to public transit. 

The team brought two samples to the [ID29 beamline](https://www.esrf.fr/id29) for time-resolved, mix and inject serial crystallography. We had a lot of technical difficulties including a leaky sample reservoir, a rogue attenuator cutting our flux, a broken HPLC pump, and one protein spontaneously crystallizing in a novel space group. In spite of it, we were able to collect timepoints at beyond 2.5 Å resolution for one of our samples, Hsp31, mixed with its substrate methylglyoxal. Our data follow the reaction progress from 50ms through 3s. 

We were attempting to record data in "single-turnover" conditions with substrate limiting. This is a challenging way to do a time-resolved experiment. The low sample concentration means that the fraction of substrate-bound proteins in the crystal will be small. Data analysis is ongoing, but we hope that the [multivariate Wilson prior](https://doi.org/10.1101/2024.07.22.604476) can help us resolve the reaction intermediates. 

For me, this was a landmark experiment, because it represents the first time that my new scaling software, [Abismal](https://github.com/rs-station/abismal), was used for real-time data analysis. For our data, we found that merging runtimes with abismal were competitive with the [Partialator](https://www.desy.de/~twhite/crystfel/manual-partialator.html) unity model. However, the implementation of Abismal as a machine-learning model trained by stochastic gradient descent (on small batches of data) means that it can "save its work" throughout training. This means it can start saving preliminary maps within minutes of parsing the data. Getting these preliminary maps early gave us actionable feedback and allowed the team to start refining structures faster. While Abismal is not necessarily ready for general use, it confirmed for me that it can provide useful feedback on the time scale of experiments. 

Thanks to everyone involved, especially the staff at ID29, Daniele, Sam, and Shibom!
