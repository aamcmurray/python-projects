#  A lambda function to test mod values, returns a tuple. 
def tester(n,m):
	return lambda a: (a%n, a%m)

def main(x,y,z):
	#  Setting up the lambda function to test denominators 3 and 5.
	mod_value=tester(x,y)
	#  Some strings to concatenate
	divisibile_three, divisible_five, divisible_none='Fizz', 'Buzz', 'N/A'
	#  A for loop to evaluate the output of the tester for numerator inputs of 1-20.
	for i in range(1,z):
		if (sum(mod_value(i))==0):
			print(i, divisibile_three + divisible_five)
		elif (sum(mod_value(i))!=0) & ((mod_value(i)[0])==0):
			print(i, divisibile_three)
		elif (sum(mod_value(i))!=0) & ((mod_value(i)[1])==0):
			print(i, divisible_five)
		else:
			print(i, divisible_none)

main(3,5,20)
