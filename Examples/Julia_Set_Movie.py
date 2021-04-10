import math
import numpy as np
from PIL import Image, ImageDraw
from collections import defaultdict
from math import floor, ceil

def juliamake(c,it,juliaterm):
	c = c
	n = 0
	while abs(c) <=2 and n < it:
		c = c*c*c + juliaterm 
		n += 1
	return n 

def gridbuild(array_x,array_y,val_set,stp_size, julia,iterations):
	histogram=defaultdict(lambda: 0)

	for i in range(0, stp_size):
		for j in range(0, stp_size):
			c = complex(array_x[i], array_y[j])
			d = juliamake(c, iterations,julia)
			val_set[i,j] = d  
			if d < iterations:
				histogram[floor(d)]+=1
	total=sum(histogram.values())
	hues=[]
	h=0
	for i in range(0,iterations):
		h+=histogram[i]/total
		hues.append(h)
	hues.append(h)
	return val_set,hues

def linear_interpolation(color1, color2, t):
    return color1 * (1 - t) + color2 * t 

def draw_machine(val_set,stp_size,it,counter,hues):
	julia_picture = Image.new('HSV', (stp_size, stp_size), (0, 0, 0))
	draw = ImageDraw.Draw(julia_picture)
	for i in range(0,stp_size):
		for j in range(0, stp_size):
			iteration_num = val_set[i,j]  
			hue = 255 - int(255*linear_interpolation(hues[floor(iteration_num)], hues[ceil(iteration_num)], iteration_num % 1)) #  Designates a shade from 0-255 according to iteration number. 
			saturation=255
			value=255 if iteration_num<100 else 0
			draw.point([i,j], (hue,saturation,value)) #  Draws the points. 
	save_dir="D:/Julia Movie/Images For Gif/NewMovie" #  Naming a directory to save in. 
	julia_picture.convert('RGB').save(f"{save_dir}/new_image_{counter}.png", 'PNG')
	images.append(julia_picture)
	counter+=1 #  Incriments the counter. 
	return counter

iterations = 100
step_size = 1000 
a = np.linspace(-2, 2, step_size) #  Re axis.
b = np.linspace(-1.5, 1.5, step_size) #  Im axis.
valuesin = {}
values = {} 
count=1
images=[]

for i in range(-100,100,1):
	juliaterm=complex(-0.162, 2*i/100)
	values,hues = gridbuild(a, b, valuesin, step_size, juliaterm, iterations)
	count=draw_machine(values, step_size, iterations,count,hues)

images[0].save("D:/Julia Movie/Images For Gif/NewMovie/Julia.gif", save_all=True,append_images=images[1:], optimize=False, duration=40, loop=0) 
