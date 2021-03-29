import pygame
import math
import random
pygame.init()

width,height = 1000,700
sized=[width,height]
screen=pygame.display.set_mode([width,height])

purple=pygame.Color('#2b2e4a')
orange=pygame.Color('#e84545')
red=pygame.Color('#903749')
darkred=pygame.Color('#53354a')

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

def line(screen,x,y,length,theta,line_width,color):
	if length<=1:
		return
	xx=int(x-length*math.cos(theta))
	yy=int(y-length*math.sin(theta))
	pygame.draw.line(screen,color,(x,y),(xx,yy),line_width)
	line(screen,xx,yy,(length*r),(theta+deltaTheta),line_width,color)
	line(screen,xx,yy,(length*r_two),(theta-deltaTheta_two),line_width,color)

def tuplechange(color,index):
	tup = color
	converted = list(tup)
	converted[0]=converted[0]-(converted[0]*(10*index/100))
	converted[1]=converted[1]-(converted[1]*(10*index/100))
	converted[2]=converted[2]-(converted[2]*(10*index/100))
	tup=tuple(converted)
	return tup
	

z=3
r,r_two,deltaTheta,deltaTheta_two=0.3,0.8,2*math.pi/z, (math.pi/(2*z))
running=True
while running:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False

	screen.fill((255,255,255))
	surface=vertical(sized,darkred,red)
	screen.blit(surface,(0,0))
	number=50
	for i in range(0,8):
		color=orange
		line(screen, width/2,height/2,number,(i/4)*math.pi,2,tuplechange(orange,i))

	pygame.display.flip()

pygame.quit()
