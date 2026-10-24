#Ask the user to enter the first number
print("Please enter the first number.")
number1 = int(input())

#Ask the user to enter the second number
print("Please enter the second number.")
number2 = int(input())

#Compare the two numbers
if number1  < number2:
    print(f"The first number is the smallest!")
elif number1 > number2:
    print(f"The second number is the largest!")
else:
    print("Both numbers are equal!")
