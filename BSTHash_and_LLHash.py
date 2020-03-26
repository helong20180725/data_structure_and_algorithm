# Put a linked list or a binary search tree in the bucket of the hash table.

from random import randint


class HashSet:

    def __init__(self):
        # self.prime can be changed to any primes
        self.prime = 53
        # Bucket: BSTBucket() or LLBucket()
        self.buckets_array = [LLBucket() for _ in range(self.prime)]

    def _hash(self, key):
        # A simple hash function
        return key % self.prime

    def add(self, key):
        hash_value = self._hash(key)
        self.buckets_array[hash_value].insert(key)

    def remove(self, key):
        hash_value = self._hash(key)
        self.buckets_array[hash_value].delete(key)

    def contains(self, key):
        hash_value = self._hash(key)
        return self.buckets_array[hash_value].exists(key)


class TreeNode:

    def __init__(self, value, left= None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BSTree:

    def __init__(self):
        self.root = None

    def insert(self, node, key):
        if not node:
            return TreeNode(key)

        if key < node.value:
            node.left = self.insert(node.left, key)
        elif key == node.value:
            return node
        else:
            node.right = self.insert(node.right, key)

        return node

    def search(self, node, key):
        if not node or key == node.value:
            return node
        if key < node.value:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def remove(self, node, key):
        if not node:
            return None

        if key > node.value:
            node.right = self.remove(node.right, key)
        elif key < node.value:
            node.left = self.remove(node.left, key)
        else:
            if not node.left and not node.right:
                node = None

            elif node.right:
                node.value = self.successor(node)
                node.right = self.remove(node.right, node.value)
            else:
                node.value = self.predecessor(node)
                node.left = self.remove(node.left, node.value)

        return node

    def successor(self, node):
        node = node.right

        while node.left:
            node = node.left
        return node.value

    def predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.value


class BSTBucket:

    def __init__(self):

        self.dummy = BSTree()

    def insert(self, key):
        
        self.dummy.root = self.dummy.insert(self.dummy.root, key)
    
    def delete(self, key):
        self.dummy.root = self.dummy.remove(self.dummy.root, key)
    
    def exists(self, key):
        return (self.dummy.search(self.dummy.root, key) is not None)

    
class LLNode:
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LLBucket:
    
    def __init__(self):
        # Nothing is in head
        self.head = LLNode(0)
    
    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = LLNode(newValue, self.head.next)
            self.head.next = newNode
    
    def delete(self, value):
        prev = self.head
        curr = self.head.next
        
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
    
    def exists(self, value):
        curr = self.head.next
        
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False
        
if __name__ == "__main__":
    hs = HashSet()
    for _ in range(100):
        hs.add(randint(0, 100))
    for _ in range(30):
        test = randint(0, 100)
        if hs.contains(test):
            print(test)
        