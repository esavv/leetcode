# See: https://leetcode.com/problems/sqrtx/
class Solution(object):
    def mySqrt(self, x):
        return self.soln2(x)
        # return self.soln1(x)

    # binary search
    def soln2(self, x):
        left, right = 0, x+1
        while left+1 < right:
            mid = (left + right) // 2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod > x:
                right = mid
            else:
                left = mid
        return left

    # O(sqrt(n)) search
    def soln1(self, x):
        for i in range(x+1):
            prod = i * i
            if prod == x:
                return i
            elif prod > x:
                return i-1
        return 0
        