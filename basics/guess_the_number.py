import random

print("=========  Guess The Number  ==========")

guess = random.randint(1, 10)
response = int(input("\nGuess the number [1-10]: "))
message = ""

if response < 1 or response > 10:
    print("\nSilly! The number must be in the range 1-10")
    exit(1)

if guess == response:
    message = "\nGreat, you won!"
else:
    message = "\nHahaha, you lose!"

print(message)
print("The winning number was {}".format(guess))
