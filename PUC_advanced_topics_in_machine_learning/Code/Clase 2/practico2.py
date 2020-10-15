from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import dirichlet

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n=100
a = np.array([1,2,3])

def plot_Dirichlet(a,n):
	datos = dirichlet.rvs(a,size=n)
	x = datos[:,0]
	y = datos[:,1]
	z = datos[:,2]
	ax.plot_trisurf(x, y, z)
	return (datos)

d=plot_Dirichlet(a,n)
#plt.show()
