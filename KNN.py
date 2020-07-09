#  ===============================================================
#  ____________________________________________K-Nearest Neighbors
#  ===============================================================

import numpy as np
import matplotlib.pyplot as plt 
import seaborn; seaborn.set() 

rand = np.random.RandomState(42)

array=rand.rand(10,2) 

x=array[:,0]
y=array[:,1]

x_distance=(x[:,np.newaxis] - x[np.newaxis,:])**2 
y_distance=(y[:,np.newaxis] - y[np.newaxis,:])**2

sumdist=x_distance+y_distance 

K=2 
nearest_partition=np.argpartition(sumdist, K+1, axis=-1) 

plt.scatter(x,y) 

for i in range(array.shape[0]):
	for j in nearest_partition[i, :K+1]:
		plt.plot(*zip(array[i],array[j]), color="black")
		
plt.show()
