#  =================================================================================
#  ___________________________________________________________Diving Safety Test____
#  ___________________________________________________________ver. 6________________
#  ___________________________________________________________28/07/2020____________
#  =================================================================================
#  Description
#  =================================================================================
#
#  A simple program that determines if a planned dive exceeds the British Sub Aqua Club guidelines on Oxygen partial pressure levels. This is not endorsed by or affiliated with BSAC. It's a code written for personal use based on their safety guidelines. 
#
#  =================================================================================
#  Version History
#  =================================================================================
#
#  v.1. (240720) - Initially a simple program that ran once with basic error validation. If a string was input rather than a float it would inform you but give you no chance to correct it and retry. 
#  v.2. (250720) - Turned the input process into a generalised function so it can be repeated for depth.
#  v.3. (260720) - Improved error validation, the inputs must be floats and they must not lie outside a given range thanks to custom error creation. The user is no prompted to retry on a failed attempt. 
#  v.4. (280720) - Currently working on forcing the user to repeat their entries if the partial pressure oxygen is outside of safe limits. 
#  v.5. (290720) - Forces the user to repeat their entries if the limits are exceeded
#  v.6. (010720) - Edits to print statements
#  =================================================================================
#  The Code
#  =================================================================================

#  __________________________________________________________________________Classes

class Error(Exception):
	"""Base class for other exceptions"""
	pass
class ValueTooSmallError(Error):
	"""Raised when input value too small"""
	pass
class ValueTooLargeError(Error):
	"""Raised when input value too large"""
	pass
# Custom exceptions for entries which are too small or large. 

#  __________________________________________________________________________Functions

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

# The above function takes user inputs and forces the user to retry should the inputs lie outside accetable ranges or be the wrong type. It then returns the input value. 

def data(oxyinput, depthinput, safety):
	fraction_oxy=oxyinput/100
	abs_press=((depthinput/10)+1)
	oxy_partial_press=fraction_oxy*abs_press
	MOD=10*((safety/fraction_oxy)-1)
	print("_____________________________________")
	print("Calculated Oxygen Fraction: ", fraction_oxy, "\n", "Calculated Absolute Pressure (bar): ", abs_press, "\n","Calculated Oxygen Partial Pressure (bar): ", oxy_partial_press, "\n", "Safety limit (bar): ", safety, "\n", "Calculated Maximum Operating Depth: ", MOD, "\n")
	print("_____________________________________")
	return oxy_partial_press, MOD

# This performs some calculations to establish the maximum operating depth and other key numbers for diving. 

#  __________________________________________________________________________Global variables 

percent_oxy_tag= str("Oxygen (%) to be used")
oxy_min = 10 
oxy_max = 100
depth_tag= str("Maximum planned depth (m)")
depth_min = 0
depth_max = 318
safe = 1.4
looper=True

#  __________________________________________________________________________Main

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