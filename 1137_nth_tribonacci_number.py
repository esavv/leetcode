# See: https://leetcode.com/problems/n-th-tribonacci-number/
class Solution(object):
    def tribonacci(self, n):
        return self.soln2(n)
        # return self.soln1(n)

    # better space efficiency
    def soln2(self, n):
        if n == 0:
            return 0
        if n in (1, 2):
            return 1
        p3, p2, p1 = 0, 1, 1
        for _ in range(3, n+1):
            p3, p2, p1 = p2, p1, p3 + p2 + p1
        return p1

    # iterative approach
    def soln1(self, n):
        seq = [0, 1, 1]
        for i in range(3, n+1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])
        return seq[n]
        