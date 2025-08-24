import pyautogui






def logen():
    login = pyautogui.prompt(text="Логин", title="лавушка джокера")
    password = pyautogui.password(text="Пароль", title="лавушка джокера", mask="**")
    if login in data and password == data[login]:
        pyautogui.alert(text='Вы успешно вошли.')
    else:
        pyautogui.alert(text='Логин или пароль неверны.')

def reg():
    name = pyautogui.prompt(text="Имя", title="лавушка джокера")
    login = pyautogui.prompt(text="Логин", title="лавушка джокера")
    if login in data:
        pyautogui.alert(text='Данный логин уже существует.')
        return
    password = pyautogui.password(text="Пароль", title="лавушка джокера", mask="**")
    password_repeat = pyautogui.password(text="Повтори его", title="лавушка джокера", mask="**")
    if password == password_repeat:
        pyautogui.alert(text='Вы успешно зарегестрировались')
        data[login]=password
    else:
        pyautogui.alert(text='Пароли не совпадают.')

        
data = {'Max':'123'}


while True:
    answer = pyautogui.confirm(text='text', title='title', buttons=['Войти', 'Зарегестрироваться', 'Выйти'])
    if answer is None or answer == 'Выйти':
        answer = pyautogui.confirm(text='Вы точно хотите выйти?', buttons=['Выйти', 'Отмена'])
        if answer is None or answer == 'Выйти':
            break
    if answer == 'Войти':
        logen()
    if answer == 'Зарегестрироваться':
        reg()