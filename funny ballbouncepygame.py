import pygame 
import random 
import time
import sys

pygame.init()
window_size = (450,1600/2)

black = (0,0,0)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('gravity')
# Hauptprogrammschleife
running = True
while running:
    screen.fill((15, 15, 15))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(black)
    pygame.draw.circle(screen, (255,255,255), (300,200), 200, width=20)
    pygame.draw.circle(screen, )
    pygame.display.flip()
    
pygame.quit()
sys.exit()
