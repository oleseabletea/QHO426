#Mini adventure game
#Demonstrates decision, nesting and logical operators

#Ask the user to choose an adventure
adventure = input("Choose an adventure (forest, cave, beach):")
#Check the chosen adventure
if adventure == "forest" or adventure == "cave" :
    print("You are going on a dangerous adventure!")
    #Ask if the user has a torch
    torch = input("Do you have a torch?(yes/no):")
    #Nested  decision using AND
    if torch == "yes" and adventure == "cave" :
        print("You can explore the dark cave safely!")
    elif torch == "yes" and adventure == "forest":
        print("You can explore the forest!")
    else:
        print(" It is to dark to explore!")
#Check if the user chose the beach
elif adventure == "beach":
    print("You are going on a relaxing adventure!")
    #Ask about the weather
    weather = input("Is it sunny?(yes/no):")
    #Use the NOT operator
    if not weather == "yes":
        print("It might rain, so take an umbrella!")
    else:
        print("Enjoy the sunshine!")
#Handle an unknown adventure
else:
    print("That adventure is not available!")
