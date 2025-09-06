# Create a function calculate_unit_price
import math


def calculate_unit_price(diameter_cm, price_euros):
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * (radius_cm ** 2)
    area_m2 = area_cm2 / 10000
    unit_price = price_euros / area_m2
    return unit_price


# Main program
d1 = float(input("Enter the diameter of the first pizza (cm):"))
p1 = float(input(" Enter the price of the first pizza (euros):"))
d2 = float(input(" Enter the diameter of the second pizza (cm):"))
p2 = float(input(" Enter the price of the second pizza (euros):"))

unit1 = calculate_unit_price(d1, p1)
unit2 = calculate_unit_price(d2, p2)

print(f" Unit price of the first pizza: {unit1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit2:.2f} euros/m²")

if unit1 < unit2:
    print("The first pizza provides better value for money.")
elif unit2 < unit1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
