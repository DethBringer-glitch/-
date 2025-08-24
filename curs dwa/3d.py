from ursina import *
import random

app = Ursina()

camera.position = Vec3(0, 10, -10)  # Выше и чуть назад
camera.rotation_x = 45              # Наклон вниз под 45 градусов
camera.fov = 70                    # Увеличенный угол обзора

window.title = '3D Крестики-нолики на Ursina'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

board_size = 3
cell_size = 2

# Глобальные переменные для игры
board = [[0 for _ in range(board_size)] for _ in range(board_size)]
current_player = 1
figures = [[None for _ in range(board_size)] for _ in range(board_size)]

cross_color = color.red
nought_color = color.azure

# Освещение
DirectionalLight(y=2, rotation=(45, -45, 0), shadows=True)
AmbientLight(color=color.rgba(100, 100, 100, 0.3))

# Модель крестика с анимацией появления
class Cross(Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            model=None,
            parent=scene,
            scale=Vec3(0,0,0)
        )
        self.bar1 = Entity(parent=self, model='cube', color=cross_color, scale=(0.3, 0.05, 0.05))
        self.bar1.rotation_z = 45
        self.bar2 = Entity(parent=self, model='cube', color=cross_color, scale=(0.3, 0.05, 0.05))
        self.bar2.rotation_z = -45
        self.animate_scale(Vec3(1,1,1), duration=0.5, curve=curve.out_elastic)

# Модель нолика с анимацией появления
class Nought(Entity):
    def __init__(self, position):
        super().__init__(
            position=position,
            model=Circle(),
            color=nought_color,
            scale=0,
            rotation_x=90
        )
        self.animate_scale(0.5, duration=0.5, curve=curve.out_elastic)

def create_board():
    global board_plane, lines
    board_plane = Entity(
        model='plane',
        scale=board_size * cell_size,
        color=color.light_gray,
        collider='box'  # Вот это важно для взаимодействия мыши
    )

    lines = []
    line_thickness = 0.05
    line_height = 0.1
    for i in range(1, board_size):
        line_v = Entity(model='cube', color=color.black,
                        scale=(line_thickness, line_height, board_size * cell_size + line_thickness),
                        position=(i * cell_size - board_size * cell_size / 2, 0.01, 0),
                        collider=None)  # Отключаем коллайдер у линий, чтобы не мешали наведению
        lines.append(line_v)
        line_h = Entity(model='cube', color=color.black,
                        scale=(board_size * cell_size + line_thickness, line_height, line_thickness),
                        position=(0, 0.01, i * cell_size - board_size * cell_size / 2),
                        collider=None)  # Отключаем коллайдер
        lines.append(line_h)


def check_winner():
    for i in range(board_size):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    if all(all(cell != 0 for cell in row) for row in board):
        return 0
    return None

game_over_flag = False  # Новый флаг для контроля конца игры

def game_over(winner):
    global game_over_flag
    game_over_flag = True
    if winner == 1:
        info_text.text = "Победили крестики! 🥳"
    elif winner == 2:
        info_text.text = "Победили нолики! 💻"
    else:
        info_text.text = "Ничья! 🤝"
    invoke(reset_game, delay=3)

def reset_game():
    global board, current_player, figures, game_over_flag
    game_over_flag = False
    for i in range(board_size):
        for j in range(board_size):
            if figures[i][j]:
                destroy(figures[i][j])
                figures[i][j] = None
            board[i][j] = 0
    current_player = 1
    info_text.text = ""

def ai_move():
    global current_player
    if game_over_flag:
        return  # Если игра закончена, ИИ не ходит
    empty_cells = [(i,j) for i in range(board_size) for j in range(board_size) if board[i][j] == 0]
    if not empty_cells:
        return
    i,j = random.choice(empty_cells)
    board[i][j] = 2
    pos = Vec3(j * cell_size - board_size*cell_size/2 + cell_size/2, 0.1, i * cell_size - board_size*cell_size/2 + cell_size/2)
    figures[i][j] = Nought(position=pos)
    winner = check_winner()
    if winner is not None:
        game_over(winner)
    else:
        current_player = 1

def input(key):
    global current_player
    if not game_started or game_over_flag:
        return
    if current_player != 1:
        return
    if key == 'left mouse down':
        if mouse.hovered_entity == board_plane:
            local_pos = mouse.world_point - board_plane.position
            x = int((local_pos.x + board_size*cell_size/2) // cell_size)
            z = int((local_pos.z + board_size*cell_size/2) // cell_size)
            i, j = z, x
            if 0 <= i < board_size and 0 <= j < board_size:
                if board[i][j] == 0:
                    board[i][j] = current_player
                    pos = Vec3(j * cell_size - board_size*cell_size/2 + cell_size/2, 0.1, i * cell_size - board_size*cell_size/2 + cell_size/2)
                    figures[i][j] = Cross(position=pos)
                    winner = check_winner()
                    if winner is not None:
                        game_over(winner)
                    else:
                        current_player = 2
                        invoke(ai_move, delay=1)

# ----------- НАЧАЛО ДОБАВЛЕННОГО КОДА ДЛЯ УПРАВЛЕНИЯ КАМЕРОЙ -----------

# Сделаем "пивот" для камеры — точку вращения
camera_pivot = Entity()
camera.parent = camera_pivot
camera.position = Vec3(0, 10, -10)
camera.rotation_x = 45

# Включим захват мыши для вращения камеры (можешь отключить, если неудобно)
mouse.locked = False

def update():
    global current_player

    if game_started and not game_over_flag:
        # Управление камерой мышью (вращение вокруг pivot)
        camera_pivot.rotation_y += mouse.velocity[0] * 40 * time.dt
        camera.rotation_x -= mouse.velocity[1] * 40 * time.dt
        camera.rotation_x = clamp(camera.rotation_x, 10, 80)  # ограничим наклон камеры вниз/вверх

        # Управление камерой клавишами WASD
        speed = 10 * time.dt
        if held_keys['w']:
            camera_pivot.position += camera.forward * speed
        if held_keys['s']:
            camera_pivot.position -= camera.forward * speed
        if held_keys['a']:
            camera_pivot.position -= camera.right * speed
        if held_keys['d']:
            camera_pivot.position += camera.right * speed

# ----------- КОНЕЦ ДОБАВЛЕННОГО КОДА -----------

def start_game():
    global game_started, menu, info_text
    game_started = True
    menu.disable()
    create_board()
    info_text.text = ""

# Главное меню UI
game_started = False

menu = Entity(parent=camera.ui)
Panel(parent=menu, scale=(0.5,0.6), color=color.cyan.tint(-0.3))

Text('3D Крестики-нолики', parent=menu, y=0.1, scale=2, origin=(0,0))

btn_start = Button('Начать игру', parent=menu, y=-0.05, scale=(0.4,0.1), color=color.orange)
btn_exit = Button('Выйти', parent=menu, y=-0.18, scale=(0.4,0.1), color=color.red)

btn_start.on_click = start_game
btn_exit.on_click = application.quit

info_text = Text('', parent=camera.ui, y=-0.4, scale=1.5, color=color.yellow)

app.run()
