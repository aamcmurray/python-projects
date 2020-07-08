#  =================================================================================
#  ___________________________________________________________Julia Set Movie Maker
#  ___________________________________________________________ver. 1________________
#  ___________________________________________________________07/07/2020____________
#  =================================================================================
#  Description
#  =================================================================================
#  Repeatedly iterates checking if the absolute value of the function is greater than two up to a certain number of iterations. Places to see:
#
#  complex(-0.7589,0.0753)
#  complex(-0.79,0.15)
#  complex(-0.162,1.04)
#  complex(0.33,0.008)
#  complex(-0.835,-0.2321)
#  complex(-0.7269, 0.1889)
#  complex(0.285, 0.01)
#  complex(-0.8, 0.156)
#  complex(-0.4, 0.6)
#
#  =================================================================================
#  Version History
#  =================================================================================
#
#  v.1. (080720) - Built off a mandelbot set plotter.
#  =================================================================================
#  The Code
#  =================================================================================
#  __________________________________________________________________________Imports

import math
import numpy as np
from PIL import Image, ImageDraw

#  __________________________________________________________________________Functions

def juliamake(c,it,juliaterm):
	c = c
	n = 0
	while abs(c) <=2 and n < it:
		c = c*c + juliaterm 
		n += 1
	return n 

# Returns the number of iterations taken to achieve abs(z)>2. 

def gridbuild(array_x,array_y,val_set,stp_size, julia):
	for i in range(0, stp_size):
		for j in range(0, stp_size):
			c = complex(array_x[i], array_y[j])
			d = juliamake(c, iterations,julia)
			val_set[i,j] = d  
	return val_set

# Creates complex numbers, c, from -2i-1.5j to 2i+1.5j using the values in the np.linspace() arrays. Then applies the juliamake() function to return the number of iterations. Number of iterations is then associated with coordinates for the draw_machine() function later. 

def draw_machine(val_set,stp_size,it,counter):
	julia_picture = Image.new('RGB', (stp_size, stp_size), (0, 0, 0))
	draw = ImageDraw.Draw(julia_picture)
	for i in range(0,stp_size):
		for j in range(0, stp_size):
			iteration_num = val_set[i,j]  
			clr = 255 - int(iteration_num * 255 / it) #  Designates a shade from 0-255 according to iteration number. 
			draw.point([i,j], (clr, clr, clr)) #  Draws the points. 
	save_dir="D:/Julia Movie/Images For Gif" #  Naming a directory to save in. 
	julia_picture.save(f"{save_dir}/new_image_{counter}.png") #  Saves image to directory with a number. 
	images.append(julia_picture)
	counter+=1 #  Incriments the counter. 
	return counter

#  __________________________________________________________________________ Globals

iterations = 100
step_size = 1000 
a = np.linspace(-2, 2, step_size) #  Re axis.
b = np.linspace(-1.5, 1.5, step_size) #  Im axis.
valuesin = {}
values = {} 
count=1
images=[]

#  __________________________________________________________________________ Main 

for i in range(1, 100):
	juliaterm=complex(0.3, -2 * (i / 100))
	values = gridbuild(a, b, valuesin, step_size, juliaterm)
	count=draw_machine(values, step_size, iterations,count)

images[0].save("D:/Julia Movie/Images For Gif/Julia.gif", save_all=True,append_images=images[1:], optimize=False, duration=40, loop=0) 