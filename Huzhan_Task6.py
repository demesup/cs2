# Programming:Task 6
# Huzhan Sofiia, KB 14308564

print("‘Programming’:Task 4.3\nHuzhan Sofiia, KB 14308564")


def find_subtuple(tup1, tup2):
    index = None
    sub = None

    for i in range(len(tup1) - len(tup2) + 1):
        if tup1[i:i + len(tup2)] == tup2:
            index = i
            sub = tup2
            break

    if index is not None and sub is not None:
        result = (index, sub)
        return result
    else:
        return None


a = (2, 3, -4, 5, 8, 1)
b1 = (-4, 5, 8)
b2 = (8, 1)
b3 = (5, 8)

c = (2, 3)
d = (5, 6)
test = (b1, b2, b3, c, d)
for case in test:
    result = find_subtuple(a, case)
    if result is not None:
        print(result)
    else:
        print("Один кортеж не входить в інший.")
