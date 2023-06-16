class user:
    def __init__(self,our_damage,enemy_damage,health):
        self.user=user
        self.our_damage=our_damage
        self.enemy_damage=enemy_damage
        self.health=health

    def health_down(self,enemy_damage):
        self.health-=enemy_damage
        print(f"\n{self.user}:")
        print("По тебе попали.Осталось {self.health} очков здоровья")

    def shot(self,enemy):
        if enemy.health<=0 or self.damage>=self.health:
            self.health=0
            print("Соперник уничтожен")
        else:
            enemy.health_down(enemy.damage)
            print(f"У противника осталось {enemy.health} очков здоровья")

class magician(user):
    def __init__(self,our_damage,enemy_damage,health):
        magician().__init__( min_damage, max_damage, health)
        self.forceMagician = True

    def health_down(self, enemy_damage):
        magician().health_down(enemy_damage / 2)
        
class warrior(user):
    def __init__(self,our_damage,enemy_damage,health):
        magician().__init__( min_damage, max_damage, health)
        self.forceWarrior = True

    def health_down(self, enemy_damage):
        warrior().health_down(enemy_damage / 2)
        
class archer(user):
    def __init__(self,our_damage,enemy_damage,health):
        magician().__init__( min_damage, max_damage, health)
        self.forceArcher = True

    def health_down(self, enemy_damage):
        archer().health_down(enemy_damage / 2)
