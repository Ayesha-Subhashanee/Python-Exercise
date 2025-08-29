# prints out the smallest and largest number from the numbers it received

number_input = input("Enter a number (or press Enter to quit): ")

if number_input != "":
    number = float(number_input)
    smallest = number
    largest = number

    while number_input != "":
        number = float(number_input)
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        number_input = input("Enter a number (or press Enter to quit): ")

    print(f"Smallest number:", smallest)
    print(f"Largest number:", largest)
else:
    print("No numbers were entered.")

