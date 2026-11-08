import random
def play_gues_the_number():
    min_value = int(input("Please enter a minimum value: "))
    max_value = int(input("Please enter a maximum value: "))

    #Generate a random number1
    number = random.randint(min_value, max_value)

    print(f"I am thinking of a number between {min_value} and {max_value}.Can you guess what it is?")
    guess =int(input())
    while guess != number:
        if guess < number:
            print(f"Your guess is too low.")
        elif guess > number:
            print(f"Your guess is too high.")
        print("Try again:")
        guess = int(input())
    print("Congratulations! You guessed the number!")
play_gues_the_number()