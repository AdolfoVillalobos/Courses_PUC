from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

## Gibbs Sampling

#### Distribuciones
def Conjunta(x,y,alph,beta,n):
    r = (np.math.factorial(n)/(np.math.factorial(n-x)*np.math.factorial(x)))*(y**(x+alph-1))*(y**(n-x+beta-1))
    return r
def Apply_Conjunta(X,Y,alpha,beta,n):
    Z = []
    for x,y in zip(X,Y):
        z = Conjunta(x,y,alpha,beta,n)
        Z.append(z)
    return (X,Y,Z)


##### Pre-ambulo
fig = plt.figure()
ax = fig.gca(projection='3d')
n = 10
alpha = 1
beta = 2
y0 = 1/2

###### Generacion de muestras Gibbs Sampling

def Gibbs(y0,alpha,beta,n):
    X =[]
    Y = []
    yiter=y0
    for i in range(2000):
        xiter = np.random.binomial(n,yiter,1)[0]
        X.append(xiter)
        Y.append(yiter)
        yiter = np.random.beta(xiter+alpha,n-xiter+beta)
    return X,Y

X,Y = Gibbs(y0,alpha,beta,n)
x,y,z = Apply_Conjunta(X,Y,alpha,beta,n)

######## Plot de Histograma

hist, xedges, yedges = np.histogram2d(x, y, bins=(100,100))
xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

xpos = xpos.flatten()/2.
ypos = ypos.flatten()/2.
zpos = np.zeros_like (xpos)

dx = xedges [1] - xedges [0]
dy = yedges [1] - yedges [0]
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.xlabel ("X")
plt.ylabel ("Y")


####### Plot Conjunta 

X, Y = np.meshgrid(X,Y)
X,Y,Z = Apply_Conjunta(X,Y,alpha,beta,n)

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')

surf = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

#### falta arreglar 



