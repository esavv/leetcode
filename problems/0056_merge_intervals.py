# See: https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        return self.soln1(intervals)
        
    # soln #1 on 5/03/2025
    # sort by first element, merge adjacent overlaps
    def soln1(self, intervals):
        intervals.sort()
        noOverlap = [intervals[0]]

        for i in range(1, len(intervals)):
            startIn, endIn = intervals[i]
            endOut = noOverlap[-1][1]
            if endOut >= startIn:
                noOverlap[-1][1] = max(endIn, endOut)
            else:
                noOverlap.append(intervals[i])

        return noOverlap