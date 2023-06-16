

class user:
    def __init__(self,our_damage,enemy_damage,health):
        self.our_damage=our_damage
        self.enemy_damage=enemy_damage
        self.health=health

    def health_down(self,enemy_damage):
        self.health-=enemy_damage
        print(f"\n{self.model}:")
        print("По тебе попали.Осталось {self.health} очков здоровья")

    def shot(self,enemy):
        if enemy.health<=0 or self.damage>=self.health:
            self.health=0
            print("Соперник уничтожен")
        else:
            enemy.health_down(enemy.damage)
            print(f"У противника осталось {enemy.health} очков здоровья")
            
