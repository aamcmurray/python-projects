#  Determines if a planned dive exceeds the British Sub Aqua Club guidelines on Oxygen partial pressure levels. This is not endorsed by or affiliated with BSAC. It's a code written for personal use based on their safety guidelines. 

class Error(Exception):
	"""Base class for other exceptions"""
	pass
class ValueTooSmallError(Error):
	"""Raised when input value too small"""
	pass
class ValueTooLargeError(Error):
	"""Raised when input value too large"""
	pass

def userinput(inputstr, inputmin, inputmax):
	while True:
		try:
			print(inputstr)
			inputval=float(input("Enter number here: "))
			if inputval <= inputmin:
				raise ValueTooSmallError
			elif inputval > inputmax:
				raise ValueTooLargeError
			break
		except ValueTooSmallError:
			print("please enter a number greater than ", inputmin)
		except ValueTooLargeError:
			print("please enter a number less than or equal to", inputmax)
		except ValueError:
			print("please enter a number")
	return inputval

def data(oxyinput, depthinput, safety):
	fraction_oxy=oxyinput/100
	abs_press=((depthinput/10)+1)
	oxy_partial_press=fraction_oxy*abs_press
	MOD=10*((safety/fraction_oxy)-1)
	print("_____________________________________")
	print("Calculated Oxygen Fraction: ", fraction_oxy, "\n", "Calculated Absolute Pressure (bar): ", abs_press, "\n","Calculated Oxygen Partial Pressure (bar): ", oxy_partial_press, "\n", "Safety limit (bar): ", safety, "\n", "Calculated Maximum Operating Depth: ", MOD, "\n")
	print("_____________________________________")
	return oxy_partial_press, MOD

def main():
	percent_oxy_tag= str("Oxygen (%) to be used")
	oxy_min = 10 
	oxy_max = 100
	depth_tag= str("Maximum planned depth (m)")
	depth_min = 0
	depth_max = 318
	safe = 1.4
	looper=True

	while looper==True: 
		try: 
			percent_oxy=userinput(percent_oxy_tag,oxy_min,oxy_max) 
			depth=userinput(depth_tag,depth_min,depth_max) 
			oppMOD=data(percent_oxy,depth,safe)
			oxygen_partial_press=oppMOD[0]
			MOD=oppMOD[1]
			if oxygen_partial_press >= safe:
				raise ValueTooLargeError
			elif oxygen_partial_press < safe: 
				print("Dive is within BSAC recommended safety limits for Oxygen partial pressure", "\n")
				print("Your maximum operating depth (m) is: ", MOD)
				looper==False
			break
		except ValueTooLargeError:
			print("Safety Limit is exceeded!", "\n", "Oxygen partial pressure (bar) should be below 1.4, your calculated Oxygen partial pressure (bar) is :",oxygen_partial_press, "\n", "Your input depth (m) ", depth, "is greater than the calculated safe Maximum operating depth", MOD,"\n","\n", "Decrease your planned depth or use a lower % Oxygen - if possible.")

if __name__ == "__main__":
	main()
