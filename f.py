import random
import time
class Pycharm:
    def __init__(self,name,health,damage):
        self.damage = damage
        self.health = health
        self.name = name
        self.xp = 0
        self.lvl = 0
        self.heals = 0

    def attack(self, victim):
        luck = random.randint(1,4)
        if luck == 1:
            victim.health -= self.damage
            print(f"Ты нанёс врагу полный урон. А именно {self.damage}. Теперь у него {victim.health} здоровья.")
        elif luck == 2:
            victim.health -= self.damage*2
            print(f"ты сделал headshot. И нанёс {self.damage*2}. Теперь у него {victim.health} здоровья.")
        elif luck == 3:
            victim.health -= self.damage/2
            print(f"Ты попал в ногу. И снёс ему {self.damage/2} . Теперь у него {victim.health} здоровья.")
        elif luck == 4:
            victim.health -= 0
            print(f"Ты не попал, потому что ты рукожоп. И нанёс 0 урона. Теперь у него {victim.health} здоровья.")

        if victim.health <= 0:
            print(f"{victim.name} повержен!")
            luck = random.randint(0,1)
            if luck == 0:
                self.heals += 1
                print(f"Ты получил Лечебный отвар🧋! Теперь у тебя их {self.heals} ед.")

            self.xp += victim.xp
            if self.xp >= 100:
               while self.xp >= 100:
                   self.lvl += 1
                   print(f"ПОЗДРАВЛЯЮ! Уровень повышен: {self.lvl}")
                   self.xp -=  100
                   self.damage *= 1.5
                   print(f"Ты стал сильнее! ⚔️: {self.damage}")

            print(f"Ты получил {victim.xp} опыта! Теперь у тебя {self.lvl} LVL и {self.xp} XP.")
            return False
        else:
            return True

    def fight(self):
        print('mario')
class Enemy:
    races = {
        "долбаная мышь": (1, 0.01),
        "тупой моб": (25000000000000000000000000, 0.000000000000000000000000000000000000000000000000000000001),
        "русский язык": (1, 0.1),
        "изо": (1200, 250),
        "амогус": (1000000, 5000000),
        "бутылка": (10,9.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999),
        "стакан": (100,100)
    }
    def __init__(self):
        self.name = random.choice(list(self.races.keys()))
        self.health = self.races[self.name][0]
        self.damage = self.races[self.name][1]
        self.xp = self.health * 1.5

    def attack(self, victim):
        victim.health -= self.damage
        if victim.health <= 0:
            print(f"{self.name} нанёс тебе {self.damage} урона. Теперь у тебя 0 здоровья.")
            exit(print("ПОТРАЧЕНО!"))
        print(f"{self.name} нанёс тебе {self.damage} урона. Теперь у тебя {victim.health} здоровья.")


def create_pycharm(name,race,prof):
    hp = 180
    dmg = 25
    hp *= races[race][0]
    hp *= profs[prof][0]
    dmg *= races[race][1]
    dmg *= profs[prof][
        1]
    hero = Pycharm (name,hp, dmg)
    return hero
def start(heal = None):
    if heal is None:
        enemy = Enemy()
    else:
        enemy = heal
    print(f"Тебе встретился {enemy.name}. ❤️: {enemy.health}, ⚔️: {enemy.damage}")
    print("Нападать?")
    answer = input("Да/Нет/лечиться: ").lower()
    if answer == "да":
        fight(enemy)
    elif answer == "лечиться":
        if super_mario.heals > 0:
            super_mario.health += 50
            super_mario.heals -= 1
            print(f"Ты выпил Лечебный отвар🧋. ❤️: {super_mario.health}")
        else:
            print("У тебя нет больше отвара.")
        start(enemy)
    elif answer == 'нет':
        luck = random.randint(0, 100)
        if luck in range(10):
            print("Ты смог незаметно ускользнуть и пойти дальше!")
            time.sleep(2)
            start()
        else:
            print("Ты НЕ смог незаметно ускользнуть!")
            time.sleep(2)
            enemy.attack(super_mario)
            fight(enemy)
def fight(victim):
  result = super_mario.attack(victim)
  time.sleep(1)
  if result:
      victim.attack(super_mario)
      time.sleep(1)
      fight(victim)
  else:
    start()


name = input("Введи своё имя: ")
races = {
          "angel": (4.5, 1),
          "mink": (10000, 100000),
          "human": (1, 1),
          "shark": (1.75,2.12),
          "kiborg": (2.5,3.56),
          "ghoul": (6.8,1.46),
          "phone": (100,99.99),
          "cat": (10000,100000000000)
}
profs = {
    "предатель": (0.9, 2),
    "член экипажа": (2, 0.6),
    "инжинера": (1.2, 1.2),
    "обротень": (5,6),
    "доктор": (1.25,0.3),
    "зарядка": (1000,9999.9999),
    "игрушка": (99999,106586977985678546756756745675674567000000000)
}
race = ""
prof = ""
while race not in tuple(races.keys()):
    print (f"Bыбеpи расу: {tuple (races.keys())}")
    race=input("->").lower()
while prof not in tuple (profs.keys()):
    print (f"Bыбеpи профессию: {tuple(profs.keys())}")
    prof=input("->").lower()

super_mario = create_pycharm(name,race,prof)
print(super_mario.name,super_mario.health,super_mario.damage)

time.sleep(1)
start()