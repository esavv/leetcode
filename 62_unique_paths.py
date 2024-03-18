class Solution(object):
    def uniquePaths(self, m, n):
        return self.soln4(m, n)
        # return self.soln3(m, n)
        # return self.soln2(m, n)
        # return self.soln1(m, n)

    # A combinatorics solution. Linear time + constant space.
    def soln4(self, m, n):
        if m == 1 or n == 1:
            return 1
        
        big, small = m, n
        if n >= m:
            big, small = n, m

        sfact = 1
        for i in range(2, small):
            sfact *= i
        bfact = sfact
        for i in range(small, big):
            bfact *= i
        bsfact = bfact
        for i in range(big, big+small-1):
            bsfact *= i
        return bsfact / (bfact * sfact)
    
    # A DP tabulation solution. Quadratic time + linear space.
    def soln3(self, m, n):
        if m == 1 or n == 1:
            return 1

        prev = [1] * (n)
        for i in range(m-1):
            curr = [0] * (n-1) + [1]
            for j in range(n-2, -1, -1):
                curr[j] = curr[j+1] + prev[j]
            prev = curr
        return prev[0]

    # A DP tabulation solution. Quadratic time + space.
    def soln2(self, m, n):
        if m == 1 or n == 1:
            return 1

        grid = []
        for _ in range(m-1):
            grid.append([0] * (n-1) + [1])
        grid.append([1] * n)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                grid[i][j] = grid[i+1][j] + grid[i][j+1]
        return grid[0][0]

    # A DP recursion / memoization solution. Quadratic time + space.
    def soln1(self, m, n):
        if m == 1 or n == 1:
            return 1
            
        grid = []
        for _ in range(m-1):
            grid.append([0] * (n-1) + [1])
        grid.append([1] * n)

        def paths(i, j):
            # avoid redundant calculations
            if grid[i][j] != 0:
                return grid[i][j]
            grid[i][j] = paths(i+1, j) + paths(i, j+1)
            return grid[i][j]
        return paths(0, 0)