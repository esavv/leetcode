# See: https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        minCost = [0] * len(cost)
        minCost[-1] = cost[-1]
        minCost[-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        return min(minCost[0], minCost[1])
        