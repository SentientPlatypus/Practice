import random


def print_greeting(tries):
  print("Welcome to the game!")
  print("You get " + str(tries) + " rolls.")
  print("If you roll a 1, your money is divided by 2")
  print("If you roll a 2, 3, or 4, you gain the amount you rolled")
  print("If you roll a 5, you gain 10")
  print("If you roll a 6, your money is doubled")
  print()
  print()


def take_single_turn(total_money, turn, tries):
  roll = random.randint(1, 6)
  print("Roll " + str(turn+1) + ": You rolled a " + str(roll))

  if (roll == 1):
    total_money /= 2

  if (roll == 2 or roll == 3 or roll == 4):
    total_money += roll

  if (roll == 5):
    total_money += 10 

  if (roll == 6):
    total_money *= 2

  print("You have $" + str(total_money) + ", and " + str(tries - turn - 1) +
       " rolls left.")
  print()
  return total_money

def take_turns(tries, total_money=10):
    turn = 0
    while turn < tries and total_money >= 3:
        total_money = take_single_turn(total_money=total_money, turn=turn, tries=tries)
        turn += 1
    print("Game over! You made $" + str(total_money) + "!")

def play_game():
    total_money = 10
    tries = int(input("How many tries do you want?\t"))
    print_greeting(tries)
    take_turns(tries, total_money)


if __name__ == '__main__':
  random.seed(5)
  play_game()


## Test cases

def test_normal():
  random.seed(5)
  assert take_turns(5) == (50, 5)


def test_end_early():
  random.seed(5)
  output = take_turns(10)
  print(output)
  assert take_turns(10) == (2.5, 5)


def test_long():
  random.seed(5)
  assert take_turns(30) == (20.625, 30)