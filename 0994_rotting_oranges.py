# See: https://leetcode.com/problems/rotting-oranges/
class Solution(object):
    def orangesRotting(self, grid):
        return self.soln2(grid)
        # return self.soln1(grid)
    
    # improvement with stack/queue, where t = time to propagate rottens, p = # of oranges in grid
    def soln2(self, grid):
        time, fresh = 0, 0
        lstack, rstack = [], []
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    lstack.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        while lstack or rstack:
            if rstack:
                lstack, rstack = rstack, lstack
            while lstack:
                i, j = lstack.pop()
                neighbors = [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]
                for x, y in neighbors:
                    if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        rstack.append((x,y))
            if rstack:
                time += 1

        if fresh > 0:
            return -1
        return time

    # brute force attempt, where t = time to propagate rottens
    def soln1(self, grid):
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
        if m == 1 and n == 1 and fresh == 1:
            return -1
        time = 0
        while True:
            if fresh == 0:
                return time
            nextg = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    nextg[i][j] = grid[i][j]
            conversions = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if i-1 >= 0 and grid[i-1][j] == 1 and nextg[i-1][j] != 2:
                            nextg[i-1][j] = 2
                            conversions += 1
                            fresh -= 1
                        if j-1 >= 0 and grid[i][j-1] == 1 and nextg[i][j-1] != 2:
                            nextg[i][j-1] = 2
                            conversions += 1
                            fresh -= 1
                        if i+1 < m and grid[i+1][j] == 1 and nextg[i+1][j] != 2:
                            nextg[i+1][j] = 2
                            conversions += 1
                            fresh -= 1
                        if j+1 < n and grid[i][j+1] == 1 and nextg[i][j+1] != 2:
                            nextg[i][j+1] = 2
                            conversions += 1
                            fresh -= 1
            if conversions == 0 and fresh > 0:
                return -1
            grid = nextg
            time += 1		
