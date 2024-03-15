print("‘Programming’:Task 8")
print("Huzhan Sofiia, FB-31, 11")


# 11)Дано список. Відібрати ті елементи, які менше за деяке число, помістити їх в новий
# список та відсортувати отриманий список

def bubble_sort(lst):
    """
    >>> bubble_sort([5, 3, 8, 4, 2, 7, 6, 1])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> bubble_sort([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> bubble_sort([])
    []
        """
    changed = True
    last_to_check = len(lst) - 1
    pass_num = 1

    while changed:
        changed = False
        for i in range(last_to_check):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                changed = True
        pass_num += 1
    return lst


def insertion_sort(lst):
    """
    >>> insertion_sort([5, 3, 8, 4, 2, 7, 6, 1])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> insertion_sort([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> insertion_sort([])
    []
        """
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1
        while j >= 0 and current < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current
    return lst


def get_index_of_smallest(lst, i):
    index_of_smallest = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[index_of_smallest]:
            index_of_smallest = j
    return index_of_smallest


def selection_sort(lst):
    """
    >>> selection_sort([5, 3, 8, 4, 2, 7, 6, 1])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> selection_sort([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> selection_sort([])
    []
    """
    for i in range(len(lst)):
        index_of_smallest = get_index_of_smallest(lst, i)
        lst[i], lst[index_of_smallest] = lst[index_of_smallest], lst[i]
    return lst


def filter_and_sort(lst, num, sort_algorithm):
    """
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 5, bubble_sort)
    [1, 2, 3, 4]
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 5, insertion_sort)
    [1, 2, 3, 4]
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 5, selection_sort)
    [1, 2, 3, 4]
    >>> filter_and_sort([52, 23, 28,54, 62,97], 5, bubble_sort)
    []
    >>> filter_and_sort([52, 23, 28,54, 62,97], 5, insertion_sort)
    []
    >>> filter_and_sort([52, 23, 28,54, 62,97], 5, selection_sort)
    []
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 50, bubble_sort)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 50, insertion_sort)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> filter_and_sort([5, 3, 8, 4, 2, 7, 6, 1], 50, selection_sort)
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> filter_and_sort([], 5, insertion_sort)
    []
    """
    return sort_algorithm([i for i in lst if i < num])


if __name__ == '__main__':
    import doctest

    doctest.testmod()
