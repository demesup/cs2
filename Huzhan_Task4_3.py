# Programming:Task 4.1
# Huzhan Sofiia, FB-31, 11

print("‘Programming’:Task 4.3")
print("Huzhan Sofiia, FB-31, 11")


def get_positive_float(message):
    while True:
        try:
            f = float(input(message))
            if f >= 0:
                return f
        except ValueError:
            print(message)


def heron_iteration(a, x):
    while x != 0:
        next_x = 0.5 * (x + a / x)
        if abs(next_x - x) < 0.0001:
            return next_x
        x = next_x
    return 0


const = 23

initial = get_positive_float("Enter initial value(positive number): ")
result = heron_iteration(const, initial)
print(f"Square root of {const} starting from {initial} with accuracy 0.0001: {result:.4f}")
