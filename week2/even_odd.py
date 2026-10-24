#Ask the user to enter a whole number
print("Plase enter a whole number.")
number = int(input())

#Check whether the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is an even number.")
else:
    print(f"The number {number} is an odd number.")
