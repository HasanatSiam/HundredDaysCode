import random
rock = 'ROCK'
paper = 'PAPER'
scissors = 'SCISSORS'

game_images = [rock, paper, scissors]
user_choice = int(input("0 for Rock, 1 for Papaer and 2 for Scissors: "))
if user_choice >=0 and user_choice <= 2:
    print(game_images[user_choice])
com_choice = random.randint(0, 2)
print("Computer chose: ")
print(game_images[com_choice])


if user_choice >= 3 or user_choice < 0:
    print("Invalid number. You lose!")
elif user_choice == 0 and com_choice == 2:
    print("You win!")
elif com_choice == 0 and user_choice == 2:
    print("You lose!")
elif com_choice > user_choice:
    print("You lose!")
elif user_choice > com_choice:
    print("You win!")
elif com_choice == user_choice:
    print("It's a draw!")

