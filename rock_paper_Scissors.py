import random

def player_input():
    player_pick = ''
    while not (player_pick== 'rock' or player_pick == 'paper' or player_pick == 'scissors'):
        player_pick = input('Choose Rock, Paper or Scissors: ').lower()
    return player_pick

count_player = 0
count_computer = 0

while True:
    computer_choice = random.choice(['rock','paper','scissors'])
    player_choose = player_input()
    
    if player_choose == 'rock' and computer_choice == 'scissors' or player_choose == 'paper' and computer_choice == 'rock' or player_choose == 'scissors' and computer_choice == 'paper':
        print('Player wins')
        count_player += 1
        print(f"Player {count_player} and Computer {count_computer}")
    elif player_choose == computer_choice:
        print('Draw')
    else:
        print('Computer wins')
        count_computer += 1
        print(f"Player {count_player} and Computer {count_computer}")
    
    q = input("Do you want to play or q: ")
    
    if q[0].lower().startswith('q'):
        break


