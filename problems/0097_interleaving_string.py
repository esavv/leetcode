# See: https://leetcode.com/problems/interleaving-string/
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        return self.soln2(s1, s2, s3)
        # return self.soln1(s1, s2, s3)
        
    # soln #2 on 4/24/2025
    # dynamic programming with memoization
    def soln2(self, s1, s2, s3):
        n, m = len(s1), len(s2)
        memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        def recurse(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if k == len(s3):
                return False

            if memo[i][j] != -1:
                return memo[i][j]

            if i < len(s1) and s3[k] == s1[i] and j < len(s2) and s3[k] == s2[j]:
                memo[i+1][j] = recurse(i+1, j, k+1)
                memo[i][j+1] = recurse(i, j+1, k+1)
                return memo[i+1][j] or memo[i][j+1]
            elif i < len(s1) and s3[k] == s1[i]:
                memo[i+1][j] = recurse(i+1, j, k+1)
                return memo[i+1][j]
            elif j < len(s2) and s3[k] == s2[j]:
                memo[i][j+1] = recurse(i, j+1, k+1)
                return memo[i][j+1]
            return False

        return recurse(0, 0, 0)

    # soln #1 on 4/24/2025
    # three pointers, doesn't work
    def soln1(self, s1, s2, s3):
        i, j, k = 0, 0, 0

        while k < len(s3):
            if i < len(s1) and s3[k] == s1[i]:
                i += 1
                k += 1
            elif j < len(s2) and s3[k] == s2[j]:
                j += 1
                k += 1
            else:
                break
        
        if i == len(s1) and j == len(s2) and k == len(s3):
            return True
        return False