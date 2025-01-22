# See: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        return self.soln2(spells, potions, success)
        # return self.soln1(spells, potions, success)
        
    # sorting + two pointers
    def soln2(self, spells, potions, success):
        n, m = len(spells), len(potions)
        res = [0] * n
        for i in range(n):
            spells[i] = (spells[i], i)
        spells.sort(key=lambda tup: tup[0])
        potions.sort()
        i, j = 0, m-1
        while i < n:
            while j >= 0 and spells[i][0] * potions[j] >= success:
                j -= 1
            res[spells[i][1]] = m-1 - j
            i += 1
        return res

    # brute force
    def soln1(self, spells, potions, success):
        n, m = len(spells), len(potions)
        res = [0] * n
        for i in range(n):
            for j in range(m):
                product = spells[i] * potions[j]
                if product >= success:
                    res[i] += 1
        return res
