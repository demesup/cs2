
def get_float(var_name, condition=lambda v: False):
    while True:
        try:
            i = float(input("Enter {}: ".format(var_name)))
            if not condition(i):
                return i
            else:
                raise ArithmeticError("Value does not meet the condition.")
        except ValueError:
            print("Enter a number")
        except ArithmeticError as e:
            print(e)


def abs(number):
    if number < 0:
        return -number
    return number


def term(n, x):
    if n == 0:
        return 1
    return term(n - 1, x) * x / n


def e_power(x, epsilon=1e-4):
    return approximation(x, 1, 1, epsilon)


def approximation(x, n, sum_prev, epsilon):
    sum_current = sum_prev + term(n, x)
    if abs(sum_current - sum_prev) < epsilon:
        return sum_current
    else:
        return approximation(x, n + 1, sum_current, epsilon)


def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


print(e_power(4))

z = get_float("z")
# Ми не вчили лямбда-вирази, проте я вважаю, що тут їх доречно використати, щоб не писати через if
x = get_float("x", lambda x: z == 0 and x == 1)
try:
    y = (x + e_power(z - 1)) / (1 - x * x * abs(x - z))
    print(y)
except RecursionError as r:
    print(r)
