# See: https://leetcode.com/problems/non-overlapping-intervals/
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        return self.soln1(intervals) 

    # soln #1 from 3/14/2025
    # sort by 2nd element ascending + two pointer traversal
    def soln1(self, intervals):
        minRemovals = 0
        n = len(intervals)

        intervals.sort(key=lambda interval: interval[1])

        def overlap(first, second):
            starti, endi = first
            startj, endj = second

            # one fully contains the other
            if (starti <= startj and endi >= endj) or (startj <= starti and endj >= endi):
                return True

            # partial overlaps
            if (starti <= startj and startj < endi) or (startj <= starti and starti < endj):
                return True

            return False

        left, right = 0, 1
        while right < n:
            while right < n and overlap(intervals[left], intervals[right]):
                minRemovals += 1
                right += 1

            while right < n and not overlap(intervals[left], intervals[right]):
                left, right = right, right + 1

        return minRemovals