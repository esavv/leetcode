class Solution(object):
    def lengthOfLastWord(self, s):
        return self.soln2(s)
        # return self.soln1(s)

    # search backwards
    def soln2(self, s):
        curr, idx = 0, len(s)-1
        while idx >= 0:
            char = s[idx]
            if char != ' ':
                curr += 1
            elif char == ' ' and curr > 0:
                return curr
            idx -= 1
        return curr

    # linear solution
    def soln1(self, s):
        prev, curr = 0, 0
        for char in s:
            if char != ' ':
                curr += 1
            elif char == ' ' and curr > 0:
                prev, curr = curr, 0
        if curr > 0:
            return curr
        return prev