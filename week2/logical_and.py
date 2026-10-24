#Program to explore the dark forest
#Ask the user what they heard
sound = input("What did I hear?\n")

#Ask the user what they saw
sight = input("What did I see?\n")

#Check both conditions using the AND operator
if sound == "grrr" and sight == "two red eyes":
    print("There is a scary creature.I should get out of here!")
else:
    print("I am a little scared but I will continue!")
