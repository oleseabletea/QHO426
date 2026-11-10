def average_ofmarks(marks):
    total=sum(marks)
    average = total/len(marks)
    return average

mark_list = [23,44,46,12,13,6]
avg = average_ofmarks(mark_list)
print("the average marks is equal to", avg)

