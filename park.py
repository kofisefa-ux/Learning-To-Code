height = int(input("Enter your height in cm: "))

# 1. Catch impossible inputs first
if height <= 0:
    print("Error: Height cannot be zero or negative!")
elif height < 50:
    print("Error: Please re-enter a valid height.")

# 2. Do query for real heights
elif height >= 140:
    print("You are tall enough to ride the Thunder Mountain!")
elif height >= 130:
    with_adult = input("Are you with an adult? (yes/no): ").strip().lower()
    if with_adult == "yes":
        print("You can ride the Thunder Mountain with an adult!")
    else:
        print("Sorry, you have to go to the kiddie coaster.")
else:
    # if you are less than 130cm
    print("Sorry, you have to go to the kiddie coaster.")