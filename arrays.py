# Arrays/ List
# Use plural name when using arryas like single variable number but an arrays would be numbers
# Index in arrays always start at 0 so 0 is the 1 stop in the array
# To access the array index it will be in the [] syntax

number = 10

name = "John"

pi = 3.142

# Array of numbers
numbers = [1, 4, 6, 7, 8, 10, 23, 45, 26, 11, 34, 20, 15, 19]
print(len(numbers))

# Range is a function in python
# for index in range(0, len(numbers),2): this will skipp two numbers at a time three arguments, Skip or Step operator (For Loop)
for index in range(0, len(numbers)):
    number = numbers[index]
    print(f"The value on index {index} is {number}")

# for each loop no access to index from start to end not offical name in python
for number in numbers:
    print(number)

# Stores the number in the array into a variable than prints it out
number = numbers[4]
print(number)

# Directly prints out the number from the array instead of storing it into a variable
print(numbers[5])

# Array of strings
names = ["Nick", "Mary", "Alex", "Jerry"]

# Array of numbers and names
numbersAndNames = ["Alex", 10, 5, "Nick"]
