import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def phi(x):
	r = np.sqrt(4.0-x)
	return r
def Ps(x):
	return 1/(x**2)
def Q1(x,mu,sigma):
	r = 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x - mu)**2 / (2 * sigma**2))
	return r
def Q2(x,loc,scale):
	r = np.exp(-abs(x-loc)/scale)/(2.*scale)
	return r
def integral(x):
	return  (1.0/4.0)*(np.log(np.abs(phi(x)+2)/(np.abs(phi(x)-2)))) +(1/(2*(phi(x)-2)))+(1/(2*phi(x)+2))

def aproximar_integral_lap(mu1,lamb,n):
	Z = integrate.quad( lambda x : Ps(x),1,4)[0]
	sample = np.random.laplace(mu1, lamb, n)
	x = []
	for i in range(len(sample)):
		if sample[i]>4.0 or sample[i]<1.0:
			continue
		else:
			x.append(sample[i])
	x = np.array(x)
	wr = Ps(x)/Q2(x,mu1,lamb)
	num = sum(wr*phi(x))
	den = sum(wr)
	return (Z*(num/den))

def aproximar_integral_gaus(mu2,sigma,n):
	Z = integrate.quad( lambda x : Ps(x),1,4)[0]
	sample = np.random.normal(mu2, sigma, n)
	x = []
	for i in range(len(sample)):
		if sample[i]>4 or sample[i]<1:
			continue
		else:
			x.append(sample[i])
	x = np.array(x)
	wr = Ps(x)/Q1(x,mu2,sigma)
	num = sum(wr*phi(x))
	den = sum(wr)
	return (Z*(num/den))


### Parametros
n = 1000
mu1 = 1
mu2 = 1
lamb = 1
sigma = 1

s = aproximar_integral_lap(mu1,lamb,n)

### error
