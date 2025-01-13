# See: https://leetcode.com/problems/find-peak-element/
class Solution(object):
    def findPeakElement(self, nums):
        return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # binary search, recursive
    def soln3(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        def binary(left, right):
            mid = (left + right) // 2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid+1] > nums[mid]:
                return binary(mid+1, right)
            return binary(left, mid-1)

        return binary(1, n-2)

    # binary search, iterative
    def soln2(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        left, right = 1, n-2
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            if nums[mid+1] > nums[mid]:
                left = mid+1
            else:
                right = mid-1

    # linear brute approach
    def soln1(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        for x in range(1,n-1):
            if nums[x] > nums[x-1] and nums[x] > nums[x+1]:
                return x        