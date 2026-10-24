#Set the counters to zero
even_count = 0
odd_count = 0
#Ask the user to enter tree whole numbers
print("Please enter the first  whole number.")
number1 = int(input())
print("Please enter the second whole number.")
number2 = int(input())
print("Please enter the third whole number.")
number3 = int(input())
#Check whether the first  number is even or odd
if number1 % 2 == 0:
    even_count

else:
    odd_count += 1
#Check whether the second number is even or odd
if number2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
#Check whether the third number is even or odd
if number3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
#Display the total even and odd numbers
print(f"There were {even_count} even and {odd_count} odd numbers.")

