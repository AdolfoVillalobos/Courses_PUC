import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

# Parametros
theta = 6
k = 2
loc = 10
scale = 5.8
n = 1000
def Q2(x,loc,scale):
	r = np.exp(-abs(x-loc)/scale)/(2.*scale)
	return r

def generar_gamma(k,theta,loc,scale,n):
	lap_sample = np.random.laplace(loc, scale, n)
	xb = []
	array = []
	for i in lap_sample:
		y = gamma.pdf(i,theta,k)
		test = np.random.uniform(i,Q2(i,loc,scale),1)
		if test < y:
			array.append(test)
			xb.append(i)
	return (np.array(xb))


a = generar_gamma(k,theta,loc,scale,n)

plt.scatter(a,Q2(a,loc,scale))
