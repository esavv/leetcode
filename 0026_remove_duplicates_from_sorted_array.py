# See: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        return self.soln1(nums)

    # linear solution
    def soln1(self, nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k
 