import random

def main():
  player = 2
  player_rolls = []
  max = 6
  winner = 0
  for i in range(0, player):
    roll = random.randint(1, 6)
    player_rolls.append(roll)
    dice_sum += roll
    print(f'player{i+1} rolled {roll}')
    if player_rolls[i] <= max:
      max = player_rolls[i]
      winner = i+1
  print(f'player{winner} won')


if __name__ == "__main__":
    main()
