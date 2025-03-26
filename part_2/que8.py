'''Write a program to create a number guessing game for the user. The program should ask the user to input a number'''
import random

def number_guessing_game():
    
    answer = random.randint(1, 100)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess the correct number.")

    
    for attempt in range(1, attempts + 1):
        try:
            
            guess = int(input(f"Attempt {attempt}: Guess the number: "))

            
            if guess < answer:
                print("Too low!")
            elif guess > answer:
                print("Too high!")
            else:
                print("Correct number! You win!")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    else:
        print(f"Game Over! The correct number was {answer}.")


number_guessing_game()