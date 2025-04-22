# See: https://leetcode.com/problems/triangle/
class Solution(object):
    def minimumTotal(self, triangle):
        return self.soln2(triangle)
        # return self.soln1(triangle)

    # soln #2 on 4/22/2025
    # bubble up min leaves
    def soln2(self, triangle):
        num_rows = len(triangle)

        for i in range(num_rows-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

    # soln #1 on 4/22/2025
    # naive recursive DFS, time limit exceeded
    def soln1(self, triangle):
        num_rows = len(triangle)
        minPathSum = [float("inf")]

        def dfs(row, col, sum):
            if row == num_rows:
                minPathSum[0] = min(minPathSum[0], sum)
            else:
                dfs(row+1, col, sum + triangle[row][col])
                dfs(row+1, col+1, sum + triangle[row][col])
            return

        dfs(0, 0, 0)
        return minPathSum[0]
