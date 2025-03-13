# See: https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        return self.soln1(candidates, target)
        
    # soln #1 from 3/13/2025
    # backtracking
    def soln1(self, candidates, target):
        combos = []

        def backtrack(target, combo, idx):
            if target == 0:
                combos.append(list(combo))
                return

            if target < 0:
                return

            for i in range(idx, len(candidates)):
                val = candidates[i]
                combo.append(val)
                backtrack(target - val, combo, i)
                combo.pop()
            return
        
        backtrack(target, [], 0)
        return combos