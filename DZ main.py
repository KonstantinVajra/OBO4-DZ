from abc import ABC, abstractmethod


# Абстрактный класс оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."


class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


# Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self, monster):
        if self.weapon:
            print(self.weapon.attack())
            monster.take_damage()
        else:
            print("Боец без оружия не может атаковать!")


# Класс монстра
class Monster:
    def __init__(self, health=1):
        self.health = health

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print("Монстр ранен, но еще жив!")


# Демонстрация работы кода
fighter = Fighter("Герой")
monster = Monster()

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
fighter.attack(monster)

fighter.change_weapon(bow)
fighter.attack(monster)

