import numpy as np
import matplotlib.pyplot as plt


def data(file):
	data = np.genfromtxt(file,delimiter =",",dtype = None)
	X = np.array(data[1:,0],dtype = float)
	Y = np.array(data[1:,1],dtype=float)
	X = (X-X.mean())/(X.std())
	Y = (Y-Y.mean())/(Y.std())
	return (X,Y)
def phi_pol(xi,p):
	result = []
	for i in range(0,p+1):
		result.append(np.power(xi,i))
	return np.array(result)
def X_pol(X,p):
	result = phi_pol(X[0],p)
	for i in range(1,len(X)):
		ph = phi_pol(X[i],p)
		result = np.vstack((result,ph))
	return result

def bayessian_regression(D,N,sigma,alpha,p):
	Phi = X_pol(D[0],p)
	Phin = X_pol(N[0],p)
	XTX= np.dot(Phi.T,Phi)
	shape = XTX.shape
	Vn = np.linalg.inv((alpha)**(-2)*np.identity(shape[0]) + (sigma)**(-2)*XTX)
	m = (sigma)**(-2) * np.dot(Vn, np.dot(Phi.T,D[1]).T)
	M = np.dot(Phin,m)
	Sigma = (sigma**2)*np.identity(Phin.shape[0])+np.dot(Phin,np.dot(Vn,Phin.T))
	print (XTX)
	return (M,Sigma)

##### Parametros
nombre = "lc_5.4892.1971.B.txt"
num_datos = 50
p = 9
X,Y = data(nombre)
x_train = X
y_train = Y
x_test = np.arange(x_train.min(),x_train.max(),0.01)
y_test =0


D = (x_train,y_train)
N = (x_test,y_test)
sigma,alpha = 0.2,2

#### Ejecucion
M,Sigma = bayessian_regression(D,N,sigma,alpha,p)

#### Plot

fig, aux = plt.subplots()
aux.plot(x_test,M,alpha = 1.2,color="r")
aux.fill_between(x_test,M-1.96*np.diagonal(Sigma),M+1.96*np.diagonal(Sigma),interpolate=True,color='g')
#aux.scatter(X,Y)
