# See: 
class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        idx_s = 0
        for c in t:
            if c == s[idx_s]:
                if idx_s == len(s) - 1:
                    return True
                idx_s += 1
        return False
