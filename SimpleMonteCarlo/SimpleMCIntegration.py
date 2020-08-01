import math
import random
import numpy as np
# Short Simple Monte Carlo integration to integrate ln(x)/x between 1 and 10

def function(a):
	return math.log(a)/a

def SMC_integrate(iterations, lower_x, upper_x,lower_y, upper_y):
	count = 0.0
	in_area = 0.0
	while count <iterations :
		x = random.uniform(lower_x, upper_x)
		y = random.uniform(lower_y, upper_y)
		#  (x,y) of a random generated point.
		if y < function(x):
			in_area += 1
		#  Checks if point lies under curve or not.
		count += 1
	area_box = (upper_x-lower_x)*(upper_y-lower_y) 
	answer=(in_area/count)*area_box
	error=1/(np.sqrt(iterations))
	return answer, error

def main():
	it=100000
	l_x = 1
	u_x = 10
	l_y = 0
	u_y = 1/math.e

print(SMC_integrate(it,l_x,u_x,l_y,u_y))

if __name__ == "__main__":
	main()
