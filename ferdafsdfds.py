print("Приветсвую тебя, друг!")
name = input('Назови мне своё имя: ')
race_list = ['эльф', 'гном', 'человек', 'хоббит', 'кто-то']
print(f'Я рад видеть тебя,{name}! К какому виду ты принадлежишь:{race_list}?')
hp = 0
damage = 0
race = input('Кто ты: ')
if race == race_list[0]:
    hp+=10
    damage+=15
elif race == race_list[1]:
    hp+=20
    damage +=10
elif race == race_list[2]:
    hp+=11
    damage+=18
elif race == race_list[3]:
    hp += 25
    damage += 5
elif race == race_list[4]:
    hp += +1000
    damage += 5000
else:
    print('Ох, мне не известна такая раса...')
    hp+=0
    damage+=0
print(f'Что ж,{name}, так как ты {race}, то количество твоего здоровья равно\
 {hp}, а твой урон равен {damage}')
level = ['уровень 1', 'уровень 2', 'уровень 3']
for l in level:
    hp+= 1500
    damage+=4000
    print(f'Сейчас у тебя {l}, а это значит, что здоровье твоё равно {hp}, а урон: {damage}')