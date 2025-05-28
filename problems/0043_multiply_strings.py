# See: https://leetcode.com/problems/multiply-strings/
class Solution(object):
    def multiply(self, num1, num2):
        return self.soln1(num1, num2)

    # soln #1 on 5/28/2025
    # char-wise ordinal distance
    def soln1(self, num1, num2):
        n, m = len(num1), len(num2)
        int1 = int2 = 0

        multiple = 1
        for i in range(n-1, -1, -1):
            distance = ord(num1[i]) - ord('0')
            int1 += distance * multiple
            multiple *= 10

        multiple = 1
        for i in range(m-1, -1, -1):
            distance = ord(num2[i]) - ord('0')
            int2 += distance * multiple
            multiple *= 10

        product = str(int1 * int2)
        return product