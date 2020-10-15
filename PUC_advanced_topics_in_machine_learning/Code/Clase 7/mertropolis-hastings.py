import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import car_met_hast_STU as serie
from scipy.stats import multivariate_normal


##### Funciones

def genQ(xprev,cov):
    return (np.random.multivariate_normal(xprev, cov, 1)[0])

def Q(x,mean,cov):
    return multivariate_normal.pdf(x, mean=mean, cov=cov)

def metropolis(x0,T,X,Y,Z,cov):
    x = []
    x.append(x0)
    t = 0
    while t<T-1:
        t+=1
        xs = genQ(x[-1],cov)
        alpha = np.log((serie.car_lik(xs,X,Y,Z)/serie.car_lik(x[-1],X,Y,Z)) * (Q(x[-1],xs,cov)/Q(xs,x[-1],cov)))
        if alpha>=1:
            x.append(xs)
        else:
            bernoulli = np.random.binomial(1,alpha)
            if bernoulli==1: 
                x.append(xs)
            else: 
                t = t-1
    return x

##### Preprosessing

def data(file):
    data = np.genfromtxt(file,delimiter =",",dtype = None)
    X = np.array(data[1:,0],dtype = float)
    Y = np.array(data[1:,1],dtype=float)
    Z = np.array(data[1:,2],dtype=float)
    indices = np.where(Z <= 3* np.mean(Z))[0]
    X_limp = np.take(X,indices)
    Y_limp = np.take(Y,indices)
    Z_limp = np.take(Z,indices)
    Y = Y_limp/(np.max(Y_limp)-np.min(Y_limp))
    return (X_limp,Y,Z_limp)

nombre = "data.txt"
X,Y,Z= data(nombre)

#### Solucion optima por Scipy


#max_x = optimize.minimize(-1*car_lik,[1,1])


#Metropolis - Hastings

x0 = [1,1]
T = 1000
cov = np.diag([1,2])
samples = metropolis(x0,T,X,Y,Z,cov)


