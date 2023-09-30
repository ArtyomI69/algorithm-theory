class Hero:
    __damage = 20
    __health = 100

    def __init__(self, name):
        self.__name = name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, val):
        self.__health = val

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name -= val

    def attack(self, hero):
        print(f"{self.name} атакует")
        print(f"{hero.name} имеет {hero.health} здоровья")
        hero.health = hero.health - 20
