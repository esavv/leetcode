# See: https://leetcode.com/problems/longest-palindromic-substring/
class Solution(object):
    def longestPalindrome(self, s):
        return self.soln1(s)
    
    # soln 1 on 4/14/2025
    # recursive approach, doesn't work
    def soln1(self, s):
        longest = ['']
        explored = set()

        def recurse(left, right, matches):
            if right <= left:
                if right - left + matches + matches + 1 > len(longest[0]):
                    longest[0] = s[left-matches:right+matches+1]
                return

            if right - left + matches + matches + 1 <= len(longest[0]):
                return

            if s[left:right+1] not in explored:
                explored.add(s[left:right+1])
            elif matches == 0:
                return

            if s[left] == s[right]:
                recurse(left+1, right-1, matches+1)
            recurse(left, right-1, 0)
            recurse(left+1, right, 0)
            return

        recurse(0, len(s)-1, 0)
        return longest[0]