# See: https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        return self.soln2(digits)
        # return self.soln1(digits)

    # in-place
    def soln2(self, digits):
        remainder = True
        idx = len(digits) - 1
        
        while remainder and idx >= 0:
            sum = 1 + digits[idx]
            if sum == 10:
                digits[idx] = 0
            else:
                digits[idx] = sum
                remainder = False
            idx -= 1
        if remainder:
            digits = [1] + digits
        return digits

    # out-of-place
    def soln1(self, digits):
        res = digits
        remainder = True
        idx = len(digits) - 1
        
        while remainder and idx >= 0:
            sum = 1 + digits[idx]
            if sum == 10:
                res[idx] = 0
            else:
                res[idx] = sum
                remainder = False
            idx -= 1
        if remainder:
            res = [1] + res
        return res
        