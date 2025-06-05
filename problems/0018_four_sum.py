# See: https://leetcode.com/problems/4sum/
class Solution(object):
    def fourSum(self, nums, target):
        return self.soln2(nums, target)
        # return self.soln1(nums, target)

    # soln #2 on 6/05/2025
    # hash complement pairs, time limit exceeded
    def soln2(self, nums, target):
        quads = []
        n = len(nums)
        nums.sort()

        compHashes = {}
        for i in range(n-1):
            for j in range(i+1, n):
                sumIJ = nums[i] + nums[j]
                if sumIJ in compHashes:
                    compHashes[sumIJ].append([i,j])
                else:
                    compHashes[sumIJ] = [[i,j]]

        solnHashes = set([])
        for i in range(n-1):
            for j in range(i+1, n):
                complement = target - (nums[i] + nums[j])
                if complement in compHashes:
                    pairList = compHashes[complement]
                    for k, m in pairList:
                        if k > j:
                            soln = [nums[i], nums[j], nums[k], nums[m]]
                            solnHash = '#'.join([str(val) for val in soln])
                            if solnHash not in solnHashes:
                                solnHashes.add(solnHash)
                                quads.append(soln)
        return quads

    # soln #1 on 6/05/2025
    # brute force, time limit exceeded
    def soln1(self, nums, target):
        quads = []
        n = len(nums)
        nums.sort()
        solnHashes = set([])
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for m in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[m] == target:
                            soln = [nums[i], nums[j], nums[k], nums[m]]
                            solnHash = '#'.join([str(val) for val in soln])
                            if solnHash not in solnHashes:
                                solnHashes.add(solnHash)
                                quads.append(soln)
        return quads