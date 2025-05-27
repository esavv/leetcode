# See: https://leetcode.com/problems/decode-ways/
class Solution(object):
    def numDecodings(self, s):
        return self.soln3(s)
        # return self.soln2(s)
        # return self.soln1(s)

    # soln #3 on 5/27/2025
    # soln2 with cleanup
    def soln3(self, s):
        n = len(s)
        alpha = set([str(i+1) for i in range(26)])
        cache = {}

        def backtrack(i):
            if i in cache:
                return cache[i]
            ans = 0
            if s[i:i+1] in alpha:
                if i == n-1:
                    cache[i] = 1
                    return 1
                ans += backtrack(i+1)
            if i < n-1 and s[i:i+2] in alpha:
                if i == n-2:
                    ans += 1
                else:
                    ans += backtrack(i+2)
            cache[i] = ans
            return ans
        return backtrack(0)

    # soln #2 on 5/27/2025
    # backtracking with caching
    def soln2(self, s):
        n = len(s)
        alpha = set([str(i+1) for i in range(26)])
        cache = {}

        def backtrack(i, j):
            if i in cache and j in cache[i]:
                return cache[i][j]
            if s[i:j] in alpha:
                # we found a valid decoding!
                if j == n:
                    if i in cache:
                        cache[i][j] = 1
                    else:
                        cache[i] = {j: 1}
                    return 1
                ans = backtrack(j, j+1)
                ans += backtrack(j, j+2) if j < n-1 else 0
                if i in cache:
                    cache[i][j] = ans
                else:
                    cache[i] = {j: ans}
                return ans
            else:
                if i in cache:
                    cache[i][j] = 0
                else:
                    cache[i] = {j: 0}
                return 0

        ans = backtrack(0, 1)
        ans += backtrack(0, 2) if n > 1 else 0
        return ans
        
    # soln #1 on 5/27/2025
    # un-optimized backtracking time limit failed
    def soln1(self, s):
        ans = [0]
        n = len(s)
        alpha = set([str(i+1) for i in range(26)])

        def backtrack(i, j):
            if s[i:j] in alpha:
                # we found a valid decoding!
                if j == n:
                    ans[0] += 1
                    return
                backtrack(j, j+1)
                backtrack(j, j+2) if j < n-1 else None
            return

        backtrack(0, 1)
        backtrack(0, 2) if n > 1 else None
        return ans[0]