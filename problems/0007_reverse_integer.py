# See: https://leetcode.com/problems/reverse-integer/
class Solution(object):
    def reverse(self, x):
        return self.soln2(x)
        # return self.soln1(x)
        
    # soln #2 on 5/16/2025
    # two pointers
    def soln2(self, x):
        xStr = [char for char in str(x)]
        n = len(xStr)
        left = 0 if x >= 0 else 1
        right = n-1
        while left < right:
            xStr[left], xStr[right] = xStr[right], xStr[left]
            left += 1
            right -= 1
        xStr = ''.join(xStr)

        small = '-2147483648'
        big = '2147483647'
        
        if x < 0 and n == len(small) and xStr > small:
            return 0
        if x >= 0 and n == len(big) and xStr > big:
            return 0
        return int(xStr)

    # soln #1 on 5/16/2025
    # reverse
    def soln1(self, x):
        xStr = str(x)
        n = len(xStr)
        xStrReverse, end = '', -1
        if x < 0:
            xStrReverse, end = '-', 0
        for i in range(n-1, end, -1):
            xStrReverse += xStr[i]

        small = '-2147483648'
        big = '2147483647'
        
        if x < 0 and n == len(small) and xStrReverse > small:
            return 0
        if x >= 0 and n == len(big) and xStrReverse > big:
            return 0
        return int(xStrReverse)
