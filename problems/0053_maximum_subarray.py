# See: https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        return self.soln1(nums)

    # soln #1 on 4/28/2025
    # sliding window
    def soln1(self, nums):
        left = right = 0
        currSum = maxSum = nums[0]

        while right < len(nums)-1:
            if currSum >= 0:
                right += 1
                currSum += nums[right]
            if currSum < 0 and right < len(nums)-1:
                left, right = right+1, right+1
                currSum = nums[left]
            maxSum = max(maxSum, currSum)

        return maxSum