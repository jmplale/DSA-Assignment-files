# Exercise 1 - Temperature Converter

try:
  temperature = float(input("Please enter a temperature: "))
  conversion = input("\n1. From Celsius to Fahrenheit\n2. From Fahrenheit to Celsius\nSelect a conversion type (1 or 2): ")
  unit = ''

except ValueError:
  print("You entered a wrong input.")
  exit()

if conversion == '1':
  unit = '°F'
  print(f"\n{(temperature * 9/5) + 32} {unit}")

elif conversion == '2':
  unit = '°C'
  print(f"\n{(temperature - 32) * (5/9)} {unit}")

else:
  print("Sorry, you entered an invalid character/s.")