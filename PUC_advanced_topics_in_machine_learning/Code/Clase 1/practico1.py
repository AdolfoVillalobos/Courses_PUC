import numpy as np 
import matplotlib.pyplot as plt
import scipy
from scipy.stats import beta
from scipy.stats import binom
from scipy.stats import bernoulli


#####################
####  Parametros  ###
#####################

n = 20
p = 0.4
a = [5.0,2.0]
N1 = 11
N0 = 13
num_bins = 50

######################################
#Funciones de Densidad e Histogramas #
######################################

######################
## Distribucion Beta #
######################

#Densidad

fig1, ax1 = plt.subplots(1, 1)
x1 = np.linspace(beta.ppf(0.01, a[0], a[1]),beta.ppf(0.99, a[0], a[1]), 100)
ax1.plot(x1, beta.pdf(x1, a[0], a[1]),'r-', lw=5, alpha=0.6, label='Densidad Beta')
ax1.set_xlabel("Valores X")
ax1.set_ylabel("Valores Y")

#Histograma
r_beta = beta.rvs(a[0], a[1], size=1000)
ax1.hist(r_beta, normed=True, histtype='stepfilled', alpha=0.2)
ax1.legend(loc='best', frameon=False)

##########################
#  Distribucion Binomial #
##########################

#Densidad
fig2, ax2 = plt.subplots(1, 1)
x2 = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax2.plot(x2, binom.pmf(x2, n, p), 'bo', ms=8, label='Densidad Binomial')
ax2.set_xlabel("Valores X")
ax2.set_ylabel("Valores Y")

#Histograma
r_binom = binom.rvs(n, p, size=1000)
ax2.hist(r_binom, normed=True, histtype='stepfilled', alpha=0.2)
ax2.legend(loc='best', frameon=False)

################################
## Experimento lanzar moneda  ##
################################

fig3,ax3=plt.subplots(1,1)

##Funciones 

def posteriori(x,a,b,N0,N1):
	n = N0+N1
	integral, error = scipy.integrate.quad(lambda x: x**(N1 + a - 1)*(1 - x)**(N0 + b - 1),0,1)
	likelihood = scipy.special.binom(n, N1)*(x**N1)*(1 - x)**N0
	posteriori = x**(N1 + a - 1)*(1 - x)**(N0 + b - 1)/integral
	return (posteriori,likelihood)


## Preparar experimento:
resultado  = posteriori(x1,a[0],a[1],N0,N1)
ax3.plot(x1,resultado[0],alpha=0.6)
ax3.plot(x1,resultado[1],alpha=0.6)
ax3.plot(x1,beta.pdf(x1,a[0],a[1]),alpha=0.6)
ax3.set_xlabel("Valores X")
ax3.set_ylabel("Valores Y")


