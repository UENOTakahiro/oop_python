from character import Enemy

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hello")
dave.describe()

dave.set_weakness("cheese")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
