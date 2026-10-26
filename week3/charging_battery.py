#Ask the user how many bars to charge
no_of_bars = int(input("How many bars should be charged? "))

#Start with zero charged bars
charged_bars = 0

#Keep charging until the required number is reached
while charged_bars < no_of_bars:
    print("Charging:", end=" ")
    charged_bars = charged_bars + 1
    print(" " * charged_bars)

#Display the final message
print("The battery is fully charged.")
