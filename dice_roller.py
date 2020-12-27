import random

def main():
  player = int(input('Enter the number players: '))
  dice_num = int(input('Enter the number of dice to be rolled for each player: '))
  dice_size = int(input('Enter the size of the dice used for this game: '))
  player_rolls = []
  max = float('inf')
  winner = 0
  for i in range(0, player):
    roll_sum = 0
    for j in range(0, dice_num):
      roll = random.randint(1, 6)
      roll_sum += roll
    player_rolls.append(roll_sum)
    print(f'player{i+1} rolled  a sum of {roll_sum}')
    if player_rolls[i] <= max:
      max = player_rolls[i]
      winner = i+1
  print(f'player{winner} won')


if __name__ == "__main__":
    main()
