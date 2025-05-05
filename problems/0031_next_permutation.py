# See: https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        return self.soln1(nums)
        
    # soln #1 on 5/05/2025
    # sliding window to increase order, then minimize rest of array
    def soln1(self, nums):
        n = len(nums)
        left, right = n-2, n

        # find the swap while the window can grow and we haven't found it (right still == n)
        while left >= 0 and right == n:
            for i in range(n-1, left, -1):
                # if we found a swap, update right & perform the swap
                if nums[i] > nums[left]:
                    right = i
                    nums[left], nums[right] = nums[right], nums[left]
                    break
            # if we swapped, break
            if right < n:
                break
            left -= 1

        # minimize the remaining array
        # if we found a swap, the remainder is (left+1, n-1)
        # if we didn't find a swap, left is -1 and the remainder is the whole array, also (left+1, n-1)
        left, right = left+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return