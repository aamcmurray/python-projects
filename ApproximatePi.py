from numpy import random
import numpy as np 
import matplotlib.pyplot as plt 

def main():
	N = 10000

	circle_x = []
	circle_y = []
	square_x = []
	square_y = []

	i = 1

	while i <= N: 
		x=random.uniform(-1, 1)
		y=random.uniform(-1, 1)
		if (x**2 + y**2 <= 1):
			circle_x.append(x)
			circle_y.append(y)
		else:
			square_x.append(x)
			square_y.append(y)
		i += 1

	pi = 4 * len(circle_x) / float(N)

	plt.plot(circle_x, circle_y, 'r')
	plt.plot(square_x, square_y, ' g')
	title=str("Apprximated: ")+str(pi)
	plt.title(title)
	plt.grid()
	plt.show()

if __name__ == "__main__":
	main()
