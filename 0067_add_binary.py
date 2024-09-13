# See: https://leetcode.com/problems/add-binary/
class Solution(object):
    def addBinary(self, a, b):
        return self.soln1(a, b)

    # digit-wise addition with a carry
    def soln1(self, a, b):
        if a == '0':
            return b
        if b == '0':
            return a

        res = ''
        n = max(len(a), len(b))
        carry, char_a, char_b = 0, 0, 0
        for i in range(n):
            if i < len(a):
                char_a = int(a[len(a)-i-1])
            else:
                char_a = 0
            if i < len(b):
                char_b = int(b[len(b)-i-1])
            else:
                char_b = 0

            s = char_a + char_b + carry

            if s % 2 == 0:
                res = '0' + res
            else:
                res = '1' + res

            if s > 1:
                carry = 1
            else:
                carry = 0

        if carry == 1:
            res = '1' + res
        return res
        