#Ask user which direction the robot should move
print("Towards which directions should i go(up, down, left, right)?")
direction = input()

#Check the direction entered by the user
if direction == "up":
    print("I am moving in an upwards direction!")

elif direction == "down":
    print("I am moving in an downwards direction!")

elif direction == "left":
    print("I am moving in an leftwards direction!")

elif direction == "right":
    print("I am moving in an rightwards direction!")

else:
    print("Invalid direction!")
