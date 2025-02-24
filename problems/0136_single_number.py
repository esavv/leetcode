# See: https://leetcode.com/problems/single-number/
class Solution(object):
    def singleNumber(self, nums):
        return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # cumulative XOR, constant space
    def soln3(self, nums):
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor

    # fixed-length map array
    def soln2(self, nums):
        minNum, maxNum, offset = -30000, 30000, 30000
        numPossibleVals = maxNum - minNum + 1
        seen = [0] * numPossibleVals

        for val in nums:
            seen[val + offset] += 1

        for val in nums:
            if seen[val + offset] == 1:
                return val

    # set, linear space
    def soln1(self, nums):
        seen = set([])
        for val in nums:
            if val in seen:
                seen.remove(val)
            else:
                seen.add(val)
        return seen.pop()
