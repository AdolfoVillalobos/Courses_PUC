# Tópicos Avanzados en Inteligencia de Máquina

## Clase 2 de Mayo -2017

### Gibbs Sampling

Sean $x,y,z,w$:

$$ x_i \sim p(x |y_{i-1},z_{i-1},w_{i-1} )\\
y_i \sim p(x |x_{i-1},z_{i-1},w_{i-1} )\\
z_i \sim p(x |x_{i-1},y_{i-1},w_{i-1} )\\
w_i \sim p(x |x_{i-1},y_{i-1},z_{i-1} )\\
$$

Gibbs sampling es un caso especial de metropolis cuando $\alpha =1$.

Podemos calcular el $\alpha$ como:

$$\alpha= \dfrac{p(x')}{p(x)}\dfrac{Q(x|x')}{Q(x`|x)} =\dfrac{p(x_i'|x_{-i}')}{p(x_i|x_{-i}')}
$$

Para gibbs sampling se cumple $x_{-i} = x_{-i}'$, y por lo tanto $\alpha =1$

##### Ejemplo (programar en clases)

Una distribucion

$$P(x,y) = \dfrac{n!}{(n-x)!}y^{x+\alpha-1}(1-y)^{n-x+\beta-1},\\
x \in [0,n] \mbox{ , (discreto})\\
y \in [0,1] \mbox{,  (continuo)}$$
Se tiene :
$$ x|y \sim Bin(n,y)\\
y | x \sim Beta(x+\alpha,n-x+\beta)
$$
Y por tanto:
$$p(z| )$$