# See: https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False
        
        set1, set2 = set(word1), set(word2)
        if set1 != set2:
            return False
        
        dict1, dict2 = {},  {}
        for c in word1:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for c in word2:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1

        fdict1, fdict2 = {}, {}
        for c in dict1:
            if dict1[c] in fdict1:
                fdict1[dict1[c]] += 1
            else:
                fdict1[dict1[c]] = 1
        for c in dict2:
            if dict2[c] in fdict2:
                fdict2[dict2[c]] += 1
            else:
                fdict2[dict2[c]] = 1

        if fdict1 != fdict2:
            return False
        return True
        