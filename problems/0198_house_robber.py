# See: https://leetcode.com/problems/house-robber/
class Solution(object):
    def rob(self, nums):
        return self.soln4(nums)
        # return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # soln #3 from 2/26/2025
    # tabulation with space optimization
    def soln4(self, nums):
        n = len(nums)
        prevRob, prevNotRob = nums[0], 0

        for i in range(1,n):
            currRob = prevNotRob + nums[i]
            currNotRob = max(prevRob, prevNotRob)
            prevRob, prevNotRob = currRob, currNotRob

        return max(prevRob, prevNotRob)

    # soln #2 from 2/26/2025
    # tabulation
    def soln3(self, nums):
        n = len(nums)
        rob, not_rob = [0] * n, [0] * n
        rob[0] = nums[0]

        for i in range(1,n):
            rob[i] = not_rob[i-1] + nums[i]
            not_rob[i] = max(rob[i-1], not_rob[i-1])

        return max(rob[n-1], not_rob[n-1])
    
    # soln #1 from 2/26/2025
    # recursion with memoization
    def soln2(self, nums):
        n = len(nums)
        rob, not_rob = [-1] * n, [-1] * n

        def dp(i):
            # terminating condition: i = 0
            if i == 0:
                rob[i] = nums[i]
                not_rob[i] = 0
                return rob[i], not_rob[i]

            # memoization check
            if rob[i] != -1 and not_rob[i] != -1:
                return rob[i], not_rob[i]

            # core logic
            prevRob, prevNotRob = dp(i-1)
            rob[i] = prevNotRob + nums[i]
            not_rob[i] = max(prevRob, prevNotRob)
            return rob[i], not_rob[i]

        dp(n-1)
        return max(rob[n-1], not_rob[n-1])

    # soln #1
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