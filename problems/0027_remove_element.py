# See: https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, nums, val):
        return self.soln1(nums, val)

    # linear overwrite first k elements
    def soln1(self, nums, val):
        if not nums:
            return 0

        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k       