# See: https://leetcode.com/problems/powx-n/
class Solution(object):
    def myPow(self, x, n):
        return self.soln3(x, n)
        # return self.soln1(x, n)

    # soln #3 on 6/08/2025
    # recursion with memoization, O(logn) time
    def soln3(self, x, n):
        memo = {0: 1, 1: x}
        def power(a, b):
            if b in memo:
                return memo[b]
            res = power(a, b//2) * power(a, b - b//2)
            memo[b] = res
            return res

        if n < 0:
            return 1 / power(x, -1 * n)
        return power(x, n)

    # soln #1 on 6/08/2025
    # brute force iteration
    def soln1(self, x, n):
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        if x == -1:
            return 1 if n % 2 == 0 else -1

        power = 1
        absN = abs(n)
        while absN > 0:
            if power == 0.0:
                return power
            if n > 0:
                power *= x
            else:
                power /= x
            absN -= 1
        return power