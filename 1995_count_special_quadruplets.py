# See: https://leetcode.com/problems/count-special-quadruplets/
class Solution(object):
    def countQuadruplets(self, nums):
        return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # adapting another user's solution but start from left - O(n^2) time
    def soln3(self, nums):
        ans = 0
        n = len(nums)
        sums = {}
        sums[nums[0] + nums[1]] = 1

        for c in range(2, n-1):
            for d in range(c+1, n):
                val = nums[d] - nums[c]
                if val in sums:
                    ans += sums[val]
            
            for a in range(0, c):
                val = nums[a] + nums[c]
                if val not in sums:
                    sums[val] = 0
                sums[val] += 1
        return ans

    # hash the sums seen so far (a + b + c) and compare to each d - O(n^3) time
    def soln2(self, nums):
        n = len(nums)
        sumCounts = {}
        ans = 0
        for c in range(2, n-1):
            for a in range(c-1):
                for b in range(a+1, c):
                    sum = nums[a] + nums[b] + nums[c]
                    if sum not in sumCounts:
                        sumCounts[sum] = 0
                    sumCounts[sum] += 1
            d = c + 1
            if nums[d] in sumCounts:
                ans += sumCounts[nums[d]]
        return ans

    # brute force solution - O(n^4) time
    def soln1(self, nums):
        n = len(nums)
        ans = 0
        for x in range(n-3):
            for y in range(x+1, n-2):
                for z in range(y+1, n-1):
                    for w in range(z+1, n):
                        if nums[x] + nums[y] + nums[z] == nums[w]:
                            ans += 1
        return ans
