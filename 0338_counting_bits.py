# See: https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        ans, mod = [0], 1
        for i in range(1, n+1):
            if i == mod * 2:
                mod *= 2
            ans.append(1 + ans[i - mod])
        return ans
        