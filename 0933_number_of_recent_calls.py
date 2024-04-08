# See: https://leetcode.com/problems/number-of-recent-calls/
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.req = deque() # For solution 4

        # self.req = []      # For solution 3
        # self.size = 0      # For solution 3
        # self.pos = 0       # For solution 3

        # self.req = []      # For solution 2

        # self.req = []      # For solution 1

    def ping(self, t):
        return self.soln4(t)
        # return self.soln3(t)
        # return self.soln2(t)
        # return self.soln1(t)

    def soln4(self, t):
        self.req.append(t)
        while self.req[0] < t-3000:
            self.req.popleft()
        return len(self.req)

    def soln3(self, t):
        self.req.append(t)
        self.size += 1

        i = self.pos
        while self.req[i] < t-3000:
            self.size -= 1
            i += 1
        self.pos = i
        return self.size

    def soln2(self, t):
        self.req.append(t)

        while self.req[0] < t-3000:
            self.req.pop(0)
        return len(self.req)
    
    def soln1(self, t):
        self.req.append(t)

        i = len(self.req) - 1
        c = 0
        while i >= 0 and self.req[i] >= t-3000:
            c += 1
            i -= 1
        return c