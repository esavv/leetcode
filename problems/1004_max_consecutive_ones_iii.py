# See: https://leetcode.com/problems/max-consecutive-ones-iii/
class Solution(object):
    def longestOnes(self, nums, k):
        return self.soln4(nums, k)
        # return self.soln3(nums, k)
        # return self.soln2(nums, k)
        # return self.soln1(nums, k)

    # soln #1 from 3/25/2025
    # sliding window
    def soln4(self, nums, k):
        ans = left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]

            while k < 0:
                k += 1 - nums[left]
                left += 1

            ans = max(ans, right - left + 1)
        return ans

    # soln #1 from 2/21/2025
    # sliding window
    def soln3(self, nums, k):
        maxOnes = 0
        errors = 0
        if nums[0] == 0:
            errors = 1
        right = 0

        for left in range(len(nums)):
            if left > 0 and nums[left-1] == 0:
                errors -= 1

            while right < len(nums) and errors <= k:
                right += 1
                if right < len(nums) and nums[right] == 0:
                    errors += 1
            
            maxOnes = max(maxOnes, right - left)
            if right == len(nums):
                return maxOnes
        return maxOnes

    def soln2(self, nums, k):
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                k -= 1
            
            if k >= 0:
                ans = max(ans, right-left+1)

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            right += 1
        return ans

    # 54 / 59 testcases solved, 1 hint used
    def soln1(self, nums, k):
        if k == len(nums):
            return len(nums)

        ans = 0
        left, right, prev = 0, 0, -1

        while right < len(nums):
            tolerance = k
            
            left = prev+1
            while left<len(nums) and (nums[left]==0 or (left-1>=0 and nums[left]==1 and nums[left-1]==1)):
                left += 1
            prev = left

            right = left
            while right < len(nums) and (nums[right] == 1 or tolerance > 0):
                # if we find a zero and have flips remaining, flip the zero
                if nums[right] == 0:
                    tolerance -= 1
                right += 1

            while right == len(nums) and left >= 0 and tolerance > 0:
                left -= 1
                if nums[left] == 0:
                    tolerance -= 1

            # we found a window, so record it
            curr = right - left
            ans = max(ans, curr)
        return ans
