import random

# Создайте карточк

dragon = 100
witch = 75
orc = 50
elf = 25

# Код торговца
yourscore = 0
dealer = 0
while (dealer < 3 and yourscore < 3):

    print('Текущий счет - Игрок:', yourscore, 'Торговец: - ', dealer)
    you = int(input('Выбирай: 100, 75, 50, 25'))
    if (you == dragon or you == elf or you == orc or you == witch):
        comp = random.randint(1, 4)
        if comp == 1:
            comp = 100
        if comp == 2:
            comp = 75
        if comp == 3:
            comp = 50
        if comp == 4:
            comp = 25
        print('Торговец выбрал: ', comp)
        if comp == you:
            print("НИЧЬЯ!")
        elif ((you == 100 and comp == 75) or
              (you == 100 and comp == 50) or
              (you == 100 and comp == 25) or
              (you == 50 and comp == 25) or
              (you == 75 and comp == 50) or
              (you == 75 and comp == 25)):
            print("Ты победил!")
            yourscore += 1
        else:
            print('Ты проиграл')
            dealer += 1
    else:
        print('нет такого варианта')
if yourscore > dealer:
    print("Ты победил, твоя подсказка:")
    print("Используй арифметические операторы и примеры для перегрузки, а так же умножай слова не меньше 50 раз")