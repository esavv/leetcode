# See: https://leetcode.com/problems/equal-row-and-column-pairs/
class Solution(object):
    def equalPairs(self, grid):
        return self.soln2(grid)
        # return self.soln1(grid)
        
    # soln #2 from 2/10/2025
    # hashmap
    def soln2(self, grid):
        numPairs = 0
        n = len(grid)
        rows = {}

        for i in range(n):
            row = ''
            for j in range(n):
                row += str(grid[i][j]) + ','
            if row in rows:
                rows[row] += 1
            else:
                rows[row] = 1

        for i in range(n):
            col = ''
            for j in range(n):
                col += str(grid[j][i]) + ','
            if col in rows:
                numPairs += rows[col]
        return numPairs

    # soln #1 from 2/10/2025
    # brute force
    def soln1(self, grid):
        numPairs = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                areEqual = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        areEqual = False
                        break
                if areEqual:
                    numPairs += 1
        return numPairs
