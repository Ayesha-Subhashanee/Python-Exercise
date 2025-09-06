# Function definition
def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return liters


# Main program
while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallons < 0:
        print("Program finished.")
        break

    liters = gallons_to_liters(gallons)
    print(f"{gallons:.1f} American gallons is {liters:.2f} liters.")
