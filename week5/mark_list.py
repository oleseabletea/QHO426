def average_ofmarks(marks):
    total=sum(marks)
    average = total/len(marks)
    return average

mark_list = list(map(int,input("Enter marks separately by space:").split()))
avg = average_ofmarks(mark_list)
print("the average marks is equal to", avg)

