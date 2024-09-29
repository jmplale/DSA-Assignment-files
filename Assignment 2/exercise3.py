ranges = int(input("Enter the side length of the square: "))

for index in range(ranges):
  if index == 0 or index == ranges - 1:
    print('x' * ranges)
  else:
    print('x' + ' ' * (ranges - 2) + 'x')