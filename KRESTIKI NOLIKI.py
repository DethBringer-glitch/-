import pygame
import random
import menu


def side(a,pick):
    global player1,player2
    if pick:
        player1 = 'x'
        player2 = 'o'
    else:
        player1 = 'o'
        player2 = 'x'

def fild_draw():
    pygame.draw.line(screen, color='black', start_pos=(0, HEIGHT/3), end_pos=(WIDTH, HEIGHT/3))
    pygame.draw.line(screen, color='black', start_pos=(0, HEIGHT/3*2), end_pos=(WIDTH, HEIGHT/3*2))
    pygame.draw.line(screen, color='black', start_pos=(WIDTH/3, 0), end_pos=(WIDTH/3, HEIGHT))
    pygame.draw.line(screen, color='black', start_pos=(WIDTH/3*2, 0), end_pos=(WIDTH/3*2, HEIGHT))

def drawx_o():
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'o':
                pygame.draw.circle(screen, color='black', center=(j*w+c,i*h+c), radius=(c),width=4)
            if field[i][j] == 'x':
                pygame.draw.line(screen, color='black', start_pos=(j * w, i * h), end_pos=(j * w + w, i * h + h), width= 4)
                pygame.draw.line(screen, color='black', start_pos=(j * w + w, i * h), end_pos=(j * w, i * h + h), width= 4)


def win_check(symbol):
    global win1
    win1 = []
    if field[0][0] == field[1][1] == field[2][2] == symbol:
        win1 = [[0,0],[1,1],[2,2]]
        return True
    if field[0][2] == field[1][1] == field[2][0] == symbol:
        win1 = [[0,2],[1,1],[2,0]]
        return True
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == symbol:
            win1 = [[i,0],[i,1],[i,2]]
            return True
        if field[0][i] == field[1][i] == field[2][i] == symbol:
            win1 = [[0,i],[1,i],[2,i]]
            return True
    return False
def win1_draw():
    #pygame.draw.line(screen, 'black', start_pos=(win1[0][1] * w, win1[0][0] * h + c),end_pos=(win1[2][1] * w + w, win1[2][0] * h + c),width=10) #отрисовка по горизонтали
    #pygame.draw.line(screen, 'black', start_pos=(win1[0][1] * w + c, win1[0][0] * h),end_pos=(win1[2][1] * w + c, win1[2][0] * h + h),width=10)
    pygame.draw.line(screen, 'black', start_pos=(win1[0][1] * w, win1[0][0] * h),end_pos=(win1[2][1] * w + w, win1[2][0] * h + h),width=10)
    pygame.draw.line(screen, 'black', start_pos=(win1[0][1] * w, win1[0][0] * h),end_pos=(win1[2][1] * w + w, win1[2][0] * h + h),width=10)
pygame.init()




WIDTH = 600
HEIGHT = 600
w = WIDTH/3
h = HEIGHT/3
c = w/2
FPS = 360
player1 = 'x'
player2 = 'o'
pc = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MENU')

clock = pygame.time.Clock()

run = True

mainmenu = menu.Menu(screen)
mainmenu.active = True
mainmenu.add.selector('сторона:',items=[("crosses",True),("noughts",False)], onchange=side)
mainmenu.add.button('PLAY', mainmenu.disable)
mainmenu.add.button('EXIT', quit)

button = pygame.Surface((36,36))
field = [
    ['','',''],
    ['','',''],
    ['','','']
]

win = False
count = 0


while run: # цикл работает пока run=True
    clock.tick(FPS) # ограничение выполнения цикла в секунду
    events = pygame.event.get() # в переменную events записываются все события pygame
    for event in events: #event итерирует events
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                mainmenu.enable()
        if event.type == pygame.MOUSEBUTTONDOWN and not win and not mainmenu.active:
            pos = pygame.mouse.get_pos()
            if field[pos[1] // (HEIGHT // 3)][pos[0] // (WIDTH // 3)] == '':
                field[pos[1] // (HEIGHT // 3)][pos[0] // (WIDTH // 3)] = player1
                count += 1
                print(count)
                if win_check(player1):
                    print('You win!(*^▽^*)')
                    win = True
                    continue
                pc_y = random.randint(0, 2)
                pc_x = random.randint(0, 2)
                if count == 5:
                    continue
                while field[pc_y][pc_x] != '':
                    pc_y = random.randint(0, 2)
                    pc_x = random.randint(0, 2)
                field[pc_y][pc_x] = player2

                if win_check(player2):
                    print('defeat!╯︿╰')
                    win = True
                    continue
                print(field)





    screen.fill(color=("#00edff"))
    fild_draw()
    drawx_o()
    if win:
        win1_draw()
    mainmenu.flip(events)
    pygame.display.flip() # показать (перевернуть) изменение на экране
pygame.quit()