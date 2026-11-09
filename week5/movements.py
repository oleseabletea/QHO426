def movement():
    path = ["Move Forward", 10, "Move Backward", 5, "Turn Left", 3, "Turn Right", 1]
    return path

def run_task2():
    print("Moving...")

    path = movement()

    for i in range(0, len(path), 2):
        direction = path[i]
        steps = path[i+1]

        print(f"{direction} for {steps} steps")

run_task2()
