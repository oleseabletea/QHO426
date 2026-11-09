color = ["red", "white", "black","pink","purple"]
print(len(color))
number=[56,20,49,6.5,2.7]
print(len(number))
print(max(number))
print(number[3])
print(color[0])
print(color[-1])
print(number[-1])
print(number[-2])
if "green" in color:
    print("yes white is in the given list color")
else:
    print("sorry! not found")
color = ["red", "white", "black","pink","purple"]
color[2]="green"
print(color)