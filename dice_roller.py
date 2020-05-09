import random

def main():
  dice_sum = 0
  dice_size = int(input('How many sides does the dice have?'))
  dice_rolls = int(input('How many times would you roll the die?'))
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll} critical fail')
    elif roll == dice_size:
      print(f'You rolled a {roll} critical success')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
