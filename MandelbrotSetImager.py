# Repeatedly iterates checking if the absolute value of the function is greater than two up to a certain number of iterations. Produces an image of the Mandelbrot set.

import math
import numpy as np
from PIL import Image, ImageDraw

def mandelbrot(cplx,it,jul):
	z = jul
	n = 0
	while abs(z) <=2 and n < it:
		z = z*z + cplx
		n += 1
	return n 

def gridbuild(array_x,array_y,val_set,stp_size):
	for i in range(0, stp_size):
		for j in range(0, stp_size):
			julia=complex(-0.7589,-0.0753)
			c = complex(array_x[i], array_y[j])
			d = mandelbrot(c, iterations, julia)
			val_set[(i,j)] = d  
	return val_set

def draw_machine(val_set,stp_size,it):
	mandel_picture = Image.new('RGB', (stp_size, stp_size), (0, 0, 0))
	draw = ImageDraw.Draw(mandel_picture)
	for i in range(0,stp_size):
		for j in range(0, stp_size):
			x = val_set[(i,j)] 
			color = 255 - int(x*255/it) 
			draw.point([i,j], (color, color, color)) 
	mandel_picture.save('Mandelbrot.png', 'PNG')

iterations = 100
step_size = 1000
a = np.linspace(-2,1,step_size)
b = np.linspace(-1,1,step_size)
valuesin = {}
values = {} 

values = gridbuild(a,b,valuesin,step_size)
draw_machine(values,step_size,iterations)
