from math import *

# ‘Programming’, Task 1"
# Huzhan Sofiia, FB-31, KB 14308564

print("‘Programming’:Task 3")
print("Huzhan Sofiia, FB-31, KB 14308564")

while True:
    try:
        x = float(input("Enter x: "))
        break
    except ValueError:
        print("Enter a number")

first = x ** 2 - 4.0
if first > 0 and log(first) > 0:
    print(sqrt(log(pow(x, 2) - 4.0)))

else:
    print("""Значення x виходить за область визначення функції:
                        (-нескінченність; -sqrt(5)) U (sqrt(5); +нескінченність)""")
