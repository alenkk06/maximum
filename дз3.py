import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError

warriors = [Warrior('Воин 1'), Warrior('Воин 2')]
while True:
    a = input('Введите +, чтобы какой-то воин атаковал. Для закрытия программы введите -: ')
    if a == '+':
        i = random.randint(0, 1)
        attacker, victim = warriors[i], warriors[i - 1]
        attacker.hit(victim)
        print(attacker.name, 'атаковал', victim.name)
        print('У', victim.name, 'осталось здоровья', victim.health)
        if victim.health <= 0:
            print(attacker.name, 'победил!')
            break
    elif a == '-':
        print('Игра oкончена')
        break
    else:
        print('Ошибка ввода')
