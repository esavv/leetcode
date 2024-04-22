# See: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution(object):
    def maxVowels(self, s, k):
        return self.soln1(s, k)

    # sliding window
    def soln1(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        numVowels = 0
        for i in range(k):
            if s[i] in vowels:
                numVowels += 1
        ans = numVowels
        
        right = k
        while right < len(s):
            if s[right-k] in vowels:
                numVowels -= 1
            if s[right] in vowels:
                numVowels += 1
            ans = max(ans, numVowels)
            right += 1
        return ans	