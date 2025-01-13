# See: https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        return self.soln3(n)
        # return self.soln2(n)
        # return self.soln1(n)

    # hacky iterative DFS using hint from community
    def soln3(self, n):
        res = []
        stack = []
        openP, closeP = 0, 0
        combo = ""
        while stack or openP + closeP < 2*n:
            while openP < n:
                if stack and openP == closeP:
                    combo, openP, closeP = stack.pop()
                combo += "("
                openP += 1
                stack.append((combo, openP, closeP))

            combo, openP, closeP = stack.pop()
            if openP + closeP == 2*n:
                res.append(combo)
            elif closeP < n and closeP < openP:
                combo += ")"
                closeP += 1
                stack.append((combo, openP, closeP))
        return res

    # dynamic programming, iterative approach
    def soln2(self, n):
        combos = [[] for _ in range(n+1)] 
        combos[1] = ["()"]

        for i in range(2, n+1):
            res_set = set()
            large, small = i-1, 1
            while large >= small:
                for combo1 in combos[large]:
                    for combo2 in combos[small]:
                        res_set.add(combo1 + combo2)
                        res_set.add(combo2 + combo1)
                large -= 1
                small += 1
            for combo in combos[i-1]:
                res_set.add("(" + combo + ")")
            for combo in res_set:
                combos[i].append(combo)
        return combos[n]

    # dynamic programming, recursion with memoization
    def soln1(self, n):
        combos = [[] for _ in range(n+1)] 
        combos[1] = ["()"]

        def getCombos(n, combos):
            if combos[n]:
                return combos[n]
						
            res_set = set()
            large, small = n-1, 1
            while large >= small:
                for combo1 in getCombos(large, combos):
                    for combo2 in getCombos(small, combos):
                        res_set.add(combo1 + combo2)
                        res_set.add(combo2 + combo1)
                large -= 1
                small += 1
            for combo in getCombos(n-1, combos):
                res_set.add("(" + combo + ")")
            for combo in res_set:
                combos[n].append(combo)
            return combos[n]

        return getCombos(n, combos)
