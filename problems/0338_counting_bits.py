# See: https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        return self.soln3(n)
        # return self.soln2(n)
        # return self.soln1(n)
        
    # soln #2 from 2/15/2025
    def soln3(self, n):
        ans = [0] * (n+1)
        distance = 1
        for x in range(1, n+1):
            if x == 2 * distance:
                distance *= 2
            ans[x] = ans[x - distance] + 1
        return ans

    # soln #1 from 2/15/2025
    def soln2(self, n):
        ans = [0] * (n+1)

        def countSetBits(n):
            numSetBits = 0
            while n > 0:
                numSetBits += n & 1
                n >>= 1
            return numSetBits

        for i in range(n+1):
            ans[i] = countSetBits(i)

        return ans

    # solution from sometime in early 2024
    def soln1(self, n):
        ans, mod = [0], 1
        for i in range(1, n+1):
            if i == mod * 2:
                mod *= 2
            ans.append(1 + ans[i - mod])
        return ans
        