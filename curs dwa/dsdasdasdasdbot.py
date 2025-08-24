import pyautogui
import time
import random

money = 1000
pyautogui.confirm(text='Хочешь поиграть в латерею?',title='Лотерея',buttons=['Да','Нет'])
while True:
    money -= 10
    if random.randint(1, 10) == random.randint(1, 10):
        money += 100
        answer = pyautogui.confirm(text=f'ты выйграл!\nтвой баланс {money}\nпродолжить?',title='Лотерея',buttons=['Да','Нет'])
        if answer is None or answer == 'Нет':
            break








print(money)
