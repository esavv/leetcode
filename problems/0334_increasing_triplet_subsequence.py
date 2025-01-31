# See: https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution(object):
    def increasingTriplet(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # greedy
    def soln2(self, nums):
        small, medium = float("inf"), float("inf")
        for val in nums:
            if val <= small:
                small = val
            elif val <= medium:
                medium = val
            else:
                return True
        return False

    # brute force, time limit exceeded
    def soln1(self, nums):
        n = len(nums)
        if n < 3:
            return False
            
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False
