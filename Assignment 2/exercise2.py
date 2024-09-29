sizeArray = int(input("Enter the size of the array: "))
elements = input("Enter the elements separated by space: ").split()

container = []

for index in elements:
  container.append(int(index))

if sizeArray != len(elements):
  print("Sorry, the length of the array does not matched what you've entered.")

else:
  for index in container:
    print(int(index) ** 3)
