# See: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution(object):
    def nearestExit(self, maze, entrance):
        return self.soln2(maze, entrance)
        # return self.soln1(maze, entrance)

    # BFS with queue
    def soln2(self, maze, entrance):
        from collections import deque
        m, n = len(maze), len(maze[0])

        def isExit(space):
            if space == entrance:
                return False
            row, col = space
            if row in (0, m-1) or col in (0, n-1):
                return True
            return False

        def visit(space):
            row, col = space
            maze[row][col] = 'x'
            return

        def getChildren(space):
            row, col = space
            candidates = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            children = []
            for candidate in candidates:
                x, y = candidate
                if 0 <= x <= m-1 and 0 <= y <= n-1 and maze[x][y] == '.':
                    children.append(candidate)
            return children

        queue = deque([(entrance, 0)])
        visit(entrance)
        while queue:
            space, dist = queue.popleft()
            if isExit(space):
                return dist
            for child in getChildren(space):
                queue.append((child, dist+1))
                visit(child)
        return -1

    # DFS - doesn't work because graph is not acyclic
    def soln1(self, maze, entrance):
        visited = {}
        m, n = len(maze), len(maze[0])
        empty = '.'

        # calculate the smallest possible distance to exit
        x, y = entrance
        smallestDist = min(x, m-1-x, y, n-1-y)
        
        def moveStep(position, distance):
            x, y = position
            if position != entrance and (x == 0 or y == 0 or x == m-1 or y == n-1):
                return distance

            if x in visited:
                visited[x].add(y)
            else:
                visited[x] = set([y])

            candidate_moves = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            minSteps = float("inf")
            for move in candidate_moves:
                i, j = move
                moveVisited = (i in visited) and (j in visited[i])
                if 0 <= i < m and 0 <= j < n and maze[i][j] == empty and not moveVisited:
                    minSteps = min(minSteps, moveStep(move, distance + 1))
                    if minSteps == smallestDist:
                        break
            return minSteps

        minSteps = moveStep(entrance, 0)
        if minSteps == float("inf"):
            return -1
        return minSteps