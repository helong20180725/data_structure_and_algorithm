"""
This is a method to calculate the inversions in an array.
[1, 2, 5, 2]   inversion: i < j and a[i] > a[j]
We can use merge sort to do that.
"""


def merge(left, right, array, inversion):
    i, j = 0, 0
    while i + j < len(array):
        if j == len(right) or (i < len(left) and left[i] <= right[j]):
            array[i+j] = left[i]
            i += 1
        else:
            inversion += len(left) - i
            array[i+j] = right[j]
            j += 1
    return inversion


def merge_sort(array, inversion, level):
    if len(array) <= 1:
        # print("-"*level+"{}".format(array))
        return 0
    mid = len(array) // 2
    left_a = array[:mid]
    # print("---------"*level+"{}".format(left_a))
    right_a = array[mid:]
    # print("---------"*level+"{}".format(right_a))
    level += 1
    inversion_left = merge_sort(left_a, inversion, level)
    inversion_right = merge_sort(right_a, inversion, level)
    inversion += inversion_left + inversion_right
    inversion = merge(left_a, right_a, array, inversion)
    print("------"*level+"{}".format(left_a))
    print("------"*level+"{}".format(right_a))
    print("------"*level+"{}".format(array))
    print("------"*level+"inversions: {}".format(inversion))
    return inversion
if __name__ == "__main__":
    test = [5, 4, 3, 2, 1]
    print(merge_sort(test, 0, 0))
    print(test)
