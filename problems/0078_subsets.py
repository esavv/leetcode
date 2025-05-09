# See: https://leetcode.com/problems/subsets/
class Solution(object):
    def subsets(self, nums):
        return self.soln4(nums)
        # return self.soln3(nums)
        # return self.soln2(nums)
        # return self.soln1(nums)

    # soln #4 on 5/09/2025
    # bit manipulation
    def soln4(self, nums):
        n = len(nums)
        subs = []
        for i in range(2 ** n):
            combo = []
            for j in range(n-1, -1, -1):
                if (i & 1) == 1:
                    combo.append(nums[j])
                i >>= 1
            subs.append(list(combo))
        return subs

    # soln #3 on 5/08/2025
    # optimized backtrack
    def soln3(self, nums):
        subs = []
        n = len(nums)

        def backtrack(combo, startIdx):
            subs.append(list(combo))
            for i in range(startIdx,n):
                combo.append(nums[i])
                backtrack(combo, i+1)
                combo.pop()

        backtrack([], 0)
        return subs

    # soln #2 on 5/08/2025
    # iterative backtrack
    def soln2(self, nums):
        subs = [[]]
        n = len(nums)

        for k in range(1,n+1):
            stack = [([], 0)]
            while stack:
                combo, startIdx = stack.pop()
                if len(combo) == k:
                    subs.append(list(combo))
                else:
                    for i in range(startIdx,n):
                        combo.append(nums[i])
                        stack.append((list(combo), i+1))
                        combo.pop()
        return subs

    # soln #1 on 5/08/2025
    # recursive backtrack; C(n,k) for k in (0,n)
    def soln1(self, nums):
        subs = [[]]
        n = len(nums)

        def findCombos(k, combo, startIdx):
            if len(combo) == k:
                subs.append(list(combo))
                return
            for i in range(startIdx,n):
                combo.append(nums[i])
                findCombos(k, combo, i+1)
                combo.pop()

        for k in range(1,n+1):
            findCombos(k, [], 0)

        return subs