# See: https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # soln #1 on 4/18/2025
    # backtracking
    def soln1(self, nums):
        perms = []

        def backtrack(remaining, perm):
            if len(perm) == len(nums):
                perms.append(list(perm))
                return
            
            for val in remaining:
                perm.append(val)
                newRemaining = set(remaining)
                newRemaining.remove(val)
                backtrack(newRemaining, perm)
                perm.pop()
            return
        numSet = set(nums)
        backtrack(numSet, [])

        return perms

    # soln #2 on 4/18/2025
    # stack
    def soln2(self, nums):
        perms = []
        stack = [(set(nums), [])]
        while stack:
            currRemaining, perm = stack.pop()
            if len(perm) == len(nums):
                perms.append(perm)
            for val in currRemaining:
                perm.append(val)
                nextRemaining = set(currRemaining)
                nextRemaining.remove(val)
                stack.append((nextRemaining, list(perm)))
                perm.pop()
        return perms