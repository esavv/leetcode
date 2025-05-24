# See: https://leetcode.com/problems/maximum-product-subarray/
class Solution(object):
    def maxProduct(self, nums):
        return self.soln2(nums)

    # DP attempt, doesn't work
    def soln2(self, nums):
        n = len(nums)
        include = [0] * n
        exclude = [0] * n
        dp = [0] * n

        include[0] = nums[0]
        exclude[0] = -999999
        dp[0] = nums[0]

        for i in range(1, n):
            if abs(nums[i]) > abs(nums[i] * include[i-1]):
                include[i] = nums[i]
            else:
                include[i] = nums[i] * include[i-1]
            exclude[i] = dp[i-1]
            dp[i] = max(include[i], exclude[i])
        return dp[-1]