import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#### Funciones
def MultiModal(x):
    p = 0.3*stats.norm.pdf(x,loc=0,scale=1)+0.7*stats.norm.pdf(x,loc=5,scale=3)
    return p

def IntervalCreator(mui,x,w):
    r = np.random.uniform(0,1)
    xl = x-r*w
    xr=x+(1-r)*w
    while MultiModal(xl) > mui:
        xl = xl-w
    while MultiModal(xr) > mui:
        xr = xr+w
    return (xl,xr)

def IntervalShrink(xi,x):
    if xi > x:
        xr=xi
        return (x,xr)
    else:
        xl =xi
        return (xl,x)
def SliceSampling(x0,k,w):
    xiter =x0
    samples = []
    samples2=[]
    for i in range(k):
        accept = False
        mui = np.random.uniform(0,MultiModal(xiter))
        (xl,xr) = IntervalCreator(mui,xiter,w)
        while not accept:
            xiter = np.random.uniform(xl,xr)
            if MultiModal(xiter)>mui:
                print ("Hemos aceptado el numero "+str(i))
                print ("El largo del intervalo es "+str(xr-xl))
                print ("El mu es "+str(mui))
                print ("La probabilidad es "+str(MultiModal(xiter)))
                samples.append(xiter)
                accept = True
            else:
                (xl,xr) = IntervalShrink(xiter,samples[i-1])
    return samples


##### Inputs
k = 100
w=5

#### Plot Multimodales

x = np.linspace(-5,10,100)
plt.plot(x,MultiModal(x))

### Ejecucion
x0 = 0
samples = SliceSampling(x0,k,w)
plt.scatter(samples,MultiModal(samples))
plt.show()