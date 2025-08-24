import pyautogui
import time

'''while True:
    time.sleep(2)
    print(pyautogui.position())'''


def kalkulator():
    time.sleep(2.5)
    pyautogui.hotkey('win','r')
    time.sleep(0.50)
    pyautogui.write("c")
    time.sleep(0.20)
    pyautogui.write("a")
    time.sleep(0.20)
    pyautogui.write("l")
    time.sleep(0.20)
    pyautogui.write("c")
    pyautogui.press('enter')

def search_img():
    button5 = pyautogui.locateOnScreen("png.png", confidence=0.8)
    button5x, button5y = pyautogui.center(button5)
    pyautogui.click(button5x, button5y)
    time.sleep(0.9)
    pyautogui.moveTo(x=1382, y=459)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def search_img1():
    pyautogui.moveTo(x=1221, y=457)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    pyautogui.moveTo(x=1377, y=561)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

kalkulator()
time.sleep(0.9)
search_img()
time.sleep(0.9)
search_img1()