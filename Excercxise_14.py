

# input("choose an option?")

the_game = 'rock','paper' , 'scissors'
import  random
max_attempts = 4
attempts = 0
draw = -1
win = 1
lose = 0
point = 1+0
for attempts in range (1,4):

    user_input = input('choose an option')
    computer = random.choice(the_game)
    print(computer)
    draw = user_input == computer
    # rock=paper
    # while attempts < max_attempts:
    remaining_attempts = int(max_attempts) - (int(attempts) + int(draw))
    # print(f"computer:{computer}")
    # print(f"user_input {user_input}")
    if user_input == computer:
        print("its a draw")

    elif user_input == "paper" and computer == "scissors":
        print('win one point')
    elif user_input == "rock" and computer == "scissors":
        print('win one point ')
    elif user_input == "scissors" and computer =="paper":
        print("win one point ")
    else:
        print('you lose')
    if point == 2:
        print("game over you win!")
    else:
        print("game over you lose")



    # print('you  have'+" "+str(remaining_attempts))
    # if user_input.__str__('rock') == random.choices(the_game.__str__('paper')):
    # # if user_input == computer:
    #         print('win')
    #         break
    # elif user_input.__str__('paper') in  random.choices(the_game.__str__('rock')):
    #      print('try again'+" "+ str(remaining_attempts))

# # breakpoint(max_attempts)

# def pick_random_keys_from_the_game(d:the_game):
#     key = list(d.keys),
#     random_key = random.choice(the_game.keys())
#     return random_key
# computer = dict([random.choice(list(the_game.items()))])
# print(computer)
# if computer:'input'
#     print(draw)
#     else if computer != input
#     print(loose)

# elf