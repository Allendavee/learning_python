while True:
    try:
        number = int(input("Enter a number: "))
        break

    except ValueError:
        print("You did not enter a number")

print("You entered {}".format(number))