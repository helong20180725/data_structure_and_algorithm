"""
Segment Tree structure:
This structure is used to get the max value or summation of a segment in a list
"""
class SegmentTreeNode:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.summation = 0
        self.maximum = 0
        self.left = None
        self.right = None


class SegmentTree:

    def __init__(self, array):
        self.size = len(array)
        self.root = self._build_tree(0, self.size-1, array)

    def _build_tree(self, start, end, array):
        if start > end:
            return None

        root = SegmentTreeNode(start, end)

        if start == end:
            root.summation = array[start]
            root.maximum = array[start]
            return root

        middle = (start + end)//2

        root.left = self._build_tree(start, middle, array)
        root.right = self._build_tree(middle+1, end, array)

        root.summation = root.left.summation + root.right.summation
        root.maximum = max(root.left.maximum, root.right.maximum)

        return root

    def query_sum(self, start, end):
        if start > end:
            return None
        return self._query_sum(self.root, start, end)

    def _query_sum(self, node, start, end):

        if node.start == start and node.end == end:
            return node.summation

        middle = (node.start + node.end) // 2
        left_sum, right_sum = 0, 0

        if start <= middle:
            left_sum = self._query_sum(node.left, start, min(middle, end))
        if end >= middle + 1:
            right_sum = self._query_sum(node.right, max(middle+1, start), end)

        return left_sum + right_sum

    def query_max(self, start, end):
        if start > end:
            return None
        return self._query_max(self.root, start, end)

    def _query_max(self, node, start, end):
        if node.start == start and node.end == end:
            return node.maximum

        middle = (node.start + node.end) // 2
        left_max = float("-inf")
        right_max = float("-inf")

        if start <= middle:
            left_max = self._query_max(node.left, start, min(end, middle))
        if end >= middle + 1:
            right_max = self._query_max(node.right, max(middle+1, start), end)

        return max(left_max, right_max)

    def modify(self, index, value):
        if index < 0 or index >= self.size:
            return None
        self._modify(self.root, index, value)

    def _modify(self, node, index, value):
        if node.start == node.end and node.start == index:
            node.summation = value
            node.maximum = value
            return
        middle = (node.start + node.end) // 2
        if index <= middle:
            self._modify(node.left, index, value)
        else:
            self._modify(node.right, index, value)

        node.maximum = max(node.left.maximum, node.right.maximum)
        node.summation = node.left.summation + node.right.summation


if __name__ == "__main__":
    #           0, 1, 2, 3, 4, 5, 6, 7, 8,  9
    tempList = [1, 4, 2, 5, 6, 9, 3, 0, 10, 12]
    sTree = SegmentTree(tempList)
    print(sTree.query_max(3, 6))
    print(sTree.query_sum(3, 6))
    sTree.modify(5, 20)
    print(sTree.query_max(3, 6))
    print(sTree.query_sum(3, 6))