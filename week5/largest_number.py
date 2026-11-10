def largest_number(numbers):
    largest=max(numbers)
    return largest
def smallest_number(numbers):
    smallest=min(numbers)
    return smallest

mylist=[12,4,5,22,34,100]
result=largest_number(mylist)
result2=smallest_number(mylist)

print("The largest number is",result)
print("The smallest number is",result2)
