#Ask the user for the number of rows
rows = int(input("How many rows should I have? "))

#Ask the user for the number of columns
columns = int(input("How many columns should I have? "))

#Display a message
print("\nHere I go:\n")

#Use nested loops to display the emoji grid
for row in range(rows):
    for column in range(columns):
        print(":-)", end=" ")
    print()
#Display completion message
print("\nDone!")
