# See: https://leetcode.com/problems/search-suggestions-system/
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        return self.soln3(products, searchWord)
        # return self.soln2(products, searchWord)
        # return self.soln1(products, searchWord)

    # sorting approach
    def soln3(self, products, searchWord):
        products.sort()
        prefix = ''
        res = []
        for i in range(len(searchWord)):
            prefix += searchWord[i]
            j = 0
            suggs = []
            for _ in range(len(products)):
                if products[j] < prefix:
                    products.remove(products[j])
                elif prefix == products[j][0:i+1]:
                    suggs.append(products[j])
                    if len(suggs) == 3:
                        break                
                    j += 1
                else:
                    break
            res.append(suggs)
        return res

    # better trie search, but still not great
    def soln2(self, products, searchWord):
        trie, res = Trie(), []
        for product in products:
            trie.insert(product)

        prefix = searchWord[0]
        res.append(trie.search(prefix, '', 3))
        for i in range(1, len(searchWord)):
            prefix += searchWord[i]
            lastResult = res[-1]
            searchAgain = len(lastResult) == 3 and prefix != lastResult[0][0:i+1]
            newResult = []
            for result in lastResult:
                if prefix == result[0:i+1]:
                    newResult.append(result)
            if searchAgain:
                lastWordSuffix = ''
                if newResult:
                    lastWord = newResult[-1]
                    if lastWord == prefix:
                        newResult.remove(lastWord)
                    lastWordSuffix = lastWord[i+1:]
                newResult = newResult + trie.search(prefix, lastWordSuffix, 3 - len(newResult))
            res.append(newResult)

        return res

    # naive trie search
    def soln1(self, products, searchWord):
        trie, res, prefix = Trie(), [], ''
        for product in products:
            trie.insert(product)

        for i in range(len(searchWord)):
            prefix += searchWord[i]
            res.append(trie.search(prefix, '', 3))

        return res
        
class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            i = ord(char) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isEndOfWord = True

    def search(self, prefix, lastWordSuffix, numWords):
        node = self.root
        res = []
        for char in prefix:
            i = ord(char) - ord('a')
            if not node.children[i]:
                return res
            node = node.children[i]
        
        stack, suffix = [node], lastWordSuffix
        for char in lastWordSuffix:
            i = ord(char) - ord('a')
            stack.append(node.children[i])
            node = node.children[i]

        if node.isEndOfWord and not lastWordSuffix:
            res.append(prefix)
            if len(res) == numWords:
                return(res)

        offset = 0
        while stack or node:
            while node:
                children = node.children
                node = None
                for i in range(offset, len(children)):
                    child = children[i]
                    if child:
                        stack.append(child)
                        char = chr(ord('a') + i)
                        suffix += char
                        node = child
                        offset = 0
                        break

                if node and node.isEndOfWord:
                    res.append(prefix + suffix)

                    if len(res) == numWords:
                        return(res)

            stack.pop()
            if stack:
                lastChar = suffix[-1]
                suffix = suffix[:-1]
                node = stack[-1]
                offset = ord(lastChar) - ord('a') + 1

        return res