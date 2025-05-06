# See: https://leetcode.com/problems/jump-game/
class Solution(object):
    def canJump(self, nums):
        return self.soln4(nums)
        # return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)
        
    # soln #4 on 5/06/2025
    # editorial-inspired optimization over dp tabulation
    def soln4(self, nums):
        n = len(nums)
        nearestGood = n-1

        for i in range(n-2, -1, -1):
            maxJump = min(i + nums[i], n-1)
            if nearestGood <= maxJump:
                nearestGood = i
        
        return nearestGood == 0

    # soln #3 on 5/06/2025
    # dp tabulation with jump optimizations
    def soln3(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            for j in range(min(nums[i], n-1-i), 0, -1):
                if dp[i+j]:
                    dp[i] = True
                    break
        
        return dp[0]

    # soln #2 on 5/06/2025
    # dp tabulation
    def soln2(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[n-1] = True

        for i in range(n-2, -1, -1):
            dp[i] = False
            for j in range(1, min(nums[i]+1, n-i)):
                dp[i] = dp[i+j] or dp[i]
        
        return dp[0]

    # soln #1 on 5/06/2025
    # recursion with memoization
    def soln1(self, nums):
        n = len(nums)
        memo = [0] * n

        def dp(i):
            if memo[i] != 0:
                return memo[i]

            if i == n-1:
                memo[i] = True
            else:
                memo[i] = False
                for j in range(1, min(nums[i]+1, n-i)):
                    memo[i] = dp(i+j) or memo[i]
            return memo[i]

        return dp(0)