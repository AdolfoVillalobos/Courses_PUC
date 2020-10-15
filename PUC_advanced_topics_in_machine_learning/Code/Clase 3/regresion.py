import numpy as np
import matplotlib.pyplot as plt
import math
#Regresion Simple
def regresion (X_matrix,Y):
	B = np.dot(np.dot(np.linalg.inv(np.dot( X_matrix.T,X_matrix)),X_matrix.T),Y)
	Y_estimado = np.dot(X_matrix,B)
	return (Y_estimado,B)
def data(file):
	data = np.genfromtxt(file,delimiter =",",dtype = None)
	X = np.array(data[1:,0],dtype = float)
	Y = np.array(data[1:,1],dtype=float)
	X = X/np.max(X)
	Y = Y/np.max(Y)
	return (X,Y)


def graficos_regresion(X,Y):
	fig, aux = plt.subplots()
	aux.scatter(X,Y)
	X_matrix = np.vstack( (np.ones((len(X),)) ,X)).T
	Y_estimado = regresion(X_matrix,Y)[0]
	aux.plot(X,Y_estimado,alpha=0.8,color="r")
	plt.show()

#Metodo de Kernels
def gaussian_kernel(xi,ui,sigma):
	exponent =np.power(math.e,0.5*(((xi-ui)/sigma)**2))
	return exponent
def phi(xi,u,sigma):
	result = [1]
	for i in u:
		result.append(gaussian_kernel(xi,i,sigma))
	return np.array(result)
def X_Gauss (X,u,sigma):
	result = phi(X[0],u,sigma)
	for i in range(1,len(X)):
		ph = phi(X[i],u,sigma)
		result =np.vstack((result,ph))
	return result
def graficos_gauss(X,Y,u,sigma):
	fig, aux = plt.subplots()
	aux.scatter(X,Y)
	X_gauss = X_Gauss(X,u,sigma)
	Y_estimado =regresion(X_gauss,Y)[0]
	aux.plot(X,Y_estimado,alpha=0.9,color="r")
	plt.show()

# Regresion polinomial

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
def graficos_pol(X,Y,p):
	fig,aux = plt.subplots()
	aux.scatter(X,Y)
	x_pol = X_pol(X,p)
	Y_estimado = regresion(x_pol,Y)[0]
	aux.plot(X,Y_estimado,alpha=0.6,color="r")
	plt.show()




#Experimento Regresion Simple
nombre = "lc_5.4892.1971.B.txt"
X,Y = data(nombre)

#Experimento Regresion Gaussiana

sigma = 1000
u = [50000,48000,49000,47000,51000,48500,49500,50500]
#graficos_gauss(X,Y,u,sigma)

#Regresion Polinomial
p=7
graficos_pol(X,Y,p)










