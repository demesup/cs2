# import sys
# def merge_lists(list1, list2): # O(n+m), де n - кількісмть елементів в list1, m - в list2
#     """
#     Merge two sorted lists into one sorted list.
#     >>> merge_lists([1, 3, 5, 7], [2, 4, 6, 8])
#     [1, 2, 3, 4, 5, 6, 7, 8]
#
#     >>> merge_lists([1, 2, 3], [4, 5, 6])
#     [1, 2, 3, 4, 5, 6]
#
#     >>> merge_lists([1, 3, 5, 7], [])
#     [1, 3, 5, 7]
#
#     >>> merge_lists([], [2, 4, 6, 8])
#     [2, 4, 6, 8]
#     """
#
#     merged = []
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
#
#     merged += list1[i:]
#     merged += list2[j:]
#     return merged
#
# def check_sorted(list):
#     """
#     >>> check_sorted([1, 2, 3, 4, 5])
#     >>> check_sorted([5, 4, 3, 2, 1])
#     Traceback (most recent call last):
#         ...
#     SystemExit: 1
#     >>> check_sorted([])
#     """
#     if any(list[i] > list[i+1] for i in range(len(list)-1)): # O(n), де n - кількість елементів списку
#         print("List is not sorted: ", list)
#         sys.exit(1)
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
