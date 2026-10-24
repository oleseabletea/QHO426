#Program to create a mini adventure
#Ask the user to choose an adventure
adventure = input("What type of adventure should I have?\n")
#Check if the adventure is scary or short
if adventure == "scary" or adventure == "short":
    print("Entering the dark forest!")

#Check if the adventure is safe or long
elif adventure == "safe" or adventure == "long":
    print("Taking the safe route!")

#If the adventure type is unknown
else:
    print("Not sure which route to take.")