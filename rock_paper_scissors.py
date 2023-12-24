import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'

player_choice = input('Choose [r]ock, [p]aper or [s]cissors: ')

if player_choice == 'r':
    player_choice = rock
elif player_choice == 'p':
    player_choice = 'paper'
elif player_choice == 's':
    player_choice = 'scissors'
else:
    raise SystemExit('Invalid input. Try again...')

computer_random_choice = random.randint(1, 3)
computer_selection = ''
if computer_random_choice == 1:
    computer_selection = rock
    print(f'The computer chose {computer_selection}.')
elif computer_random_choice == 2:
    computer_selection = paper
    print(f'The computer chose {computer_selection}.')
else:
    computer_selection = scissors
    print(f'The computer chose {computer_selection}.')

if (player_choice == rock and computer_selection == scissors) or\
        (player_choice == paper and computer_selection == rock) or\
        (player_choice == scissors and computer_selection == paper):
    print('You win!')
elif player_choice == computer_selection:
    print('Draw!')
else:
    print('You lose!')