# min-heap
class Heap:

    def __init__(self):
        self.data = []

    def _parent(self, index):
        # relation between child and parent : index(left_child) = 2 * index(parent) + 1
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """
        (0)
        |______(1)
        |      |______(3)
        |      |      |______(7)
        |      |      |______(8)
        |      |______(4)
        |             |______(9)
        |             |______(10)
        |______(2)
               |______(5)
               |______(6)
        """
        # index(right_child)=2*index(parent) + 2
        return (index - 1) // 2

    def _left(self, index):
        return 2 * index + 1

    def _right(self, index):
        return 2 * index + 2

    def _has_left(self, index):
        return len(self.data) > self._left(index)

    def _has_right(self, index):
        return len(self.data) > self._right(index)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _up_heap(self, index):
        parent = self._parent(index)
        if index > 0 and self.data[parent] > self.data[index]:
            self._swap(index, parent)
            self._up_heap(parent)

    def _down_heap(self, index):
        if self._has_left(index):
            small_child = self._left(index)
            if self._has_right(index):
                right = self._right(index)
                if self.data[right] < self.data[small_child]:
                    small_child = right
            if self.data[small_child] < self.data[index]:
                self._swap(index, small_child)
                self._down_heap(small_child)

    def push(self, value):
        self.data.append(value)
        self._up_heap(len(self.data) - 1)

    def get(self):
        self._swap(0, len(self.data) - 1)
        pop_value = self.data.pop()
        self._down_heap(0)
        return pop_value

    def remove(self, value):
        if not self.data:
            return None
        # O(n) for list.index()
        index = self.data.index(value)
        self._swap(index, len(self.data) - 1)
        pop_value = self.data.pop()
        self._down_heap(index)
        return pop_value

    def print_min(self):
        print(self.data[0])

    def print_heap(self):
        print(self.data)


def down_heap(a, parent, end):
    # a is the whole list. Parent is the index of node that will be down heap.
    # End is the end node of heap.
    leftChild = parent * 2 + 1
    if leftChild <= end:
        biggerChild = leftChild
        rightChild = leftChild + 1
        if rightChild <= end and a[rightChild] > a[leftChild]:
            biggerChild = rightChild

        if a[parent] < a[biggerChild]:
            a[parent], a[biggerChild] = a[biggerChild], a[parent]
            down_heap(a, biggerChild, end)


def heapify(a):
    # max heap
    n = len(a) - 1
    start = (n - 1)//2
    # Start from the parent of last leaf
    # Because all the elements after the final node's parent don't have children. 
    # If a node in the heap doesn't have children, it is not necessary to get it down the heap.
    for i in range(start, -1, -1):
        down_heap(a, i, n)


def heap_sort(a):
    heapify(a)
    i = len(a) - 1
    while i > 0:
        a[0], a[i] = a[i], a[0]
        i -= 1
        down_heap(a, 0, i)


if __name__ == '__main__':
    from random import sample
    rand_list = sample(range(1, 100), 20)
    heap = Heap()
    for number in rand_list:
        heap.push(number)
    heap.print_heap()
    heapify(rand_list)
    print(rand_list)
    heap_sort(rand_list)
    print(rand_list)
