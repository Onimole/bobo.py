import random

numbers = []

for _ in range(10):
    num = random.randrange(10, 100)
    numbers.append(num)

print(numbers)
