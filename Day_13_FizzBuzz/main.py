# Target is the number up to which we count
print("\nWelcome to FizzBuzz!!\n")
target = int(input("Enter the range: "))
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number) # remove square brackets []