# See: https://leetcode.com/problems/surrounded-regions/
class Solution(object):
    def solve(self, board):
        return self.soln2(board)
        # return self.soln1(board)

    # soln #2 on 5/02/2025
    # recursive DFS with editorial help
    def soln2(self, board):
        m, n = len(board), len(board[0])
        if m < 3 or n < 3:
            return

        top    = [(  0,   j) for j in range(n)]
        bottom = [(m-1,   j) for j in range(n)]
        left   = [(  i,   0) for i in range(1, m-1)]
        right  = [(  i, n-1) for i in range(1, m-1)]
        borders = top + bottom + left + right

        def dfs(i, j):
            board[i][j] = 'E'
            neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for x, y in neighbors:
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                     dfs(x, y)
            return

        for i, j in borders:
            if board[i][j] == 'O':
                dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'E':
                    board[i][j] = 'O'
        return

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