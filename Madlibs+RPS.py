import random

first_name = "Mayvis"
last_name = "Underscore"
full_name = first_name + " " + last_name

age = 100
human = True
height = 700.0

print(f"Hello, my name is {full_name}. I am {age}.")
print(f"Yes, it is {human} that I am human.")
print(f"My height is {height} cm.")

drinks = ["iced coffee", "coke", "water", "green tea"]
food = ["pizza", "cheeseburgers", "cheese sticks"]

print("Here are my favorite foods and drinks: ")
print(food, drinks)

print(" ")

print("Let me get to know you now.")

print(" ")

while True:
    your_name = input("What is your name?: ").strip().title()
    while True:
        try:
            your_age = int(input("How old are you?: "))
            if your_age < 0:
                raise ValueError("Age cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for age.")
    
    while True:
        try:
            your_height = float(input("How tall are you in cm?: "))
            if your_height < 0:
                raise ValueError("Height cannot be negative.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive float for height.")
    
    while True:
        drink_item = input("What do you like to drink?: ").strip().lower()
        if drink_item in drinks:
            break
        else:
            print("Invalid input. Please choose from the provided drink options.")

    while True:
        food_item = input("What do you like to eat?: ").strip().lower()
        if food_item in food:
            break
        else:
            print("Invalid input. Please choose from the provided food options.")
    
    answer = input('Run again? (yes/no): ').lower()
    if answer != 'yes':
        print("Goodbye")
        break

print(f"Your name is {your_name}.")
print(f"Your age is {your_age}.")
print(f"Your height is {your_height} cm.")
print(f"You like to drink {drink_item}.")
print(f"You like to eat {food_item}.")

print(" ")

while True:
    play_game = input("Do you want to play rock, paper, scissors? (yes/no): ").lower()

    if play_game != "yes":
        break

    print(" ")

    print("Now let's play rock, paper, scissors.")

    print(" ")

    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    choices = ["rock", "paper", "scissors"]

    human_turn = input("Enter your choice (rock/paper/scissors): ").strip().lower()
    computer_turn = random.choice(choices)

    print("You chose:", human_turn.title())
    print(f"{first_name} chose:", computer_turn.title())

    if human_turn == computer_turn:
        print("It's a tie!")
    elif wins[human_turn] == computer_turn:
        print(f"{first_name} wins!")
    else:
        print(f"{your_name} wins!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("OK, Bye!")
