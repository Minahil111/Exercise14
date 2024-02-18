# import random for computer choice
import random


# Convert input value into Rock, Paper or Scissors
# the '==' operator checks if values of two operands are equal
# use 'not in' and list of choices to identify and display valid choice
# if user input is invalid will assign its value to 'None'
def convert_input(choice):
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'
    elif choice not in ['R', 'P', 'S']:
        print('\nInvalid choice. Please try again.')
    # how to stop code from running further?


# compare the results of user and computer to choose who wins
# use if loops for each win scenario for user
# and after use elif/else for a tie or loss scenario for user
def choose_winner(user_choice, computer_choice):
    if user_choice == 'Rock' and computer_choice == 'Scissors':
        return 'You Win!'
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        return 'You Win!'
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        return 'You Win!'
    elif user_choice == computer_choice:
        return "It's a tie!"
    else:
        return 'You Lose!'


# game function
# prompt user for input
# define user and computer choices
def play_game():
    # use .upper to make r,p,s return uppercase values as only coded for uppercase values
    # otherwise it will return invalid choice
    user_input = input("Make your choice! \nEnter R for Rock, P for Paper, or S for Scissors: ").upper()

    user_choice = convert_input(user_input)
    # for computer choice use random.randint to choose random integer in given rang
    # range is inclusive
    computer_choice_number = random.randint(0, 2)
    choice_list = ['Rock', 'Paper', 'Scissors']
    # use [] to index the list of choices and return the choice that assigns with the computer's number choice
    computer_choice = choice_list[computer_choice_number]

    print(f'\nYou chose {user_choice} and the computer chose {computer_choice}\n')
    print(choose_winner(user_choice, computer_choice))


# run the game
play_game()
