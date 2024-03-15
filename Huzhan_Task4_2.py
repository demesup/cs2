# Programming:Task 4.1
# Huzhan Sofiia, FB-31, 11

print("‘Programming’:Task 4.2")
print("Huzhan Sofiia, FB-31, 11")


def get_int():
    while True:
        try:
            return int(input("Enter a number(int): "))
        except ValueError:
            print("Enter a number")


n = abs(get_int())
count = 0

if n == 0:
    count = 1
while n > 0:
    count += 1
    n //= 10

print("The number of digits in {}: {}".format(n, count))
