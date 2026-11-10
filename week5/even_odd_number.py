def count_even(numbers):
    count = 0
    for num in numbers:
        if num%2 == 0:
            count =count+1
        return count
my_numbers = [12,13,5,7]
result = count_even(my_numbers)
print("The number of even numbers in the list are ",result)
