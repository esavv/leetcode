# See: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution(object):
    def maxProfit(self, prices, fee):
        return self.soln2(prices, fee)
        # return self.soln1(prices, fee)

    # DP with memoization + O(1) space
    def soln2(self, prices, fee):
        n = len(prices)
        prevHold, prevFree = -prices[0], 0
        for x in range(1,n):
            currHold = max(prevHold, prevFree - prices[x])
            currFree = max(prevFree, prevHold + prices[x] - fee)
            prevHold, prevFree = currHold, currFree
        return max(prevHold, prevFree)

    # DP with memoization
    def soln1(self, prices, fee):
        n = len(prices)
        hold, free = [0] * n, [0] * n

        hold[0] = -prices[0]
        for x in range(1,n):
            hold[x] = max(hold[x-1], free[x-1] - prices[x])
            free[x] = max(free[x-1], hold[x-1] + prices[x] - fee)

        return max(hold[n-1], free[n-1])
