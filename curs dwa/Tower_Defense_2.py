


class Game:
    def __init__(self):
        self.enemys = []
        self.guards = []
        self.bal = 20
        self.gateway = 100
    def fight(self):
        self.enemys = [Enemy() for i in range(2)]
        for i in range(14):
            for j in self.enemys:
                j.position += 1
                for g in self.guards:
                    if g.attack(j):
                        self.enemys.remove(j)
                if j.position >= 15:
                    self.gateway -= j.damage
        print(self.gateway)
    def guards_add(self, v):
        self.guards.append(Guards())
class Enemy:
    def __init__(self):
        self.hp = 10
        self.damage = 3.5
        self.loot = 5
        self.position = 1       #15 поз

class Guards:
    def __init__(self):
        self.damage = 5
        self.cost = 20
        self.slovar = {1: [2, 4]}
        self.range = [2,4]

    def attack(self, victim):
        if victim.position in self.range:
            victim.hp -= self.damage
            if victim.hp <= 0:
                print('противник умер')
                return True
            else:
                print('противник выжил')





game = Game()