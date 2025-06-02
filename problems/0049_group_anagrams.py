# See: https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        return self.soln1(strs)
        
    # soln #1 on 6/02/2025
    # trie approach with recursive DFS
    def soln1(self, strs):
        trie = ([], {})
        for s in strs:
            # count how many chars in str
            counts = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                counts[idx] += 1

            # identify our nodes in the Trie
            charList = []
            for idx, count in enumerate(counts):
                if count > 0:
                    char = chr(idx + ord('a'))
                    charList.append(char + str(count))

            # navigate to the leaf of the Trie
            strList, root = trie
            for node in charList:
                if node not in root:
                    root[node] = ([], {})
                strList, root = root[node]

            # append the string to the leaf's string list
            strList.append(s)

        groups = []
        def dfs(trie):
            strList, root = trie
            if strList:
                groups.append(list(strList))
            for node in root:
                dfs(root[node])
            return

        dfs(trie)
        return groups