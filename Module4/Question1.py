#print all numbers divisible by 3 in range 1-1000
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number = number + 1