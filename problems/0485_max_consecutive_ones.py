# See: https://leetcode.com/problems/max-consecutive-ones/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # soln #2 from 2/25/2025
    # sliding window
    def soln2(self, nums):
        maxNum, left = 0, 0
        while left < len(nums):
            while left < len(nums) and nums[left] == 0:
                left += 1
            right = left
            while right < len(nums) and nums[right] == 1:
                right += 1
            maxNum = max(maxNum, right - left)
            left = right + 1
        return maxNum

    # soln #1 from 2/25/2025
    # array iteration
    def soln1(self, nums):
        maxNum, curr = 0, 0
        for val in nums:
            if val == 1:
                curr += 1
                maxNum = max(maxNum, curr)
            else:
                curr = 0
        return maxNum
