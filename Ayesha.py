def calculate(num1, num2):
    return num1 + num2 , (num1 + num2)/2
sum, average = calculate(2 , 3)
print(sum)
print(average)

def calculate(num1, num2):
    sum = num1 + num2
    average = sum / 2
    return sum, average
sum, average = calculate(2, 3)
print(sum)
print(average)


