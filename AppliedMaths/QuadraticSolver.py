import math
import numpy as np 
import matplotlib.pyplot as plt

def userinput(inputstr):
	while True:
		try:
			print(inputstr)
			inputval=float(input("Enter value: "))
			break
		except ValueError:
			print("Please enter a number")
	return inputval

def discriminant(x,y,z):
	disc = (y**2) - (4*x*z)
	if disc < 0 :
		print("The discriminant is less than zero - there are no real roots.")
		disc = math.sqrt(abs(disc)) / (2*x)
		solnthree = (-1*y) / (2*x)
		z_one = complex(solnthree,disc)
		z_two = complex(solnthree,-disc)
		return z_one, z_two
	elif disc == 0 :
		print("The discriminant is equal to zero - two equal real roots.")
		solnthree = (-1*y) / (2*x)
		return solnthree, solnthree
	elif disc > 0 :
		print("The discriminant is greater than zero - two different real roots.")
		solnone = ((-1*y) / (2*x)) + ((math.sqrt(disc)) / (2*x))
		solntwo = ((-1*y) / (2*x)) - ((math.sqrt(disc)) / (2*x))
		return solnone, solntwo
	return

def main():
	string_a=str("First coefficient")
	string_b=str("Second coefficient")
	string_c=str("Third coefficient")

	a=userinput(string_a)
	b=userinput(string_b)
	c=userinput(string_c)

	ans=list(discriminant(a,b,c))
	print("The roots are: ", ans)

	x=np.linspace(-5,5,100)
	y=a*(x**2)+(b*x)+c

	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)
	ax.spines["left"].set_position("center")
	ax.spines['bottom'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.xaxis.set_ticks_position('bottom')
	ax.yaxis.set_ticks_position('left')

	plt.plot(x,y, 'r')

	plt.show()

if __name__ == "__main__":
	main()
