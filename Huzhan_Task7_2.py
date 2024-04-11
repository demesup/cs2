# Напишіть рекурсивну функцію, яка перемножує два натуральних числа, не
# використовуя операції множення.

def get_int(var_name):
    while True:
        try:
            i = int(input("Enter {} (natural number): ".format(var_name)))
            if i > 0:
                return i
        except ValueError:
            print("Enter a natural number(>0)")


def multiply(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return -multiply(a, -b)
    else:
        return a + multiply(a, b - 1)


while True:
    a = get_int("a")
    b = get_int("b")
    print(multiply(a, b))
