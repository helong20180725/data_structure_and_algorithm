class TrieNode:

    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}              # {},  or list, index from 1 to 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        i = 0
        while i < len(word) and word[i] in cur.children:
            cur = cur.children[word[i]]
            i += 1

        while i < len(word):
            cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
            i += 1

        cur.isWord = True
        cur.word = word

    def search(self, word):
        cur = self.root
        i = 0

        while i < len(word) and word[i] in cur.children:
            cur = cur.children[word[i]]
            i += 1

        if i < len(word):
            return False
        else:
            return cur.isWord

    def startsWith(self, prefix):
        cur = self.root
        i = 0
        while i < len(prefix) and prefix[i] in cur.children:
            cur = cur.children[prefix[i]]
            i += 1

        if i < len(prefix):
            return False
        else:
            return True

    def print_trie(self, node, level):
        """
        It's not good. But I will think of a better way to print it. 
        """
        cur = node
        if not node.children:

            return None
        for key in node.children:
            print("----"*level+key)
            self.print_trie(node.children[key], level+1)

if __name__ == "__main__":
    words_dict = Trie()
    words_dict.insert("trie")
    words_dict.insert("dorooo")
    words_dict.insert("ttttdorooo")
    words_dict.insert("ttorooo")
    words_dict.print_trie(words_dict.root, 1)
