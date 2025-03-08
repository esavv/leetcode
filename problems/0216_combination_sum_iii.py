# See: https://leetcode.com/problems/combination-sum-iii/
class Solution(object):
    def combinationSum3(self, k, n):
        return self.soln3(k, n)
        # return self.soln2(k, n)
        # return self.soln1(k, n)

    # soln #1 on 3/7/2025
    # recursion / backtrack attempt
    def soln3(self, k, n):
        combos = []

        def backtrack(n, k, nums, combo):
            if n == 0 and k == 0:
                combos.append(combo)
                return

            if n < 1:
                return

            for number in range(nums, 0, -1):
                new_combo = combo[:]
                new_combo.append(number)
                backtrack(n - number, k - 1, number-1, new_combo)
            return

        backtrack(n, k, 9, [])
        return combos

    # soln1 with editorial-inspired renaming
    def soln2(self, k, n):
        res = []
        if n > 45 or (k == 1 and n > 9) or (k > 1 and n == 1):
            return res

        def backtrack(comb, val, sum):
            if len(comb) == k and sum == 0:
                res.append(list(comb))
                return
            elif sum < 0 or len(comb) == k:
                return

            for num in range(val, 10):
                comb.append(num)
                backtrack(comb, num+1, sum - num)
                comb.pop()
            return

        backtrack([], 1, n)

        return res

    # recursive approaach
    def soln1(self, k, n):
        res = []
        if n > 45 or (k ==1 and n > 9) or (k > 1 and n == 1):
            return res
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def find(ans, idx, sum):
            if sum < 0:
                return

            if len(ans) == k and sum == 0:
                res.append(ans)
                return

            for i in range(idx,9):
                tmp = list(ans)
                tmp.append(nums[i])
                find(tmp, i+1, sum - nums[i])
            return

        find([], 0, n)

        return res