def check():
    if height >= 140:
        return True
    elif height >= 130 and with_adult == "yes":
        return True
    else:
        return False
    
height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))
with_adult = input("Are you with an adult? (yes/no): ").strip().lower()
if check() == True:
    print("You are allowed to ride the Thunder Mountain!")
else:
    print("Sorry, you have to go to the kiddie coaster.")
