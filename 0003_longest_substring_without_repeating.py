# See: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        return self.soln1(s)

    # sliding window with hashtable
    def soln1(self, s):
        if len(s) <= 1:
            return len(s)

        left, res = 0, 1
        hash = {}
        for right in range(len(s)):
            newChar = s[right]
            while newChar in hash:
                hash.pop(s[left])
                left += 1
            hash[newChar] = right
            curLen = right - left + 1
            res = max(res, curLen)
		
        return res
        