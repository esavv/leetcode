# See: https://leetcode.com/problems/equal-row-and-column-pairs/
class Solution(object):
    def equalPairs(self, grid):
        return self.soln2(grid)
        # return self.soln1(grid)
        
    def soln2(self, grid):
        n = len(grid)
        res = 0
        start = [0] * n
        for x in range(n):
            match = True
            if start[x] == -1:
                continue
            for y in range(start[x], n):
                if grid[x][y] == grid[y][x]:
                    start[y] += 1
                else:
                    match = False
                    start[y] = -1
            res += match
        return res

    def soln1(self, grid):
        n = len(grid)
        res = 0
        for x in range(n):
            match = True
            for y in range(n):
                if grid[x][y] != grid[y][x]:
                    match = False
                    break
            res += match
        return res
