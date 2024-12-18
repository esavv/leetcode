# See: https://leetcode.com/problems/increasing-triplet-subsequence/
class Solution(object):
    def increasingTriplet(self, nums):
        return self.soln4(nums)
        # return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # implementation of the editorial's psuedocode
    def soln4(self, nums):
        first = second = 999999
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

    # "greedy" attempt that doesn't make sense. 62/84 test cases passed
    def soln3(self, nums):
        n = len(nums)
        if n < 3:
            return False

        x, y, z = 0, 1, 2
        while (x < n-3 and y < n-2 and z < n-1) and (nums[x] >= nums[y] or nums[y] >= nums[z]):
            while x < n-3 and nums[x+1] <= nums[x]:
                x += 1
                y += 1
                z += 1

            while z < n-1 and nums[z+1] >= nums[z]:
                z += 1

            while y < n-2 and nums[y] >= nums[z]:
                y += 1

            if x < n-3 and nums[y] < nums[x]:
                x, y = y, y+1
                if z < n-1 and y == z:
                    z += 1
        if nums[x] < nums[y] < nums[z]:
            return True
        return False

    # single for loop w/ two pointers, fails. 72/84 test cases passed
    # fails on: nums = [1,5,0,4,1,3], expected True
    def soln2(self, nums):
        n = len(nums)
        if n < 3:
            return False

        for i in range(n-2):
            j, k = i+1, i+2
            while j < n-2 and nums[j] <= nums[i]:
                j += 1
                k += 1
            while k < n-1 and nums[k] <= nums[j]:
                k += 1
            if nums[i] < nums[j] and nums[j] < nums[k]:
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
