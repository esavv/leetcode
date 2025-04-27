# See: https://leetcode.com/problems/gray-code/
class Solution(object):
    def grayCode(self, n):
        return self.soln1(n)

    # soln #1 on 4/27/2025
    # iterative list build
    def soln1(self, n):
        seq = [0]

        for i in range(n):
            j = len(seq)-1
            while j >= 0:
                seq.append(seq[j]+2**i)
                j -= 1

        return seq
