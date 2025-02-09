#Imported Libraries
import time
import random
#Lists
list = ["Ghoul", "Dragon", "troll", "Monster", "Gaint Lizard"]
random.shuffle(list)
villain = random.choice(list)
# ----------> Functions 
def print_pause(syntax):
    print(syntax)
    time.sleep(2)
def choice1():
    intger = input("Enter 1 or 2 ")
    if intger == "1":
        house()
    elif intger == "2":
        cave()
    else:
        print("Please try again.")
        choice1()
# Starting of the Game
def game():
    print_pause("You find yourself standing in an open field, filled with grass, and yellow wildflowers.")
    print_pause(f"Rumor has it that a {villain} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) magic wand.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice1()
# First choice going ot house
def house():
    
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a troll.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} finds you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
    choice_1of1 = input(("Would you like to (1) cast a spell or (2) run away?"))
    if choice_1of1 == "1":
        print_pause("You do your best...")
        print_pause(f"but your rusty old magic wand is no match for the {villain}.")
        print_pause("You have been turned into a frog!")
        score = 0 
        print_pause("You've lost! Try harder next time!")
        print_pause(f"Your score is {score}")
        choice_2of1 = input("Would you like to play again? (y/n) ").lower()
        while (choice_2of1 == "y" or choice_2of1 == "n"):
            if choice_2of1 == "y":
                print_pause("Preparing game please wait ...")
                print_pause("Tip: Try to look for a new and stronger wand before exploring the house!")
                game()
            elif choice_2of1 == "n":
                print("Thanks for playing")
                break
        else:
            print("please try again")
            choice_2of1 = input("Would you like to play again? (y/n)")
    elif choice_1of1 == "2":
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        choice1()
# Second choice entering the cave
def cave():
    score = 0
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Wand of Ogoroth!")
    print_pause("You put your rusty old magic wand in your bag and take the Wand of Ogoroth with you.")
    print_pause("You walk back out to the field.")
    print_pause("Your score has increased!")
    score += 1 
    print(f"Your score now is {score}")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice_a = input("What would you like to do?")
    if choice_a == "1":
        house2()
    elif choice_a == "2":
        cave()
# Going to house after entering the cave and getting the new wand
def house2():
    score = 1
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} finds you!")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny, rusty old magic wand.")
    choice_1of1 = input(("Would you like to (1) cast a spell or (2) run away?"))
    if choice_1of1 == "1":
        print_pause(f"As the {villain} moves to cast a spell, you raise your new Wand of Ogoroth.")
        print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the spell.")
        print_pause(f"But the {villain} takes one look at your shiny new wand and runs away!")
        print_pause(f"You have rid the town of the {villain}. You are victorious!")
        print_pause("Your score has increased!! Congratulations on winning our game! Play again to gian more points!")
        score += 5
        print(f"Your score is {score}")
        choice_2of1 = input("Would you like to play again? (y/n) ").lower()
        while (choice_2of1 == "y" or choice_2of1 == "n"):
            if choice_2of1 == "y":
                game()
            elif choice_2of1 == "n":
                print("Thanks for playing")
                break
        else:
            print("please try again")
            choice_2of1 = input("Would you like to play again? (y/n)")
    elif choice_1of1 == "2":
        print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        choice1()
# Calling the function Game!
game()