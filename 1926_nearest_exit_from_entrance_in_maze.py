# See: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
class Solution(object):
    def nearestExit(self, maze, entrance):
        return self.soln1(maze, entrance)

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

            candidate_moves = [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]
            viable_moves = []
            for move in candidate_moves:
                i, j = move
                moveVisited = False
                if i in visited and j in visited[i]:
                    moveVisited = True			

                if 0 <= i < m and 0 <= j < n and maze[i][j] == empty and not moveVisited:
                    viable_moves.append(move)

            if x in visited:
                visited[x].add(y)
            else:
                visited[x] = set([y])

            minSteps = float("inf")
            for move in viable_moves:
                minSteps = min(minSteps, moveStep(move, distance + 1))
                if minSteps == smallestDist:
                    break
            return minSteps

        minSteps = moveStep(entrance, 0)
        if minSteps == float("inf"):
            return -1
        return minSteps