# See: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
class Solution(object):
    def findMinArrowShots(self, points):
        return self.soln3(points)
        # return self.soln2(points)
        # return self.soln1(points)

    # soln #2 from 3/20/2025
    # greedy, sort intervals by xEnd ascending
    def soln2(self, points):
        points.sort(key=lambda x: x[1])
        minArrows = 0
        target = float("-inf")

        for point in points:
            if not (point[0] <= target <= point[1]):
                target = point[1]
                minArrows += 1
        
        return minArrows

    # soln #1 from 3/20/2025, doesn't work
    # shoot arrows at points on x-axis with most balloons, rescan x-axis until done
    def soln1(self, points):
        minArrows = 0

        if len(points) == 1:
            return 1

        points.sort()

        n = len(points)
        balloons = set([i for i in range(n)])

        while balloons:
            maxOverlap, maxOverlapIdx = 0, float("-inf")
            xAxis = {}
            for balloon in balloons:
                xStart, xEnd = points[balloon]
                for point in range(xStart, xEnd+1):
                    if point in xAxis:
                        xAxis[point].append(balloon)
                    else:
                        xAxis[point] = [balloon]
                    if len(xAxis[point]) > maxOverlap:
                        maxOverlap, maxOverlapIdx = len(xAxis[point]), point

            for balloon in xAxis[maxOverlapIdx]:
                balloons.remove(balloon)

            minArrows += 1

        return minArrows

    def soln1(self, points):
        balloons = sorted(points, key=lambda point: point[1])
        ans, cur = 1, balloons[0]
        for i in range(1, len(balloons)):
            nex = balloons[i]
            if nex[0] > cur[1]:
                ans += 1
                cur = nex
        return ans