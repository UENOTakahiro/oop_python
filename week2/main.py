from room import Room
from character import Enemy, Character
from item import Item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with files.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains....")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = Enemy("Tabitha", "An enormous spider with countless eys and furry legs.")
tabitha.set_conversation("Sssss......I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        print("What will you fight with?")
        fight_with = input()
        if inhabitant.fight(fight_with) == True:
            print("Hooray, you won the fight!")
            current_room.character = None
            if inhabitant.get_defeated() == 2:
                print("Congratulations, you have vanquished the enemy horde!")
        else:
            print("Oh dear, you lose the fight.")
            print("That's the end of the game")
            dead = True
        else: 
