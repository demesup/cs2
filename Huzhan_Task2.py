import math


# Programming Lab2

def get_float(var_name):
    while True:
        try:
            return float(input("Enter {}: ".format(var_name)))
        except ValueError:
            print("Enter a number")


print("‘Programming’:Task 2")
print("Huzhan Sofia, KB 14308564")

impossible_odz = math.log(37.5, 19 / 5)

# to avoid using Decimal
possible_odz = 530
while True:
    try:
        math.pow(3.8, possible_odz + 0.1)
        possible_odz += 0.1

    except OverflowError:
        break

x = get_float("x")
print("2 ways to destroy the world: \n\ty = {}\n\ty = {}".format(impossible_odz, possible_odz))
y = get_float("y")
z = get_float("z")

while y > possible_odz or math.isclose(y, impossible_odz):
    y = get_float("y, the last one will destroy the world (")

print((x + z / 8) / (18.2 + 19.3 - math.pow(3.8, y)))
