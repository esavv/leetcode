# See: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        return self.soln2(nums, target)
        # return self.soln1(nums, target)

    # hash table
    def soln2(self, nums, target):
        n = len(nums)
        diffs = {}
        for idx in range(n):
            diff = target - nums[idx]
            diffs[diff] = idx

        for idx in range(n):
            if nums[idx] in diffs and idx != diffs[nums[idx]]:
                return [idx, diffs[nums[idx]]]

    # brute force
    def soln1(self, nums, target):
        n = len(nums)
        for x in range(0,n-1):
            for y in range(x+1, n):
                if nums[x] + nums[y] == target:
                    return [x, y]
 