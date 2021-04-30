# Code to simulate the movement of a flock of birds.

import matplotlib.pyplot as plt
import numpy as np
import pygame
import random

otherorange=pygame.Color('#903749')
purple=pygame.Color('#2b2e4a')
orange=pygame.Color('#e84545')
red=pygame.Color('#903749')
darkred=pygame.Color('#53354a')

boid_tot = 200
height = 750               # window height
width = 1400              # window width
sized=[width,height]
borders = 350              # disstance to start avoid edge

class Boid:
	pass

def init_boids():
	boids = []
	for i in range(boid_tot):
		if i<(60*boid_tot/100):
			boid = Boid()
			boid.sight=20+200*np.random.beta(400,400, size=None)
			boid.max_speed = 19.7*np.random.beta(400,400, size=None)-5
			boid.min_speed = 6*np.random.beta(400,400, size=None)
			boid.speed_initial = np.random.uniform(boid.min_speed,boid.max_speed)
			boid.min_distance = 8+10*np.random.beta(1.5,6, size=None)
			boid.aversion = 2*np.random.beta(100,100,size=None)/10
			boid.center_desire = 10*np.random.beta(100,100,size=None)/100
			boid.speed_match_desire = np.random.beta(80,80, size=None)/7.5
			boid.loc = complex((random.randint(0, width)),(random.randint(0, height)))
			boid.vel = complex((random.randint(0, int(round(boid.speed_initial)))),(random.randint(0, int(round(boid.speed_initial)))))
			boid.color=pygame.Color('#e84545')
			#boid.avoid=False
			#boid.avoidance=0
			boids.append(boid)
		elif ((60*boid_tot/100)<=i<(80*boid_tot/100)):
			boid = Boid()
			boid.sight=20+200*np.random.beta(400,400, size=None)
			boid.max_speed = 19.7*np.random.beta(400,400, size=None)-5
			boid.min_speed = 6*np.random.beta(400,400, size=None)
			boid.speed_initial = np.random.uniform(boid.min_speed,boid.max_speed)
			boid.min_distance = 8+10*np.random.beta(1.5,6, size=None)
			boid.aversion = np.random.beta(100,100,size=None)/10
			boid.center_desire = 5*np.random.beta(100,100,size=None)/100
			boid.speed_match_desire = np.random.beta(80,80, size=None)/10
			boid.loc = complex((random.randint(0, width)),(random.randint(0, height)))
			boid.vel = complex((random.randint(0, int(round(boid.speed_initial)))),(random.randint(0, int(round(boid.speed_initial)))))
			boid.color=pygame.Color('#e84545')
			#boid.avoid=False
			#boid.avoidance=0
			boids.append(boid)
		else:
			boid = Boid()
			boid.sight=20+200*np.random.beta(400,400, size=None)
			boid.max_speed = 19.7*np.random.beta(400,400, size=None)-5
			boid.min_speed = 6*np.random.beta(400,400, size=None)
			boid.speed_initial = np.random.uniform(boid.min_speed,boid.max_speed)
			boid.min_distance = 12+10*np.random.beta(1.5,6, size=None)
			boid.aversion = np.random.beta(100,100,size=None)/20
			boid.center_desire = 8*np.random.beta(100,100,size=None)/100
			boid.speed_match_desire = np.random.beta(80,80, size=None)/15
			boid.loc = complex((random.randint(0, width)),(random.randint(0, height)))
			boid.vel = complex((random.randint(0, int(round(boid.speed_initial)))),(random.randint(0, int(round(boid.speed_initial)))))
			boid.color=pygame.Color('#e84545')
			#boid.avoid=False
			#boid.avoidance=0
			boids.append(boid)
	return boids

def keep_within_bounds(boid) :
	# Constrain a boid to within the window. If it gets too close to an edge,
	# nudge it back in and reverse its direction.
	if (boid.loc.real < 1.5*borders):
		boid.vel += (random.randint(0, 40)/50)+0j
	if (boid.loc.real > width - 1.5*borders) :
		boid.vel += -(random.randint(0, 40)/50)+0j
	if (boid.loc.imag < 1.5*borders) :
		boid.vel += complex(0,(random.randint(0, 40)/50))
	if (boid.loc.imag > height - 1.5*borders) :
		boid.vel += complex(0,-(random.randint(0, 40)/50))
	return

def fly_towards_center(boid):
	center = 0+0j
	num_neighbors = 0

	for other_boid in g_boids :
		if abs(boid.loc - other_boid.loc) < boid.sight :
			center += other_boid.loc
			num_neighbors += 1

	if num_neighbors > 0 :
		center = center / num_neighbors

	boid.loc += (center - boid.loc) * boid.center_desire

def avoid_others(boid):
	# Move away from other boids that are too close to avoid colliding
	move = 0+0j
	for other_boid in g_boids :
		if not (other_boid is boid) :
 			if abs(boid.loc - other_boid.loc) < boid.min_distance :
 				move += boid.loc - other_boid.loc

	boid.vel += move * boid.aversion

def limit_speed(boid):
	# Speed will naturally vary in flocking behavior,
	# but real animals can't go arbitrarily fast (or slow)
	speed = abs(boid.vel)
	if (speed > (80*boid.max_speed/100)) :
		boid.vel = boid.vel / speed * boid.max_speed
	if (speed < boid.min_speed) and (speed!=0) :
		boid.vel = boid.vel / speed * boid.min_speed
	return

def match_velocity(boid):
	# Find the average velocity (speed and direction) of the other boids and
	# adjust velocity slightly to match.
	avg_vel = 0+0j
	num_neighbors = 0
	for otherBoid in g_boids:
		if abs(boid.loc - otherBoid.loc) < boid.sight :
			avg_vel += otherBoid.vel
			num_neighbors += 1

	if num_neighbors > 0:
		avg_vel /= num_neighbors

	boid.vel += (avg_vel - boid.vel) * boid.speed_match_desire

def draw_boid(boid):
	x=int(boid.loc.real)
	y=int(boid.loc.imag)
	pygame.draw.circle(screen, boid.color, [x,y], 1)

	return

def draw():
	#screen.fill(BLACK)
	for boid in g_boids:
		draw_boid(boid)
	return

def update():
	for boid in g_boids:
		# Apply rules
		shock(boid)
		fly_towards_center(boid)
		avoid_others(boid)
		match_velocity(boid)
		limit_speed(boid)
		keep_within_bounds(boid)
		shock(boid)
		# Update the position based on the current velocity
		boid.loc += boid.vel

def shock(boid):
	real_speed = boid.vel.real
	im_speed=boid.vel.imag
	a=random.randint(0,100)/100
	real_choice=[a,-a]
	im_choice=[a,-a]
	if (100*random.random()>75) and (real_speed>3):
		real_speed+=random.choice(real_choice)
	if (100*random.random()>75) and (im_speed>3):
		im_speed+=random.choice(im_choice)
	boid.vel=complex(real_speed,im_speed)

def vertical(size, startcolor, endcolor):
	height = size[1]
	bigSurf = pygame.Surface((1,height)).convert_alpha()
	dd = 1.0/height
	sr, sg, sb, sa = startcolor
	er, eg, eb, ea = endcolor
	rm = (er-sr)*dd
	gm = (eg-sg)*dd
	bm = (eb-sb)*dd
	am = (ea-sa)*dd
	for y in range(height):
		bigSurf.set_at((0,y),
			(int(sr + rm*y),
				int(sg + gm*y),
				int(sb + bm*y),
				int(sa + am*y))
			)
	return pygame.transform.scale(bigSurf, size)

pygame.init()
g_boids=init_boids()
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Boids")
done = False
clock = pygame.time.Clock()
while not done:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
	screen.fill((255,255,255))
	surface=vertical(sized,purple,red)
	screen.blit(surface,(0,0))
	draw()
	update()
	print(pygame.Surface.get_at(screen,(200,200)))
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
