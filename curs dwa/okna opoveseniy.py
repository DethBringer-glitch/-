import pyautogui

'''pyautogui.alert(text='нажми',title='window',button='ок!')
pyautogui.confirm (text="хочешь сделать пароль?", title="лавушка джокера", buttons= ['Yes', 'No'])
pyautogui.prompt(text="делай пароль", title="лавушка джокера")
pyautogui.password(text="повтори его", title="лавушка джокера", mask="**")'''
from random import choice

numbers = [0, 1, 'A', 2, 3, 'B', 4, 5, 'C', 6, 7, 'D', 8, 9, 'E']

def get_sim(*args):
    number = str(choice(args))
    return number

win_ticket = get_sim(*numbers) + get_sim(*numbers) + get_sim(*numbers) + get_sim(*numbers)

print(f'Выиграл билет №: {win_ticket}')