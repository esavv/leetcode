# See: https://leetcode.com/problems/pascals-triangle/
class Solution(object):
    def generate(self, numRows):
        return self.soln2(numRows)
        # return self.soln1(numRows)
        
    # recursion
    def soln2(self, numRows):
        if numRows == 1:
            return [[1]]
        prev = self.soln2(numRows-1)
        curr = [1]
        x, y = 0, 1
        while y < len(prev[-1]):
            curr.append(prev[-1][x] + prev[-1][y])
            x, y = y, y+1
        curr.append(1)
        prev.append(curr)
        return prev

    # brute force / iterative
    def soln1(self, numRows):
        ans = [[1]]
        prev = ans[0]
        for _ in range(1, numRows):
            curr = [1]
            x, y = 0, 1
            while y < len(prev):
                curr.append(prev[x] + prev[y])
                x, y = y, y+1
            curr.append(1)
            ans.append(curr)
            prev = curr
        return ans
