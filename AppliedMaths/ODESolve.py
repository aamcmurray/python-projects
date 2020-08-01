import numpy as np
import scipy.integrate as integrate
from numpy import trapz
import matplotlib.pyplot as plt
from sklearn.metrics import auc

def ODE_model(n,tau):
	tau = 5
	dndt = -n/tau
	return dndt

def plotting(tau,num):
	plt.plot(tau,num)
	plt.xlabel('Time /s')
	plt.ylabel('N(t)')
	plt.title('Radioactive Decay')
	plt.show()

def main(): 
	n0 = 7
	t = np.linspace(0,50)
	n = integrate.odeint(ODE_model,n0,t)
	n_for_area=n[:,0].copy()
	print("Area under curve: ", auc(t,n_for_area))
	plotting(t,n)

if __name__ == "__main__":
	main()
