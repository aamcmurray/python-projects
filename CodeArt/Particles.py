import pygame
import random
import math

# =========================================================================================================================================
# VARIABLES
# =========================================================================================================================================

total_particles=100
height = 600
width = 900
borders=100

min_distance=100
aversion=-0.00001
min_speed,speed,max_speed=2,3,4
sight=80
speed_match_desire=0.015
center_desire=0.0015
inner_r_sq=140**2
outer_r_sq=170**2

sized=[width,height]

# =========================================================================================================================================
# CLASSES AND FUNCTIONS
# =========================================================================================================================================

class Particle:
	pass

def init_particle(total_particles,speed):
	particles=[]
	for i in range(0,total_particles):
		particle=Particle()
		particle.location = complex(random.randint(width/2-borders,width/2+borders),random.randint(height/2-borders,height/2+borders))
		a=random.randint(-speed,speed)
		choice=(-speed,speed)
		if a==0:
			b=random.choice(choice)
		elif a!=0:
			b=math.sqrt(speed**2-a**2)
		particle.velocity = complex(a,b)
		particle.history=[]
		particle.history.append(particle.location)
		particles.append(particle)
	return particles

def draw_particles(particle):
	length_particle_hist=len(particle.history)
	if length_particle_hist>0:
		if length_particle_hist<75:
			particle.history.append(particle.location)
			for i in range(0,length_particle_hist):
				x,y=int(particle.history[i].real),int(particle.history[i].imag)
				values,hue,difference,difference_two,difference_four=(x,y), (i*255/100),int((length_particle_hist-i)/2),int((length_particle_hist-i)/4),int((length_particle_hist-i)/12)
				pygame.Surface.set_at(screen,(x,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x-difference,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x-difference_two,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference_two,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference_two),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference_two),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x-difference_four,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference_four,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference_four),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference_four),(hue,hue,hue,hue))
		elif length_particle_hist==75:
			particle.history.append(particle.location)
			for i in range(0,length_particle_hist):
				x,y=int(particle.history[i].real),int(particle.history[i].imag)
				values,hue,difference,difference_two,difference_four=(x,y), (i*255/100),int((length_particle_hist-i)/2),int((length_particle_hist-i)/4),int((length_particle_hist-i)/12)
				pygame.Surface.set_at(screen,(x,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x-difference,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x-difference_two,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference_two,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference_two),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference_two),(hue,hue,hue,hue))
        pygame.Surface.set_at(screen,(x-difference_four,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x+difference_four,y),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y-difference_four),(hue,hue,hue,hue))
				pygame.Surface.set_at(screen,(x,y+difference_four),(hue,hue,hue,hue))
			particle.history.pop(0)
	return

def draw(moving_particles):
	for particle in moving_particles:
		draw_particles(particle)
	return

def update(moving_particles):
	for particle in moving_particles:
		keep_within_bounds(particle)
		avoid_others(particle,aversion,min_distance)
		limit_speed(particle,min_speed,max_speed)
		match_velocity(particle,sight,speed_match_desire)
		fly_towards_center(particle,sight,center_desire)
		x_c,y_c=width/2, height/2
		keep_in(x_c,y_c,particle, inner_r_sq,outer_r_sq)
		particle.location+=particle.velocity

def keep_within_bounds(particle) :
	if (particle.location.real < borders):
		particle.velocity += (random.randint(0, 40)/50)+0j
	if (particle.location.real > width - borders) :
		particle.velocity += -(random.randint(0, 40)/50)+0j
	if (particle.location.imag < borders) :
		particle.velocity += complex(0,(random.randint(0, 40)/50))
	if (particle.location.imag > height - borders) :
		particle.velocity += complex(0,-(random.randint(0, 40)/50))
	return

def keep_in(x_c,y_c,particle,inner_r_sq,outer_r_sq):
	x_p, y_p = particle.location.real, particle.location.imag
	d_sq = (x_p-x_c)**2 + (y_p-y_c)**2
	if ((d_sq<inner_r_sq)) & ((x_p-x_c)>0) & (y_p>y_c):
		particle.velocity+=0.4+0.4j
	elif ((d_sq<inner_r_sq)) & ((x_p-x_c)<0) & (y_p>y_c):
		particle.velocity+=-0.4+0.4j
	elif ((d_sq<inner_r_sq)) & ((x_p-x_c)>0) & (y_p<y_c):
		particle.velocity+=0.4-0.4j
	elif ((d_sq<inner_r_sq)) & ((x_p-x_c)<0) & (y_p<y_c):
		particle.velocity+=-0.4-0.4j
	if ((d_sq>inner_r_sq)) & (d_sq<(outer_r_sq)) & ((x_p-x_c)>0) & (y_p>y_c) :
		particle.velocity+=-0.4-0.4j
	elif ((d_sq>inner_r_sq))& (d_sq<(outer_r_sq))  & ((x_p-x_c)<0) & (y_p>y_c):
		particle.velocity+=0.4-0.4j
	elif ((d_sq>inner_r_sq))& (d_sq<(outer_r_sq))  & ((x_p-x_c)>0) & (y_p<y_c):
		particle.velocity+=-0.4+0.4j
	elif ((d_sq>inner_r_sq))& (d_sq<(outer_r_sq))  & ((x_p-x_c)<0) & (y_p<y_c):
		particle.velocity+=0.4+0.4j


def avoid_others(particle,aversion,min_distance):
	move = 0+0j
	for other_particle in moving_particles :
		if not (other_particle is particle) :
 			if abs(particle.location - particle.location) < min_distance :
 				move += particle.location - other_particle.location

	particle.velocity += move * aversion

def limit_speed(particle,min_speed,max_speed):
	speed = abs(particle.velocity)
	if (speed > (80*max_speed/100)) :
		particle.velocity = particle.velocity / speed * max_speed
	if (speed < min_speed) and (speed!=0) :
		particle.velocity = particle.velocity / speed * min_speed
	return

def match_velocity(particle,sight,speed_match_desire):
	avg_vel = 0+0j
	num_neighbors = 0
	for other_particle in moving_particles:
		if abs(particle.location - other_particle.location) < sight :
			avg_vel += other_particle.velocity
			num_neighbors += 1

	if num_neighbors > 0:
		avg_vel /= num_neighbors

	particle.velocity += (avg_vel - particle.velocity) * speed_match_desire

def fly_towards_center(particle,sight,center_desire):
	center = 0+0j
	num_neighbors = 0

	for other_particle in moving_particles :
		if abs(particle.location - other_particle.location) < sight :
			center += other_particle.location
			num_neighbors += 1

	if num_neighbors > 0 :
		center = center / num_neighbors

	particle.location += (center - particle.location) * center_desire

def shock(particle):
	real_speed = particle.velocity.real
	im_speed=particle.velocity.imag
	a=random.randint(0,100)/100
	real_choice=[a,-a]
	im_choice=[a,-a]
	if (100*random.random()>75) and (real_speed>3):
		real_speed+=random.choice(real_choice)
	if (100*random.random()>75) and (im_speed>3):
		im_speed+=random.choice(im_choice)
	particle.velocity=complex(real_speed,im_speed)
	
# =========================================================================================================================================
# MAIN FUNCTION
# =========================================================================================================================================

def main(done_before):
	done = False
	screen.fill((0,0,0))
	while not done:
		clock.tick(80)
		screen.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
		draw(moving_particles)
		update(moving_particles)
		pygame.display.flip()
	pygame.quit()

# =========================================================================================================================================
# MAIN LOOP
# =========================================================================================================================================

if __name__ == "__main__":
	pygame.init()
	done_before=False
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode(sized)
	pygame.display.set_caption("Particles")
	moving_particles=init_particle(total_particles,speed)
	main(done_before)
