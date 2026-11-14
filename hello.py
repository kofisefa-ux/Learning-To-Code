age = int(input("Enter your age: "))
if age < 13:
    price = 8.00
elif age >= 65:
    price = 9.00
else:
    price = 12.00
# Check for the type of movie
def movietype():
    movie = input("Do you want to watch a standard or 3d movie? ")
    if movie == "standard":
        newprice = price
    elif movie == "3d":
        newprice = price + 3.00
    else:
        print("Invalid movie type. Please enter 'standard' or '3d'.")
        return movietype()  # If input is wrong.
    return newprice
#final price of ticket
final_price = movietype()
print(f"The final ticket price is: ${final_price:.2f}")