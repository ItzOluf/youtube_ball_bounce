import pygame 
import random 
import time
import sys

pygame.init()
window_size = (450,800)
rect_x =225
rect_y = 400
black = (0,0,0)
var_gravity = 1

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('ballls')
running = True

def gravity(x,y,mass):
    y+= mass/5
    print(y)
    return x,y

while running:
    screen.fill((15, 15, 15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.draw.circle(screen, (255,255,255), (225,400), 225, width=10)
    pygame.draw.circle(screen, (255,0,0), (rect_x,rect_y),15)
    rect_x, rect_y =gravity(rect_x,rect_y,1)

    pygame.display.flip()
    
pygame.quit()
sys.exit()