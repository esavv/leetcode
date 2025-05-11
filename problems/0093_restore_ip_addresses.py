# See: https://leetcode.com/problems/restore-ip-addresses/
class Solution(object):
    def restoreIpAddresses(self, s):
        return self.soln2(s)
        # return self.soln1(s)
        
    # soln #2 on 5/11/2025
    # backtracking
    def soln2(self, s):
        validIPs = []
        n = len(s)
        
        def backtrack(dots, startIdx, addr):
            if dots == -1:
                validIPs.append(''.join(addr))
                return
            if dots > 0:
                numRange = range(startIdx, min(startIdx+3, n - dots))
                pad = '.'
            else:
                numRange = range(n-1, n)
                pad = ''
            for i in numRange:
                currNum = s[startIdx:i+1]
                if currNum == '0' or (currNum[0] != '0' and 0 <= int(currNum) <= 255):
                    addr.append(currNum + pad)
                    backtrack(dots-1, i+1, addr)
                    addr.pop()
            return

        backtrack(3, 0, [])
        return validIPs 

    # soln #1 on 5/11/2025
    # recursive DFS
    def soln1(self, s):
        validIPs = []
        n = len(s)

        def dfs(dots, numStr, candidate, i):
            numStr += s[i]
            validNum = 0 < len(numStr) < 4 and 0 <= int(numStr) <= 255

            if i == n-1 and validNum and dots == 0:
                candidate += numStr
                validIPs.append(candidate)

            if i < n-1:
                if validNum and dots > 0:
                    dfs(dots-1, '', candidate + numStr + '.', i+1)
                if len(numStr) < 3 and numStr != '0':
                    dfs(dots, numStr, candidate, i+1)

        dfs(3, '', '', 0)
        return validIPs