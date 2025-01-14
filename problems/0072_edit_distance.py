class Solution(object):
    def minDistance(self, word1, word2):
        return self.soln2(word1, word2)
        # return self.soln1(word1, word2)

    # space-optimized dp with tabulation
    def soln2(self, word1, word2):
        n, m = len(word1), len(word2)
        prev = [i for i in range(n+1)]

        for j in range(m):
            curr = [0 for _ in range(n+1)]
            curr[0] = j+1
            for i in range(n):
                if word1[i] == word2[j]:
                    curr[i+1] = prev[i]
                else:
                    curr[i+1] = min(prev[i+1], prev[i], curr[i]) + 1
            prev = curr
        return prev[n]

    # dp with memoization
    def soln1(self, word1, word2):
        n, m = len(word1), len(word2)
        memo = [[-1 for _ in range(m)] for _ in range(n)]

        def dp(i, j):
            # base case
            if i == -1 or j == -1:
                return max(i, j) + 1

            # memoization step
            if memo[i][j] > -1:
                return memo[i][j]

            # general case
            if word1[i] != word2[j]:
                memo[i][j] = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1)) + 1
            else:
                memo[i][j] = dp(i-1, j-1)
            return memo[i][j]

        return dp(n-1, m-1)
