# Collect numbers until the user enters an empty  string  to stop
numbers = []

# ask for the first number
num = input("Enter a number: ")

# keep asking until user press Enter
while num != "":
    numbers.append(float(num))
    num = input("Enter a number: ")

numbers.sort(reverse=True)

print("The greatest numbers in descending order:")
for n in numbers[:5]:
    print(n)