import random

N = int(input("Enter the number of random points: "))

inside_circle = 0
i = 0

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y <= 1:
        inside_circle += 1
    i += 1

pi_approx = 4 * inside_circle / N

print(f"Approximation of pi: {pi_approx:.4f}")