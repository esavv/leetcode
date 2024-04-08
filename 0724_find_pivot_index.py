# See: https://leetcode.com/problems/find-pivot-index/
class Solution(object):
    def pivotIndex(self, nums):
        right_sum, left_sum = [0] * len(nums), [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            right_sum[i] = nums[i+1] + right_sum[i+1]

        if right_sum[0] == 0:
            return 0

        for i in range(1, len(nums)):
            left_sum[i] = nums[i-1] + left_sum[i-1]
            if right_sum[i] == left_sum[i]:
                return i
        return -1
        