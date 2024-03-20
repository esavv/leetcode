# See: 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ret = ''
        minlen = min(len(word1),len(word2))
        for i in range(minlen):
            ret += word1[i] + word2[i]
        ret += (word1[minlen:] or word2[minlen:])
        return ret