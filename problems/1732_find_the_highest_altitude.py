# See: https://leetcode.com/problems/find-the-highest-altitude/
class Solution(object):
    def largestAltitude(self, gain):
        alt = maxa = 0
        for c in gain:
            alt += c
            if alt > maxa:
                maxa = alt
        return maxa
        