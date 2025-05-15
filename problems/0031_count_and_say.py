# See: https://leetcode.com/problems/count-and-say/
class Solution(object):
    def countAndSay(self, n):
        return self.soln2(n)
        # return self.soln1(n)
        
    # soln #2 on 5/15/2025
    # iterative
    def soln2(self, n):
        cur = '1'
        def rle(inputStr):
            compressedStr = ''
            run, currChar = 1, inputStr[0]
            for char in inputStr[1:]:
                if char == currChar:
                    run += 1
                else:
                    compressedStr += str(run) + currChar
                    run, currChar = 1, char
            compressedStr += str(run) + currChar
            return compressedStr
        for _ in range(n-1):
            cur = rle(cur)
        return cur

    # soln #1 on 5/15/2025
    # recursion
    def soln1(self, n):
        if n == 1:
            return '1'

        def rle(inputStr):
            compressedStr = ''
            run, currChar = 1, inputStr[0]
            for char in inputStr[1:]:
                if char == currChar:
                    run += 1
                else:
                    compressedStr += str(run) + currChar
                    run, currChar = 1, char
            compressedStr += str(run) + currChar
            return compressedStr

        return rle(self.soln1(n-1))

