# See: https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

def atoi(char):
    return ord(char) - ord('a')

class Trie():
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word):
        curr = self.head
        for char in word:
            idx = atoi(char)
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isWord = True				# check if this breaks on “” inserts

    def search(self, word):
        curr = self.head
        for char in word:
            idx = atoi(char)
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        if not curr.isWord:
            return False
        return True

    def startsWith(self, prefix):
        curr = self.head
        for char in prefix:
            idx = atoi(char)
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True