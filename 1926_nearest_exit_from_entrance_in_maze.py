# See: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution(object):
    def nearestExit(self, maze, entrance):
        return self.soln1(maze, entrance)

    # sub-optimal DFS solution that doesn't work
    def soln1(self, maze, entrance):
        visited = {}
        minSteps = float("inf")
        m, n = len(maze), len(maze[0])
        empty = '.'

        x, y = entrance[0], entrance[1]
        smallestDist = min(x, m-1-x, y, n-1-y)
        
        def moveStep(position, distance):
            if minSteps == smallestDist:
                return

            x, y = position[0], position[1]
            if position != entrance and (x == 0 or y == 0 or x == m-1 or y == n-1):
                minSteps = min(minSteps, distance)
                return

            candidate_moves = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            viable_moves = []
            for move in candidate_moves:
                i, j = move[0], move[1]
                moveVisited = False
                if i in visited and j in visited[i]:
                    moveVisited = True			

                if 0 <= i < m and 0 <= j < n and maze[i][j] == empty and not moveVisited:
                    viable_moves.append(move)

            if x in visited:
                visited[x].add(y)
            else:
                visited[x] = set([y])

            for move in viable_moves:
                moveStep(move, distance + 1)
            return

        moveStep(entrance, 0)

        if minSteps == float("inf"):
            return -1
        return minSteps