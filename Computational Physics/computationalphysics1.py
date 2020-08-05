# summing a series
import numpy as np
import math as m
import matplotlib.pyplot as plt

def summation_machine():
	dictionary_one={}
	convergence=list()
	x=np.linspace(np.deg2rad(0.01),(np.deg2rad(360)+11*np.pi),1000)
	for j in range(0,1000):
		nth_term=x[j]
		summation=x[j]
		i=2
		while abs(nth_term/summation) > 10e-8:
			nth_term=nth_term*(-x[j]**2)/(((2*i)-1)*((2*i)-2))
			summation=summation+nth_term
			imax=i
			convergence.append(abs(nth_term/summation))
			i+=1
		dictionary_one[x[j]]=str(summation)
	return dictionary_one,convergence

def sin_function_method():
	dictionary_two={}
	x=np.linspace(np.deg2rad(0.01),(np.deg2rad(360)+11*np.pi),1000)
	for j in range(0,1000):
		true_value=np.sin(x[j])
		dictionary_two[x[j]]=str(true_value)
	return dictionary_two

def dictionary_convert(adict):
	ind=list()
	val=list()
	for key in adict:
		ind.append(key)
		val.append(float(adict[key]))
	return ind, val

first_dict,conv=(summation_machine())
if conv[len(conv)-1] < 10e-8:
	print(True)
indices,values=dictionary_convert(first_dict)
indices_two,values_two=dictionary_convert((sin_function_method()))

plt.plot(indices,values, label='Summation')
plt.plot(indices_two,values_two, '--', label='True value')
plt.legend()
plt.show()