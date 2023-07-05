import random

secrete_number = random.randrange(1,11)

while True:
    try:
        guess = int(input("Guess a random number between 1 and 10: "))
        if guess == secrete_number:
            break
        else:
            print("try again")
    except ValueError:
        print("You did not enter a valid guess")

print("Congratulations!")