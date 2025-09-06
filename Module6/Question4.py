#Write a function named sum_of_list
def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers)
print(f"The sum of the numbers in the list is: {result}")
