no_of_obstacles = int(input("How many obstacles should I avoid?"))
obstacle_avoided = 0
while obstacle_avoided < no_of_obstacles:
    print("Avoiding...", end="")
    obstacle_avoided = obstacle_avoided + 1
    print(f"Done! {obstacle_avoided} obstacles avoided.")
print("All obstacles have been avoided.")