def direction():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu():
    print("Please select a direction:")

    direction_list = direction()

    for i in range (len(direction_list)):
        print(f"{i}. {direction_list[i]}")

def run_task3():
    menu()

run_task3()
