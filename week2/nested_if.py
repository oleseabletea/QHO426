#Program to classify books based on their cover type
#Ask the user for the book cover type
cover=input("What type of cover does the book have?")
#Check if the book has a soft cover
if cover == "soft":
    #Ask if the book is perfect-bound
    bound = input("Is the book perfect-bound?")

    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft cover with coils or stitches are great for short books")

#Check if the book has a hard cover
elif cover == "hard":
    print("Books with hard covers can be more expensive!")

