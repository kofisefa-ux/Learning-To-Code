age = int(input("How old are you? "))
if age < 18:
    print("You cant work here")
elif age >= 60:
    print("You are too old to work here")
elif age >= 18:
    print("You can work here")