# Get the kth small value in a unsorted array
# Average O(n)
from random import randint


def partition(a, begin, end):
    p_index = randint(begin, end)
    p_value = a[p_index]

    a[p_index], a[end] = a[end], a[p_index]
    flag_index = begin

    # The end index is not in the range
    for i in range(begin, end):
        if a[i] < p_value:
            a[flag_index], a[i] = a[i], a[flag_index]
            flag_index += 1
    a[flag_index], a[end] = a[end], a[flag_index]
    return flag_index


def quick_select(a, k, begin, end):
    # special case
    if k < 0 or k > len(a):
        print('Out of range')
        return False

    if begin == end:
        return a[begin]

    pivot = partition(a, begin, end)

    if pivot == k - 1:
        return a[pivot]
    elif pivot < k - 1:
        return quick_select(a, k, pivot+1, end)
    else:
        return quick_select(a, k, begin, pivot-1)

if __name__ == '__main__':
    a = [4, 2, 0, 10, 2, 22, 34, 88, 23, 2, 1, 12, 122, 345, 111, 90]

    k = 7
    print(quick_select(a, k, 0, len(a)-1))
