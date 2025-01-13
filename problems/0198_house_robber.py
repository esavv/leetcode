# See: https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        return self.soln1(nums)

    # recursion with memoization
    def soln1(self, nums):
        maxRob = [-1] * len(nums)

        def dp(idx):
            if idx >= len(nums):
                return 0
            if maxRob[idx] > -1:
                return maxRob[idx]
            if idx == len(nums)-1:
                maxRob[idx] = nums[idx]
                return maxRob[idx]
            maxRob[idx] = max(nums[idx] + dp(idx + 2), dp(idx + 1))
            return maxRob[idx]

        return dp(0)        