class BinaryIndexTree:
    """
    BinaryIndexTree is just an array which there are relations among the indexes.
    It makes the array like a special tree structure.
    """
    def __init__(self, array):
        self.size = len(array)
        self.sum_array = [0 for _ in range(self.size + 1)]

        # Add array to the tree.
        for i in range(self.size):
            self.add(i, array[i])

    def low_bit(self, x):
        """
        Get the number of elements which sum_array contains in the array.
        """
        return x & (-x)

    def add(self, index, value):
        """

        :param index: index in array
        :param value: new delta value
        """
        index += 1
        while index <= self.size:
            self.sum_array[index] += value
            index += self.low_bit(index)

    def prefix_sum(self, index):
        """

        :param index: index in array
        :return: the summation of array [0: index+1]
        """
        index += 1
        ret = 0
        while index > 0:
            ret += self.sum_array[index]
            index -= self.low_bit(index)

        return ret

if __name__ == "__main__":
    testList = [2, 3, 4, 5, 9, 10]
    bTree = BinaryIndexTree(testList)
    print(bTree.prefix_sum(3))
    bTree.add(3, 11 - 5)
    print(bTree.prefix_sum(3))
