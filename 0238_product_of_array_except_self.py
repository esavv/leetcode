# See: https://leetcode.com/problems/product-of-array-except-self/
class Solution(object):
    def productExceptSelf(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # compute prefixes & suffixes in constant space
    def soln2(self, nums):
        n = len(nums)
        answer = [1] * n

        prefix = nums[0]
        for i in range(1,n):
            answer[i] = answer[i] * prefix
            prefix = prefix * nums[i]

        suffix = nums[n-1]
        for i in range(n-2,-1,-1):
            answer[i] = answer[i] * suffix
            suffix = suffix * nums[i]
        return answer

    # compute prefixes & suffixes in extra arrays
    def soln1(self, nums):
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = nums[i] * prefix[i-1]

        suffix = [0] * n
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]

        answer = [0] * n
        for i in range(n):
            if i == 0:
                answer[i] = suffix[i+1]
            elif i == n-1:
                answer[i] = prefix[i-1]
            else:
                answer[i] = prefix[i-1] * suffix[i+1]
        return answer