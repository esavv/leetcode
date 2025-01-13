# See: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution(object):
    def strStr(self, haystack, needle):
        return self.soln1(haystack, needle)

    # two-pointer approach
    def soln1(self, haystack, needle):
        if len(needle) > len(haystack):
            return -1

        left = 0
        while left < len(haystack):
            if haystack[left] == needle[0]:
                right = 1
                while right < len(needle) and left + right < len(haystack) and needle[right] == haystack[left + right]:
                    right += 1
                if right == len(needle):
                    return left
                if left + right == len(haystack):
                    return -1
            left += 1
        return -1
    