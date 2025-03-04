# See: https://leetcode.com/problems/max-consecutive-ones-ii/
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # soln #2 on 3/4/2025
    # soln1 with cleanup
    def soln2(self, nums):
        left, right, maxOnes, flips = 0, 0, 0, 0

        while right < len(nums):
            while left < len(nums) and nums[right] == 0 and flips == 1:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            while right < len(nums) and (nums[right] == 1 or flips == 0):
                if nums[right] == 0:
                    flips += 1
                right += 1
            maxOnes = max(maxOnes, right - left)
        return maxOnes

    # soln #1 on 3/4/2025
    # sliding window
    def soln1(self, nums):
        if len(nums) == 0:
            return 0

        left, right, = 0, 1
        maxOnes, flips = 1, 0
        if nums[0] == 0:
            flips = 1

        while right < len(nums):
            while left < len(nums) and nums[right] == 0 and flips >= 1:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            while right < len(nums) and (nums[right] == 1 or flips < 1):
                if nums[right] == 0:
                    flips += 1
                right += 1
            maxOnes = max(maxOnes, right - left)
        return maxOnes