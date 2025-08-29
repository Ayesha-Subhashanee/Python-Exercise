# converts inches to centimeters until the user inputs a negative vale

length = float(input("Enter length in inches (negative value to quit): "))

while length >= 0:
    centimeters = length * 2.54
    print(f"{length:.1f} inches is {centimeters:.2f} centimeters")
    length = float(input("Enter length in inches (negative value to quit): "))

print("Program ended.")