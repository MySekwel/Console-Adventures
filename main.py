import random

input("Hello adventurer! Welcome to Console Adventure, a world full of... adven--tures...")
input("So yeah, I hope you are ready for your... adventure, goddamnit! hehe :). Goodluck!")
name = input("I forgot to ask, what can I call you adventurer? ")
input(f"Welcome {name} to the Console World, where everything is... just plain text.")
input("But don't you worry, you won't get bored I promise you! Are you ready?")
choice = input("1. Yes | 2. Yes: ")
health = 100
armor = 0
gold = 0
exp = 0
level = 1
weapon = 'Fist'
if choice in ('1', '2', 'Yes', 'yes'):
    slime_hp = 50
    input("Alright, here's your weapon, use this dagger to kill a slime and earn glorious rewards.")
    weapon = 'Dagger'
    print(f"\n{name} has received a dagger!\n\n\n\n")
    while slime_hp >= 1:
        choice = input("To attack, type 'Attack': ")
        while choice not in ('Attack', 'attack'):
            choice = input("To attack, type 'Attack': ")
        damage = random.randint(5, 20)
        slime_hp -= damage
        if slime_hp <= 0:
            slime_hp = 0
        print(f"{name} has damaged the slime for {damage} HP, the slime is now {slime_hp}")
        if slime_hp <= 0:
            gold = 100
            exp = random.randint(20, 50)
            input(f"\n{name} has received {gold} gold and {exp}exp for killing the slime!")
            break

    input(f"\nWell done {name}! You've killed your first monster! I knew you have the potential.")
    input("This is the point I have to say goodbye, here's a light armor as a reward from me.")
    armor = 25
    input(f"Goodluck on your endless adventures {name}!")
    choice = input("\nWhat would you like to do? (Stats: 1 | Inventory: 2 | Adventure: 3): ")
    while int(choice) != 3:
        if int(choice) == 1:
            print("[Stats]")
            print(f"Name: {name}")
            print(f"Health: {health}")
            print(f"Armor: {armor}")
            print(f"Exp: {exp}")
            print(f"Level: {level}")
            input("\nLet's go? ")
            break
        if int(choice) == 2:
            print("[Inventory]")
            print(f"Gold: {gold}")
            print(f"Weapon: {weapon}")
            input("\nLet's go? ")
            break
    input("/Walking down the forrest of Agadu.../\n\n\n\n\n")
    input("Townsmen: Oh look at there, an adventurer!")
    input("Hello adventurer! Welcome to Green Pastures,")
    input("you can have fun and rest here while preparing for your adventure")

else:
    print("I thought you were the one, sorry for wasting your time :(")
