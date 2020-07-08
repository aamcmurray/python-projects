#  =================================================================================
#  ___________________________________________________________Quadratic Solver______
#  ___________________________________________________________ver. 5________________
#  ___________________________________________________________25/06/2020____________
#  =================================================================================
#  Description
#  =================================================================================
#
#  A simple program that solves quadratic equations using math and plots them using numpy and matplotlib
#
#  =================================================================================
#  Version History
#  =================================================================================
#
#  v.1. (190620) - Wrote a script with if statements that solves quadratics.
#  v.2. (200620) - Made the script input based.
#  v.3. (200620) - Added validation layers.
#  v.4. (200620) - Turned the input portion into a function, made a separate function for determining the discriminant and calculating the solutions.
#  v.5. (250620) - Used numpy and matplotlib imports to plot the function y=ax^2+bx+c.
#
#  =================================================================================
#  The Code
#  =================================================================================
#
#  __________________________________________________________________________Imports
import math
import numpy as np 
import matplotlib.pyplot as plt
#  __________________________________________________________________________Functions
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
#  __________________________________________________________________________Globals

string_a=str("First coefficient")
string_b=str("Second coefficient")
string_c=str("Third coefficient")

#  __________________________________________________________________________Code

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
