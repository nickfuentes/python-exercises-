"""if the number is divisble by 3 then you print "Fizz"
if the number is divisble by 5 the you print "Buzz"
if the number is divisible by 3 and 5 then you print Fizz Buzz"""

number = int(input("Enter number: "))

if (number % 3 == 0) and number % 5 == 0:
    print(f"The number {number} is divisble by 3 and 5 FIZZ BUZZ!")
elif number % 3 == 0:
    print(f"The number {number} is divisble by 3 FIZZ!")
elif number % 5 == 0:
    print(f"The number {number} is divisble by 5 BUZZ!")
