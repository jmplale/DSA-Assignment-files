# Exercise 3 - Diamond Shape (advance topic):

def print_diamond(number):
  try:

    if number % 2 == 0:
      print("Please provide an odd integer!")
      exit()

  except ValueError:
    print("You entered an invalid input!")
    exit()

  for index in range(1, number + 1):
    if index % 2 != 0:
      print(f"{' ' * ((number - index) // 2) + ('*' * index)}")

  for secondIndex in range(number-2, 0, -1):
    if secondIndex % 2 != 0:
      print(f"{' ' * ((number - secondIndex) // 2) + ('*' * secondIndex)}")

print_diamond(5)