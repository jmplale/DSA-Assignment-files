# Exercise 2 - Ohm’s Law Calculator

calculate = input("What do you want to calculate? Voltage, Current, or Resistance?: ")
unit = ''
result = 0

if calculate.lower() == 'voltage':
  current = float(input("Enter the current: "))
  resistance = float(input("Enter the resistance: "))
  unit = 'V'
  result += (current * resistance)

elif calculate.lower() == 'current':
  resistance = float(input("Enter the resistance: "))
  if resistance == 0:
    print("The result is undefined.")
    exit()
  else:
    voltage = float(input("Enter the voltage: "))
    unit = 'I'
    result += (voltage / resistance)


elif calculate.lower() == 'resistance':
  current = float(input("Enter the current: "))
  if current == 0:
    print("The result is undefined.")
    exit()
  else:
    voltage = float(input("Enter the voltage: "))
    unit = 'R'
    result += (voltage / current)

else:
  print("Please choose a valid option!")
  exit()

print(f"Answer: {result} {unit}")