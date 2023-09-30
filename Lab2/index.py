import random

from hero import Hero

def battle(hero1, hero2):
    print("Здоровье обоих героев равно 100")
    while hero1.health > 0 and hero2.health > 0:
        chosen_attacker = random.randint(1, 2)
        if chosen_attacker == 1:
            hero1.attack(hero2)
        else:
            hero2.attack(hero1)

    determine_winner(hero1, hero2)

def determine_winner(hero1, hero2):
    if hero1.health == 0:
        print(f"{hero2.name} победил!!!")
    if hero2.health == 0:
        print(f"{hero1.name} победил!!!")

hero1 = Hero("Алёша Попович")
hero2 = Hero("Илья Муромец")

battle(hero1, hero2)

