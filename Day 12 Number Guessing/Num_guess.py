from random import randint

Easy = 10
Hard = 5


def check_answer(user_guss, actual_answer, turns):
    if user_guss > actual_answer:
        print('Too high')
        return turns-1
    elif actual_answer > user_guss:
        print('Too low')
        return turns-1
    else:
        print(f"You got it! Your answer was {actual_answer}")

def set_difficultry():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy".lower():
        return Easy
    else:
        return Hard

def game():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    print(f"correct answer: {answer}")

    turns = set_difficultry()
    

    guess = 0
    while (guess != answer):
        print(f"You have {turns} attempts left.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns==0:
            print("You have run out gusses. You lose")
            break
        elif guess!= answer:
            print('Guess again.')

game()