---
layout: post
title: Crystallographic distributions 
subtitle: PyTorch implementations of folded normal and Rice distributions
usemathjax: true
---

### Introduction
Two of the most important distributions in X-ray crystallography are the folded normal and Rice distributions. These are used to model centric and acentric structure factors respectively. In order to further crystallographic computing, we in the `rs-station` org desired learnable implementations of these distributions which could be trained by gradient descent. We have now implemented such distributions in PyTorch in the `rs-distributions` package ([`FoldedNormal`](https://rs-station.github.io/distributions/reference/rs_distributions/distributions/#rs_distributions.distributions.FoldedNormal) & [`Rice`](https://rs-station.github.io/distributions/reference/rs_distributions/distributions/#rs_distributions.distributions.Rice)). The remainder of this post will focus on the details of these implementations alongside some context about the recent history of variational inference. 


### Reparameterization
Reparameterization refers to several methods which render **sampling** from a distribution **as a differentiable operation** with respect to the distribution's parameters. The utility of the method is that **expectations** over distributions can be **learned by gradient descent** in a flexible manner. The concept was introduced in the seminal [paper](https://arxiv.org/abs/1312.6114) by Kingma and Welling. Their approach is simple and applies to any distribution which can be phrased as an invertible transform of a random variable with some standard distribution. 

In the original reparameterization paper, the requirement that transforms be invertible is problematic for many important distributions. For example, a folded normal random variable can be described as a transformation of a standard normal variable. If

$$
x \sim \mathrm{Normal}(0, 1),
$$

then
$$
z = |\sigma x + \mu|
$$

is folded normal distributed with location $\mu$ and scale $\sigma$. At face value, this seems like a valid reparameterization. However, it is not, because the inverse of the absolute value is ambiguous. If $f(x)=|x|$ then $f^{-1}(y)$ must have two values for any $y>0$. Therefore, the inverse is not a valid function. 

### Implicit Reparameterization Gradients

A solution to the restriction of reparameterization gradients came in the form of [implicit reparameterization gradients](https://arxiv.org/abs/1805.08498). This technique enables straightforward reparameterization of any distribution for which the cumulative distribution function is available and differentiable. 

Given a distribution with cumulative distribution function, $S_\phi(z)$, the gradient of samples, $z$, with respect to the parameters, $\phi$ is

$$
\nabla_\phi z = -\nabla_\phi S(z) / \nabla_z S(z) .
$$

All we need to compute implicit reparameterization gradients are the derivatives of $S$ with respect to the distribution's parameters and the value of the samples generated during the current gradient step. 

This suggests that we can reparameterize any distribution provided
 1) a procedure to generate samples from the desired distribution
 2) the gradients of cumulative distributionfunction with respect to parameters and samples

I will now describe how we meet these requirements for the folded normal and Rice distributions. 

### Folded Normal

A [folded normal](https://en.wikipedia.org/wiki/Folded_normal_distribution) random variable is the absolute value of a normally-distributed random variable. It has two parameters, $\mu$ and $\sigma$ which are the location and scale of the underlying normal distribution. Samples from a folded normal distribution can be straightforwardly generated from the normal distribution. If
$$
\begin{align}
x &\sim \mathrm{Normal}(\mu, \sigma) \\
z &= |x| 
\end{align}
$$
then
$$
z \sim \mathrm{FoldedNormal(\mu, \sigma)}.
$$

Gradients of the parameters with respect to these samples require the cumulative distribution function,

$$
S(z | \mu, \sigma) = \frac{1}{2}\left[
    \mathrm{erf}\left(
        \frac{z+\mu}{\sigma \sqrt{2}}
    \right) + 
    \mathrm{erf}\left(
        \frac{z-\mu}{\sigma \sqrt{2}}
    \right)
\right]
$$

Given the derivative of the error function,
$$
\frac{\partial}{\partial x} \mathrm{erf}\left(u\right) = \frac{2}{\sqrt \pi} e ^ {-u^2} \frac{\partial}{\partial x} u
$$

and a bit of algebra, the derivatives work out to pretty tidy expressions,

$$
\begin{align}
\frac{\partial}{\partial z} S(z \vert \mu, \sigma) &= 
\mathrm{Normal} \left(z\vert-\mu,\sigma\right) + 
\mathrm{Normal} \left(z\vert\mu,\sigma\right) \\
\frac{\partial}{\partial \mu} S(z\vert \mu, \sigma) &= 
\mathrm{Normal} \left(z\vert-\mu,\sigma\right) - 
\mathrm{Normal} \left(z\vert\mu,\sigma\right)  \\
\frac{\partial}{\partial \sigma} S(z\vert \mu, \sigma) &= 
-\frac{z + \mu}{\sigma}\mathrm{Normal} \left(z\vert-\mu,\sigma\right) 
-\frac{z - \mu}{\sigma}\mathrm{Normal} \left(z\vert\mu,\sigma\right) 
\end{align}
$$

These can be used compute the desired implicit reparameterization gradients,
$$
\begin{align}
\frac{\partial z}{\partial \mu} &= -
\frac{\partial}{\partial \mu}S\left(z|\mu, \sigma\right) /
\frac{\partial}{\partial z}S\left(z|\mu, \sigma\right)\\
\frac{\partial z}{\partial \sigma} &=  -
\frac{\partial}{\partial \sigma}S\left(z|\mu, \sigma\right) /
\frac{\partial}{\partial z}S\left(z|\mu, \sigma\right)\\
\end{align}
$$
which are straightforward to implement, 

```python
from torch.distributions import Normal

def gradients(z, mu, sigma):
    nminus = Normal(-mu, sigma).prob(z)
    nplus = Normal(mu, sigma).prob(z)
    dSdz = nminus + nplus
    dSdmu = nminus - nplus
    dSdsigma(z, mu, sigma) = (
       -(z + mu) * nminus -(z - mu) * nplus
    ) / sigma
    dzdmu = -dSdmu / dSdz
    dzdsigma = -dSdsigma / dSdz
    return dzdmu, dzdsigma
```
in PyTorch. Minhuan Li has a nice [explanation](https://minhuanli.github.io/2023/09/12/ImplicitReparameterizationTrick/) of how to use these gradients to define a custom function to support PyTorch's automatic differentiation. I will not repeat his effort here. 

### Rice Distribution
The rice distribution is the distribution of amplitudes of an isotropic, normally distributed variable in the complex plane. It has two parameters, $\nu$ and $\sigma$ which represent the distance from the origin and the standard deviation of the underlying normal distribution. Samples from $\mathrm{Rice}(\nu, \sigma)$ are easy to generate. If $x$ and $y$ represent independent, random draws from a standard normal, 

$$
\begin{align}
x &\sim \mathrm{Normal}(0, 1) \\
y &\sim \mathrm{Normal}(0, 1) \\
\end{align}
$$

Then,

$$
z = \sqrt{(\sigma x)^2 + (\sigma y + \nu)^2}
$$
follows the desired Rice distribution. Again, to estimate gradients of $z$ will require the cumulative distribution function, 

$$
S(z|\nu, \sigma) = 1 - Q_1\left(\frac{\nu}{\sigma} , \frac{z} {\sigma}\right)
$$

Where $Q_1$ is the Marcum Q function. The partial derivatives are [known](https://en.wikipedia.org/wiki/Marcum_Q-function#Differentiation). Using these gradients, it is possible to derive the implicit reparameterization gradients, 
$$
\begin{align}
\frac{\partial}{\partial \nu} z &= 
        I_1(\nu z \sigma^{-2}) /
        I_0(\nu z \sigma^{-2}) \\
\frac{\partial}{\partial \sigma} z &= 
        \sigma^{-1} \left(
            z - 
            \nu I_1(\nu z \sigma^{-2}) / 
            I_0(\nu z \sigma^{-2}) 
        \right).
\end{align}
$$
The end of this post will contain a more detailed derivation of these expressions. Once again, implementing these gradients is straightforward in PyTorch,

```python
from torch.special import i1e,i0e

def rice_gradients(z, nu, sigma):
    nuzsig2 = nu*z / (sigma*sigma)
    dzdnu = i1e(nuzsig2) / i0e(nuzsig2)
    dzdsigma = (z - dzdnu)/sigma
    return dzdnu, dzdsigma
```

Note that I used the numerically stable, exponentially [scaled Bessel function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.i1e.html) here. This is acceptable, because the exponential scaling factor is canceled by division. That is, `i1e(x) / i0e(x) == i1(x) / i0(x)`. Again, Minhuan Li has a nice [explanation](https://minhuanli.github.io/2023/09/12/ImplicitReparameterizationTrick/) of how to use these gradients to define a custom function in PyTorch. 


### More detailed derivation of Rice gradients


$$
\begin{align}
\frac{\partial}{\partial a} Q_1 \left(a, b\right) &= b \exp\left[-\frac{1}{2}\left(a^2 + b^2\right)\right] I_1(ab) \\
\frac{\partial}{\partial b} Q_1 \left(a, b\right) &= -b \exp\left[-\frac{1}{2}\left(a^2 + b^2\right)\right] I_0(ab)
\end{align}
$$

Knowing these derivatives, we should be able to compute the ones we need using the chain rule. Rephrasing the S in terms of the arguments of $Q_1$ gives a function $S: \mathbb R^2 \to \mathbb R$
$$
S(a, b) = 1 - Q_1(a, b)
$$
with a Jacobian / gradient,
$$
\boldsymbol{\partial}S(a,b) = \nabla S= \left\{
-\frac{\partial}{\partial a} Q_1 \left(a, b\right), \quad
-\frac{\partial}{\partial b} Q_1 \left(a, b\right) 
\right\}
$$
which is
$$
\begin{align}
 = \left\{
-b \exp\left[-\frac{1}{2}\left(a^2 + b^2\right)\right] I_1(ab),\quad 
b \exp\left[-\frac{1}{2}\left(a^2 + b^2\right)\right] I_0(ab)
\right\}
\end{align}
$$

to simplify the notation and facilitate implementation, let
$$
q(a,b) = b\exp\left[-\frac{1}{2}(a^2+b^2)\right],
$$


such that
$$
\boldsymbol{\partial}S(a,b) = \nabla S= \left\{
-q(a,b)I_1(ab), q(a,b)I_0(ab)
\right\}
$$

We can rephrase $S$ using function composition,

$$
S\left(z | \nu, \sigma\right) = 1 - Q_1(f(z, \nu, \sigma)),
$$
where $f : \mathbb R^3 \to \mathbb R^2$,
$$
f\left( z, \nu, \sigma \right) = \left\{ \frac{\nu}{\sigma} , \frac{z}{\sigma}\right\} 
$$
with Jacobian,
$$
\boldsymbol{\partial} f = \begin{bmatrix}
\frac{\partial f_1}{\partial z} & \frac{\partial f_1}{\partial \nu}  & \frac{\partial f_1}{\partial \sigma} \\
\frac{\partial f_2}{\partial z} & \frac{\partial f_2}{\partial \nu}  & \frac{\partial f_2}{\partial \sigma} \\
\end{bmatrix} = \begin{bmatrix}
0 & \sigma^{-1} & -\nu\sigma^{-2}\\
\sigma^{-1} & 0 & -z\sigma^{-2}\\
\end{bmatrix} 
$$

From the chain rule,

$$
\begin{align}
\nabla S &= 
\boldsymbol \partial S \left( f(z,\ \nu, \sigma\right)) \boldsymbol \partial f(z, \nu, \sigma) \\
&= \boldsymbol \partial S \left( \frac{\nu}{\sigma}, \frac{z}{\sigma}\right) \boldsymbol \partial f(z, \nu, \sigma) \\
&= \boldsymbol \partial f(z, \nu, \sigma)^T \nabla S \left( \frac{\nu}{\sigma}, \frac{z}{\sigma}\right) \\
&= \begin{bmatrix}
0 & \sigma^{-1} \\
\sigma^{-1} & 0 \\
-\nu\sigma^{-2}& -z\sigma^{-2}\\
\end{bmatrix}
\left\{\frac{\partial S(a,b)}{\partial a}, \frac{\partial S(a,b)} {\partial{b}}\right\}\\
&= \left\{
    \frac{\partial S(a,b)}{\partial b} \sigma^{-1}, 
    \frac{\partial S(a,b)}{\partial a} \sigma^{-1}, 
    -\frac{\partial S(a,b)}{\partial a} \nu \sigma^{-2} -\frac{\partial S(a,b)}{\partial b} z \sigma^{-2}
\right\}\\
&= \left\{
    q(a,b)I_0(ab) \sigma^{-1}, 
    -q(a,b)I_1(ab) \sigma^{-1}, 
    q(a,b)\left(I_1(ab)\nu\sigma^{-2} - I_0(ab)z\sigma^{-2}\right)
\right\}\\
&= \left\{
    q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right) 
        I_0(\nu z \sigma^{-2}) \sigma^{-1}, 
    -q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right)
        I_1(\nu z \sigma^{-2}) \sigma^{-1}, 
    q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right)
    \left(
        I_1(\nu z \sigma^{-2})\nu\sigma^{-2} - 
        I_0(\nu z \sigma^{-2})z\sigma^{-2}
    \right)
\right\}\\
\end{align}
$$

Writing the terms as separate partial derivatives,
$$
\begin{align}
\frac{\partial S}{\partial z} &= q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right) 
        I_0(\nu z \sigma^{-2}) \sigma^{-1} \\
\frac{\partial S}{\partial \nu} &= 
    -q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right)
        I_1(\nu z \sigma^{-2}) \sigma^{-1} \\
\frac{\partial S}{\partial \sigma} &= 
    q\left(\frac{\nu}{\sigma},\frac{z}{\sigma}\right)\left(
        I_1(\nu z \sigma^{-2})\nu\sigma^{-2} - 
        I_0(\nu z \sigma^{-2})z\sigma^{-2} 
    \right) \\
\end{align}
$$
is more visually appealing. Using the implicit reparameterization gradients formulas,
$$
\begin{align}
\frac{\partial}{\partial \nu} z = 
    -\frac{\partial S}{\partial \nu} 
    \left(
        \frac{\partial S}{\partial z}
    \right)^{-1} &= 
        I_1(\nu z \sigma^{-2}) /
        I_0(\nu z \sigma^{-2}) \\
\frac{\partial}{\partial \sigma} z = 
    -\frac{\partial S}{\partial \sigma} 
    \left(
        \frac{\partial S}{\partial z}
    \right)^{-1} &= 
        \sigma^{-1} \left(
            z - 
            \nu I_1(\nu z \sigma^{-2}) / 
            I_0(\nu z \sigma^{-2}) 
        \right) \\
\end{align}
$$
The $q(\frac{\nu}{\sigma}, \frac{z}{\sigma})$ terms cancel, leaving behind very clean expressions for the gradients of the samples. 
