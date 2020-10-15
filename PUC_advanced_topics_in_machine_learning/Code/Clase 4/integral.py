# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:24:11 2017

@author: Adolfo
"""

import numpy as np
import matplotlib.pyplot as plt

def sol(x):
    r = x/8-((np.sin(4*x)))/32
    return r
def phi(x):
    r = (np.sin(x)*np.cos(x))**2
    return r
def P(x):
    return 1.0
def aprox(n,a,b):
    x = np.random.uniform(a,b,n)
    c= integrate.quad(lambda x:P(x),a,b)[0]
    Z = n
    estimacion = (c)*sum(phi(x)*P(x)/Z)
    sol_exacta = integrate.quad(lambda x:phi(x)*P(x),a,b)[0]
    error = np.abs(estimacion-sol_exacta)
    return estimacion,sol_exacta,error
def error(k,a,b,sol):
    r = []
    for i in k:
        r.append(np.abs(sol-aprox(n,a,b)))
    return np.array(r)
        
a = 0.0
b = 3.0
n= 10000

m = aprox(n,a,b)[0]


k = np.arange(10,n,10)

errores = []

for i in k:
    errores.append(aprox(i,a,b)[2])

plt.plot(k,errores)

