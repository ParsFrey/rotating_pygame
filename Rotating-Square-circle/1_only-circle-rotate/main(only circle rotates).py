import pygame
import sys
pygame.init()
screen_w = 1000
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
square_size = 70
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
    wx = w+x
    hy = h+y
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))
    pygame.draw.circle(screen, RED, (wx, hy), 20)
    if x<250 and y<250 :
        x += 1
        y += 1
    elif x>=250 or y>=250:
        x = x-1
        y = y+1
    if y<750 and y>500:
        x = x+1
        y = y-1
    elif  y>=500:
        x = x-1000
        y = y-1
        pygame.draw.circle(screen, RED, (z+a+t,p+b+e ), 20)
       
        if a<250 and a>(-250):
            a -= 1
            b -= 1
        elif a>=(-250):
            t+=1
            e-=1
        if t==250:
            t=0
            e=0
            a=0
            b=0
            x=0
            y=0
    pygame.display.flip()
    clock.tick(320)

pygame.quit()
sys.exit()

