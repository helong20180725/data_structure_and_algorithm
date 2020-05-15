class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree(arr, i):
    # Build a binary tree from a list of node values.
    if i < len(arr) and arr[i] is not None:
        node = TreeNode(arr[i])
        node.left = build_tree(arr, 2*i + 1)
        node.right = build_tree(arr, 2*i + 2)
        return node
    return None


class Printer:

    def print_tree(self, root):
        depth = self.get_depth(root)
        width = (1 << depth) - 1
        # The length of " " is decided by the maximum digits number
        # The index of node in the 2d list is for the position of tree node
        tree_list = [[" " for _ in range(width)] for _ in range(depth)]
        self._fill(root, 0, 0, width-1, tree_list)
        
        for level in range(depth):
            print("".join(tree_list[level]))

    def _fill(self, node, level, left, right, tree_list):
        if node:
            mid = (left + right) // 2
            tree_list[level][mid] = str(node.val)
            self._fill(node.left, level+1, left, mid - 1, tree_list)
            self._fill(node.right, level+1, mid + 1, right, tree_list)

    def _get_depth(self, node):
        if not node:
            return 0
        left = self._get_depth(node.left)
        right = self._get_depth(node.right)
        return max(left, right) + 1


if __name__ == "__main__":

    node_list = [1, 2, 3, 4, None, 6, 8, 9, 1, None, None, 4, 2, 2, 3, None, None, 1, 2]
    root = build_tree(node_list, 0)
    printer = Printer()
    printer.print_tree(root)

