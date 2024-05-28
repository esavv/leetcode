# See: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution(object):
    def longestSubarray(self, nums):
        return self.soln1(nums)

    # linear scan maintaining two run lengths up to current element
    def soln1(self, nums):
        ans, first, second = 0, 0, 0
        all_ones = True
        prev = None
        
        for i in range(len(nums)):
            if nums[i] == 1:
                first += 1
                second += 1
                ans = max(ans, first, second)
            else:
                all_ones = False
                if prev == 1:
                    second, first = first, 0
                else:
                    second = 0
            prev = nums[i]

        if all_ones:
            return ans-1
        return ans        