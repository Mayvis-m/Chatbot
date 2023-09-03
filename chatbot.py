import random

first_name = "Mayvis"
last_name = "Underscore"
full_name = print(f"{first_name} {last_name}")

age = 100
human = True
height = 700.0

print(f"Hello, my name is {full_name}. I am {age}.")
print(f"Yes, it is {human} that I am human.")
print(f"My height is {height} cm.")

drinks = ["iced coffee", "coke", "water","green tea"]
food = ["pizza","cheeseburgers","cheese sticks"]

print("Here are my favorite foods and drinks: \n") 
print(food,drinks)

print("Let me get to know you now.\n")

while True:
    your_name = input("What is your name?: ")
    your_age = input("How old are you?: ")
    your_height = input("How tall are you in cm?: ")
    drink_item = input("What do you like to drink?: ")
    food_item = input("What do you like to eat?: ")

    while True:
        answer = (input('Run again? (yes/no): '))
        if answer in ('yes', 'no'):
            break
        print("invalid input.")
    if answer == 'yes':
        continue
    else:
        print("Alright.")
        break
    
print(f"Your name is {your_name}.")
print(f"Your age is {your_age}.")
print(f"Your height is {your_height} cm.")
print(f"You like to drink {drink_item}.")
print(f"You like to eat {food_item}.\n")

while True:  
    play_game = input("Do you want to play rock,paper, scissors? (yes/no): \n").lower()

    if play_game != "yes":
        break
    
    let_us_play = "Now let's play rock, paper, scissors.\n"
    print(let_us_play)
    
    wins = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
 }
 
    choices = ["rock", "paper", "scissors"]

    human_turn = input("Enter your choice:")
    computer_turn = random.choice(choices)

    print("You chose: {human_turn}")
    print(f"{first_name} chose: {computer_turn}")

    if human_turn == computer_turn:
        print("it's a tie!")
    elif wins[human_turn] != computer_turn:
        print(f"{first_name} wins!")
    else:
        print(f"{your_name} wins!")

    play_again = input("Play again? (yes/no): \n").lower()
    
    if play_again != "yes":
     break

print()

print("Come over to my house so we can sleep.")
print("I will set an alarm clock so we can wake up at a certain time.\n")

time_selection  = input("What time would you like to wake up?: ")

print(f"Alright, I will set the alarm clock for {time_selection}. Good night!")

print("---------------------------- ")
print("---------------------")
print("-------------")
print("---------")
print("----")
print("-")

while True:
    answer = (input("Good morning! How did you sleep, good or bad?: ")).lower()
    if answer in ('good','bad'):
        break
    print("invalid input.")
if answer == 'good':
    print("Good!")
else: 
    print("Oh, I'm sorry to hear that.\n")

def eggs():
    print("Mix the eggs.")
    print("Fry the eggs on one side.")
    print("Flip the eggs.")
    print("Enjoy!")

def bacon():
    print("Put bacon on pan.")
    print("Fry the bacon on one side.")
    print("Flip the bacon.")
    print("Enjoy!")

def pancakes():
    print("Mix the pancake mix.")
    print("Pour on pan.")
    print("Flip the pancake. ")
    print("Enjoy!")

while True:
    breakfast_question = input("I would like to make you breakfast. Is that ok?: ").lower()
    if breakfast_question == 'yes':
        print("Awesome, I will make you whatever you like.")
      
        while True:
            breakfast_choice = input("What would you like for breakfast? Eggs, bacon, or pancakes: ").lower()
            if breakfast_choice == 'eggs':
                eggs()
            elif breakfast_choice == 'bacon':
                bacon()
            elif breakfast_choice == 'pancake':
                pancakes()
            
            print(f"Sure, I'll make you {breakfast_choice}!")

            another_choice = input("Do you want anything else for breakfast? (yes/no): ").lower()
            if another_choice == 'no':
                print(f"Alright, I will only make you {breakfast_choice}")
                break
        break
    elif breakfast_question == 'no':
        print("Ok, bye!")
        break
    else:
        print("Invalid input. Please anwer with 'yes' or 'no'.")

print("I hope you enjoyed your breakfast.")
        
while True:
    breakfast_quality = input("Did you enjoy the breakfast I made you? (yes/no): ").lower()
    if breakfast_quality == 'yes':
        print("That's great to hear!")
        break
    elif breakfast_quality == 'no':
        print("That's sad to hear.")
        break
    else:
        print("Invalid input. Please anwer with 'yes' or 'no'.")
        break 

print()

print("I really enjoy playing games.")

while True:
    another_game = input("Would you like to play another game? (yes/no): ").lower()
    if another_game == 'yes':
        print("Ok, let's play a snake game.")
        import snakegame
        break
    elif another_game == 'no':
        print("You can leave. I'm done with you.")
        exit()
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

print()

print("I could sure go for some coffee.")
print("I'll make us some coffee. \n")

def make_coffee(name):
    print("Ground coffee beans.")
    print("Add coffee and water to coffee maker.")
    print("Start coffee maker.")
    print(f"Coffee for {name}.")
    print("And coffee for me.")

make_coffee(your_name)
