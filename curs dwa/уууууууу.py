import pyautogui
import time

time.sleep(5)
#pyautogui.screenshot('png.png',(801,504,79,53))
def search_img():
   button5 = pyautogui.locateOnScreen("png.png",confidence=0.8)
   button5x, button5y = pyautogui.center(button5)
   pyautogui.click(button5x, button5y)
search_img()