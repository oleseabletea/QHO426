print("What level of brightness is required?")
brightness = int(input())
print("\nAdjusting brightness...")
for brightness_level in range(2,brightness+1,2):
    stars="*"*brightness_level
    print(f"Brightness level: {stars}")
print("\nCompleted.")
