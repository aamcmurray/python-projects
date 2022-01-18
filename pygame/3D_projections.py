from math import sin, cos, sqrt, pi
import pygame
from numpy import array, newaxis, argpartition

class Window:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        pygame.display.update()

class wire_mesh:
    def __init__(self, vertices, x, y, z, rotX, rotY, rotZ, scale):
        self.vertices = vertices
        self.x = x
        self.y = y
        self.z = z
        self.rotX = rotX
        self.rotY = rotY
        self.rotZ = rotZ
        self.scale = scale
    def project_and_rotate(self, x, y, z):
        px = (((x * cos(self.rotZ) - sin(self.rotZ) * y) * cos(self.rotY) - z * sin(self.rotY)) * (200 / ((((z * cos(self.rotY) + (x * cos(self.rotZ) - sin(self.rotZ) * y) * sin(self.rotY)) * cos(self.rotX) + (y * cos(self.rotZ) + x * sin(self.rotZ)) * sin(self.rotX)) + 5) + self.z))) * self.scale + self.x
        py = (((y * cos(self.rotZ) + x * sin(self.rotZ)) * cos(self.rotX) - (z * cos(self.rotY) + (x * cos(self.rotZ) - sin(self.rotZ) * y) * sin(self.rotY)) * sin(self.rotX)) * (200 / ((((z * cos(self.rotY) + (x * cos(self.rotZ) - sin(self.rotZ) * y) * sin(self.rotY)) * cos(self.rotX) + (y * cos(self.rotZ) + x * sin(self.rotZ)) * sin(self.rotX)) + 5) + self.z))) * self.scale + self.y
        return (int(px), int(py))
    def render(self, window):
        window.screen.fill((0,0,30))
        xpointslist=[]
        threedlist=[]
        for v in self.vertices:
            point = self.project_and_rotate(v[0], v[1], v[2])
            pygame.draw.circle(window.screen, (100*point[0]/255, 100*point[1]/255, 100*point[1]/255), point, 3)
            xpointslist.append([point[0],point[1]])
            threedlist.append([v[0],v[1],v[2]])
        arroy=array(threedlist)
        x=arroy[:,0]
        y=arroy[:,1]
        z=arroy[:,2]
        x_dist=(x[:,newaxis] - x[newaxis,:])**2 
        y_dist=(y[:,newaxis] - y[newaxis,:])**2
        z_dist=(z[:,newaxis] - z[newaxis,:])**2
        sum_dist=x_dist+y_dist+z_dist
        K=5
        nearest_partition=argpartition(sum_dist, K+2, axis=-1)
        for i in range(arroy.shape[0]):
            for j in nearest_partition[i, :K+1]:
                pygame.draw.line(window.screen,(100*point[0]/255, 100*point[1]/255, 100*point[1]/255),xpointslist[i],xpointslist[j],1)

def fibonacci_sphere(samples=200):
    points = []
    phi = pi * (3. - sqrt(5.))
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2
        radius = sqrt(1 - y * y)
        theta = phi * i
        x = cos(theta) * radius
        z = sin(theta) * radius
        points.append((x, y, z))
    return points

def plane(samples=16):
    points=[]
    for i in range(samples):
        for j in range(samples):
            y = 1 - (i / float(samples - 1)) * 2
            x = 1 - (j / float(samples - 1)) * 2
            z = 0
            points.append((x,y,z))
    return points

def cube(samples=8):
    points=[]
    for i in range(samples):
        for j in range(samples):
            for k in range(samples):
                y = 1 - (i / float(samples - 1)) * 2
                x = 1 - (j / float(samples - 1)) * 2
                z = 1 - (k / float(samples - 1)) * 2
                points.append((x,y,z))
    return points

surface = fibonacci_sphere()
window = Window(500, 500, "Sphere")
sphere = wire_mesh(surface, 250, 250,2, 0, 0, 10, 5)


while True:
    sphere.rotX += 0.001
    sphere.rotY += 0.001
    sphere.rotZ += 0.001
    sphere.render(window)
    window.update()
