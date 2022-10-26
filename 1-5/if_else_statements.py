print("Welcome to the roller coaster")
height = int(input("what is your height in cm?"))


if height >= 120:  # remember to put the colon after the if statement
    print("You can ride the roller coaster")
    age = int(input('What is your age?'))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:  # <-- remember to put the colon after
    print("Sorry, you have to grow taller before you can ride.")


