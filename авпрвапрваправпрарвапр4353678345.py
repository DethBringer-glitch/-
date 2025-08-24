import pygame
import time
import pygame_menu
from pygame_menu import themes
import menu


pygame.init()

WIDTH = 480
HEIGHT = 360
A = 20
B = 10
C = 10/ 2
FPS = 360
X = WIDTH / 2 - C
G = HEIGHT / 2 - C

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Меню')

clock = pygame.time.Clock()

run = True

mainmenu = menu.Menu(screen)
mainmenu.add.text_input('nickname: ','')
mainmenu.add.button('PLAY',mainmenu.disable)
mainmenu.add.button('EXIT',quit)


while run:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                X -= 5
            if event.key == pygame.K_d:
                X += 5
            if event.key == pygame.K_w:
                G -= 5
            if event.key == pygame.K_s:
                G += 5


            
    screen.fill(color=(200,150,255))
    pygame.draw.circle(screen,'#FFBCD9',(X,G), radius=B)
    mainmenu.flip(events)
    #pygame.draw.rect(screen, 'green', (230,170,20,20))
    pygame.display.flip()
pygame.quit()