import pyautogui
import time

def kalkulator():
    time.sleep(2.5)
    pyautogui.hotkey('win','r')
    time.sleep(0.50)
    pyautogui.write("calc", interval=0.5)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('5')
    time.sleep(1)
    pyautogui.press('-')
    time.sleep(1)
    pyautogui.press('5')
    time.sleep(1)
    pyautogui.press('=')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')


kalkulator()