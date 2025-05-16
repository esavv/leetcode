# See: https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    def longestConsecutive(self, nums):
        return self.soln1(nums)
        
    # soln #1 on 5/16/2025
    # hash table
    def soln1(self, nums):
        seen = {}
        maxLength = 0

        for num in nums:
            if num in seen:
                continue
            first = last = num
            if num+1 in seen:
                last = seen[num+1][1]
            if num-1 in seen:
                first = seen[num-1][0]
                seen[first] = (first, last)
            if num+1 in seen:
                seen[last] = (first, last)
            seen[num] = (first, last)
            maxLength = max(maxLength, last - first + 1)

        return maxLength