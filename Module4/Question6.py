#program that draws two random combinations of numbers for a combination lock
import random

code3 = "".join(str(random.randint(0, 9)) for _ in range(3))

code4 = "".join(str(random.randint(1, 6)) for _ in range(4))

print(f"3-digit code: {code3}")
print(f"4-digit code: {code4}")