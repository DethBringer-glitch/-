import pyautogui
import time

strength = 0


def craft():
    time.sleep(2)
    move('s')
    pyautogui.hotkey('4')
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.leftClick(x=844, y=667)
    time.sleep(1)
    pyautogui.moveTo(x=859, y=412)
    time.sleep(1)
    pyautogui.dragTo(x=937, y=402, duration=0.75, button='right')
    time.sleep(1)
    pyautogui.leftClick(x=844, y=667)
    time.sleep(1)
    pyautogui.leftClick(x=883, y=656)
    time.sleep(1)
    pyautogui.moveTo(x=895, y=441)
    time.sleep(1)
    pyautogui.dragTo(x=898, y=483, duration=0.75, button='right')
    time.sleep(1)
    pyautogui.leftClick(x=883, y=656)
    time.sleep(1)
    pyautogui.leftClick(x=1047, y=442)
    time.sleep(1)
    pyautogui.leftClick(x=813, y=657)
    time.sleep(1)
    pyautogui.hotkey('esc')
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(4)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.hotkey('1')
    move('w')


def mine():
    for i in range(17):
        click()
        move('d')
        click()
        move('w')
        time.sleep(0.5)
        with pyautogui.hold('shift'):
            pyautogui.keyDown('s')
            time.sleep(0.1)
            pyautogui.keyUp('s')
        time.sleep(0.5)
        click()
        move('a')
        click()
        move('w')
        time.sleep(0.5)
        with pyautogui.hold('shift'):
            pyautogui.keyDown('s')
            time.sleep(0.1)
            pyautogui.keyUp('s')


def move(key):
    pyautogui.keyDown(key)
    time.sleep(0.65)
    pyautogui.keyUp(key)


def click():
    global strength
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    strength += 1
    if strength == 131:
        strength = 0
        craft()
    time.sleep(0.141592654)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.mouseUp()
    strength += 1
    if strength == 131:
        strength = 0
        craft()


time.sleep(5)
mine()