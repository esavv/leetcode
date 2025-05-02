# See: https://leetcode.com/problems/surrounded-regions/
class Solution(object):
    def solve(self, board):
        return self.soln1(board)

    # soln #1 on 5/02/2025
    # recursive DFS
    def soln1(self, board):
        m, n = len(board), len(board[0])
        if m < 3 or n < 3:
            return

        visited = set()
        surroundedRegions = []

        def dfs(i, j, region, surrounded):
            # add it to the region
            region.append((i,j))

            # mark it as visited
            visited.add((i,j))

            # check if it's on an edge
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                surrounded = False

            # explore its O neighbors
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in neighbors:
                # if it's on the board, and it's an O, and it's not already visited
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x,y) not in visited:
                    surrounded = dfs(x, y, region, surrounded) and surrounded
            return surrounded

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    # create a new region with space (i,j), initialized as surrounded
                    region = []
                    # explore the region
                    surrounded = dfs(i, j, region, True)
                    # add region to regions list if surrounded
                    if surrounded:
                        surroundedRegions.append(region)

        for region in surroundedRegions:
            # capture each element in the region
            for i, j in region:
                board[i][j] = 'X'
        return