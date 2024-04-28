# See: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
class Solution(object):
    def minFlips(self, a, b, c):
        return self.soln1(a, b, c)

    # O(logn) approach, where n = max(a, b, c)
    def soln1(self, a, b, c):
        flips = 0
        while a + b + c > 0:
            aBit, bBit, cBit = a & 1, b & 1, c & 1

            if aBit | bBit != cBit:
                if aBit | bBit == 0:
                    flips += 1
                else:
                    flips += aBit + bBit

            a, b, c = a >> 1, b >> 1, c >> 1
        return flips
