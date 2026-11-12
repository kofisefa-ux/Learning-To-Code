def main():
    # input
    D = float(input("Enter distance in km: "))
    R = float(input("Enter fuel rate in litres/100km: "))
    P = float(input("Enter price/litre in $: "))
    N = int(input("Enter Number of passengers: "))

    # calculations
    F = (D * R) / 100
    C = F * P
    S = C / N

    # output
    print("\n")
    print(f"Distance Travelled: {D} km")
    print(f"Total Fuel Required:{F:.2f} litres")
    print(f"Total Fuel Cost: ${C:.2f}")
    print(f"Cost per Passenger: ${S:.2f}")
    print("\n")


main()