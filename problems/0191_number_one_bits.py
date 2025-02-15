# See: https://leetcode.com/problems/number-of-1-bits/
class Solution(object):
    def hammingWeight(self, n):
        return self.soln2(n)
        # return self.soln1(n)

    # binary ops
    def soln2(self, n):
        numSetBits = 0
        while n > 0:
            numSetBits += n & 1
            n >>= 1
        return numSetBits

    # integer ops
    def soln1(self, n):
        numSetBits = 0
        while n > 0:
            numSetBits += n % 2
            n = n // 2
        return numSetBits