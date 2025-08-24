import pygame
import time
import pygame_menu
from pygame_menu import themes
import menu
import pause

pygame.init()

WIDTH = 480
HEIGHT = 360
A = 20
B = A / 2
C = 10 / 2
H = 2
FPS = 360
X = WIDTH / H - C
G = HEIGHT / H - C

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MENU')

clock = pygame.time.Clock()

run = True

mainmenu = menu.Menu(screen)
mainmenu.add.text_input('nickname: ', '')
mainmenu.add.button('PLAY', mainmenu.disable)
mainmenu.add.button('EXIT', quit)

button = pygame.Surface((36,36))
text = pygame.font.Font(None,24).render('⏸',True,(255,255,255))
button_rect = pygame.Rect(0,0,36,36)
text_rect = pygame.Rect(0,0,36,36)


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
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if button_rect.collidepoint(event.pos):
                mainmenu.enable()



    screen.fill(color=(131, 67, 22))
    screen.blit(button,button_rect)
    screen.blit(text,text_rect)
    pygame.draw.circle(screen, '#fdff2b', (X, G), radius=B)
    mainmenu.flip(events)
    # pygame.draw.rect(screen, 'green', (230,170,20,20))
    pygame.display.flip()
pygame.quit()