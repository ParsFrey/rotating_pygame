import pygame
import sys
pygame.init()
screen_w = 1000
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
square_size = 50
square_color = RED
square_x = 500
square_y = 300 
w = 550
h = 100
z = 550
p = 600
x = 0
y = 0
a = 0
b = 0
t = 0
e = 0
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    angle = 0
    wx = w+x
    hy = h+y
    rotated_squ = pygame.Surface((square_size, square_size))
    pygame.draw.rect(rotated_squ, square_color, (square_x, square_y, square_size, square_size))
    #rotated_squ = pygame.transform.rotate(rotated_squ, angle)
    pygame.draw.circle(screen, RED, (wx+t, hy+e), 10)
    if x<250 and y<250 :
        x += 1
        y += 2
    elif y>=250 and y<375:
        x = x-2
        y = y+1
    elif y<=800 and y>=375:
        #x = x+2
        y = y+2
        e = e-3
    elif y>800 and x<=30:
        x = x+1
    elif x>30 and e>(-640) and y<930:
        y = y+1
    elif y>=930 and e>(-700):
        e = e-1
        t = t-1
    angle += 1
    if angle >= 360:
        angle = 0

    pygame.display.flip()
    clock.tick(280)

pygame.quit()
sys.exit()

