# See: https://leetcode.com/problems/online-stock-span/
class StockSpanner(object):

    def __init__(self):
        # soln3 init:
        # self.history = []
        # self.max = float("-inf")

        # soln2 init:
        self.peaks = [] # stack of tuples: (peak price, peak span)

        # soln1 init:
        # self.hist = [] # list of ints
        
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        return self.soln3(price)
        # return self.soln2(price)
        # return self.soln1(price)

    # soln #1 from 3/22/2025
    # history with span skipping
    def soln3(self, price):
        if price >= self.max:
            span = len(self.history) + 1
            self.history.append([price, span])
            self.max = price
            return span

        span = 1
        idx = len(self.history) - 1
        while idx >= 0 and price >= self.history[idx][0]:
            span += self.history[idx][1]
            idx -= self.history[idx][1]
        self.history.append([price, span])
        return span

    # stack optimization. still n^2 time in the worst case, I think, but much better avg. case performance
    def soln2(self, price):
        span = 1
        while self.peaks and self.peaks[-1][0] <= price:
            span += self.peaks[-1][1]
            self.peaks.pop()

        peak = (price, span)
        self.peaks.append(peak)

        return span

    # the naive approach
    def soln1(self, price):
        span = 1
        i = len(self.hist)-1
        while i >= 0 and price >= self.hist[i]:
            span += 1
            i -= 1
        self.hist.append(price)
        return span
