# See: https://leetcode.com/problems/removing-stars-from-a-string/
class Solution(object):
    def removeStars(self, s):
        ans = []
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
        