# See: https://leetcode.com/problems/guess-number-higher-or-lower/description/
class Solution(object):
    def guessNumber(self, n):
        delta = max(1, n // 2)
        num = delta
        while guess(num) != 0: # type: ignore
            delta = max(1, delta // 2)
            if guess(num) == -1: # type: ignore
                num -= delta
            else:
                num += delta
        return num
