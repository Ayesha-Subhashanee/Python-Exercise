length_str = input("Enter the length of the rectangle: ")
length = float(length_str)

width_str = input("Enter the width of the rectangle: ")
width = float(width_str)

perimeter = 2 * (length + width)
area = length * width

print(f"The perimeter of the rectangle is {perimeter}")
print(f"The area of the rectangle is {area}")
