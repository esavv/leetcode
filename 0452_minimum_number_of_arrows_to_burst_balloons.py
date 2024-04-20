# See: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution(object):
    def findMinArrowShots(self, points):
        return self.soln1(points)

    def soln1(self, points):
        balloons = sorted(points, key=lambda point: point[1])
        ans, cur = 1, balloons[0]
        for i in range(1, len(balloons)):
            nex = balloons[i]
            if nex[0] > cur[1]:
                ans += 1
                cur = nex
        return ans