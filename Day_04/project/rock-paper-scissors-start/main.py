import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("Press 1 if you want to play with the computer or 2 if you want to play with another human: ")
answer = int(input())
###########################################################################
# delete this when you are done and check for "not playing with bot"
playing_with_bot = False
###########################################################################
if answer == 1:
    playing_with_bot = True
    player2_weapon = random.randint(0, 2)
    player1_weapon = int(input("Player 1, choose your weapon (Type 0 for Rock, 1 for Paper or 2 for Scissors.)\n"))
else:
    player1_weapon = int(input("Player 1, choose your weapon (Type 0 for Rock, 1 for Paper or 2 for Scissors.)\n"))

    player2_weapon = int(input("Player 2, choose your weapon (Type 0 for Rock, 1 for Paper or 2 for Scissors.)\n"))

game_drawn = False
player1_win = False
player2_win = False

################################################
# change rock back to None after you are done
weapon1 = None
weapon2 = None
################################################


if player1_weapon == 0:
    weapon1 = rock
elif player1_weapon == 1:
    weapon1 = paper
else:
    weapon1 = scissors

if player2_weapon == 0:
    weapon2 = rock
elif player2_weapon == 1:
    weapon2 = paper
else:
    weapon2 = scissors

if weapon1 == rock:
    if weapon2 == rock:
        pass
    elif weapon2 == paper:
        player2_win = True
    elif weapon2 == scissors:
        player1_win = True

elif weapon1 == paper:
    if weapon2 == rock:
        player1_win = True
    elif weapon2 == paper:
        pass
    elif weapon2 == scissors:
        player2_win = True

elif weapon1 == scissors:
    if weapon2 == rock:
        player2_win = True
    elif weapon2 == paper:
        player1_win = True
    elif weapon2 == scissors:
        pass

if not player1_win and not player2_win:
    game_drawn = True

# Show the result
if not playing_with_bot:

    if player1_win:
        print(f"Player 1 chose:\n{weapon1}")
        print(f"Player 2 chose:\n{weapon2}")
        print("Player 1 wins!")
    elif player2_win:
        print(f"Player 1 chose:\n{weapon1}")
        print(f"Player 2 chose:\n{weapon2}")
        print("Player 2 wins!")
    else:
        print(f"Player 1 chose:\n{weapon1}")
        print(f"Player 2 chose:\n{weapon2}")
        print("The game is a draw!")

else:
    if player1_win:
        print(f"Player 1 chose:\n{weapon1}")
        print(f"I chose chose:\n{weapon2}")
        print("You win!")
    elif player2_win:
        print(f"You chose:\n{weapon1}")
        print(f"I chose chose:\n{weapon2}")
        print("I win!")
    else:
        print(f"You chose:\n{weapon1}")
        print(f"I chose:\n {weapon2}")
        print("The game is a draw!")
