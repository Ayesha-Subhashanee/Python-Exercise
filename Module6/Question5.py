# Write a function named filter_even_numbers
def filter_even_numbers(numbers):
    evens = []
    for n in numbers:
        if n % 2 == 0:
            evens.append(n)
    return evens


# Main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)

print(f"Original list: {original_list}")
print(f"List with even numbers only: {filtered_list}")