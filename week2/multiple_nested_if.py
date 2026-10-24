#Program to find a missing phone using nested if statements
#Ask the user where to look
location = input("Where should I look?\n")

#Check the bedroom
if location =="in the bedroom":
    place =input("Where in the bedroom should I look?\n")

    if place =="under the bed":
        print("Found some shoes nut no phone")
    else:
        print("Found some mess but no phone.")

#Check the bathroom
elif location =="in the bathroom":
    place=input("Where in the bathroom should I look?\n")
    if place ==("in the bathtub"):
        print("Found a rubber duck but no phone")
    else:
        print("Found a bathroom stuff but no phone.")

#Check the living room
elif location =="in the living room":
    place=input("Where in the living room should I look?\n")
    if place =="on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
#If the location is unknown
else:
    print("I do not know where that is but I will keep looking.")



