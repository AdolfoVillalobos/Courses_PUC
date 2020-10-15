# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 16:20:34 2017

@author: Adolfo
"""
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
def sol(x):
    r = x/8-((np.sin(4*x)))/32
    return r
def phi(x):
    r = (np.sin(x))**2
    return r
def P(x):
    return np.cos(x)**2
def aprox(n,a,b):
    x = np.random.uniform(a,b,n)
    c= integrate.quad(lambda x:P(x),a,b)[0]
    Z = sum(P(x))
    estimacion = (c)*sum(phi(x)*P(x)/Z)
    sol_exacta = integrate.quad(lambda x:phi(x)*P(x),a,b)[0]
    error = np.abs(estimacion-sol_exacta)
    return estimacion,sol_exacta,error
n = 1000000

a = 0
b = 3

z = aprox(n,a,b)
print (z)