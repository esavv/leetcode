# See: https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution(object):
    def maxOperations(self, nums, k):
        return self.soln3(nums, k)
        # return self.soln2(nums, k)
        # return self.soln1(nums, k)
    
    # sorting + two pointers, slower with improved space
    def soln3(self, nums, k):
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        res = 0
        if n >= 2 and (k < nums[left] + nums[left+1] or k > nums[right] + nums[right-1]):
            return 0
        while left < right:
            if k == nums[left] + nums[right]:
                res += 1
                left += 1
                right -= 1
            elif k > nums[left] + nums[right]:
                left += 1
            else:
                right -= 1
        return res

    # hash table approach, iterate through hash table (better avg time)
    def soln2(self, nums, k):
        res = 0
        counts = {}
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        for key in counts:
            complement = k - key
            if key == complement:
                res += counts[key] // 2
                counts[key] = 0
            elif complement in counts:
                res += min(counts[key], counts[complement])
                counts[key], counts[complement] = 0, 0
        return res

    # hash table approach, iterate through nums
    def soln1(self, nums, k):
        res = 0
        counts = {}
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1
        for val in nums:
            complement = k - val
            if val == complement and counts[val] > 1:
                res += 1
                counts[val] -= 2
            elif val != complement and counts[val] > 0 and complement in counts and counts[complement] > 0:
                res += 1
                counts[val] -= 1
                counts[complement] -= 1
        return res