# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:52:13 2017

@author: Adolfo
"""

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

n = 10000
x = np.random.uniform(0.0,1.0,n)
y = np.random.uniform(0.0,1.0,n)

mu = 0
sigma = 1

def gaussian_sample(x,y,mu,sigma):
    m = mu+sigma*(-2*np.log(x))*np.cos(2*np.pi*(y))
    n=mu+sigma*(-2*np.log(x))*np.sin(2*np.pi*(y))
    return (m,n)
M,N = gaussian_sample(x,y,mu,sigma)

bins= np.sort(N)

densidad =  1/(sigma * np.sqrt(2 * np.pi))*np.exp( - (bins - mu)**2 / (2 * sigma**2) )

plt.plot(bins,densidad)

