from math import *

# Programming:Task 4.1
# Huzhan Sofiia, FB-31, 11

print("‘Programming’:Task 4.1")
print("Huzhan Sofiia, FB-31, 11")

index = 0
current = 0
summary = 0

while True:
    current = (factorial(index) ** 2) / (2 ** (index ** 2))
    print("Current element {:10f} with index {}".format(current, index))
    if not (abs(current) > 0.0001 or isclose(current, 0.0001)):
        break
    summary += current
    index += 1

print("The sum of the series is {}".format(summary))
