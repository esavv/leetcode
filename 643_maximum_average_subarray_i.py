# See: 
class Solution(object):
    def findMaxAverage(self, nums, k):
        maxn = sum(nums[:k])
        curr = maxn
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            maxn = max(maxn, curr)
        return maxn / float(k)
        