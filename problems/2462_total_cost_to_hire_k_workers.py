# See: https://leetcode.com/problems/total-cost-to-hire-k-workers/
import heapq
class Solution(object):
    def totalCost(self, costs, k, candidates):
        return self.soln2(costs, k, candidates)
        # return self.soln1(costs, k, candidates)

    # min heap approach
    def soln2(self, costs, k, candidates):
        left, right = [], []
        leftIdx, rightIdx = 0, len(costs)-1
        totalCost = 0

        while len(left) < candidates and leftIdx <= rightIdx:
            left.append(costs[leftIdx])
            leftIdx += 1
        while len(right) < candidates and leftIdx <= rightIdx:
            right.append(costs[rightIdx])
            rightIdx -= 1
        heapq.heapify(left)
        heapq.heapify(right)

        for _ in range(k):
            if (left and not right) or (left and right and left[0] <= right[0]):
                minWorker = heapq.heappop(left)
                if leftIdx <= rightIdx:
                    heapq.heappush(left, costs[leftIdx])
                    leftIdx += 1
            elif right:
                minWorker = heapq.heappop(right)
                if leftIdx <= rightIdx:
                    heapq.heappush(right, costs[rightIdx])
                    rightIdx -= 1
            totalCost += minWorker
        return totalCost

    # sliding window approach that fails for time on certain test cases
    def soln1(self, costs, k, candidates):
        remaining = len(costs)
        hired = [0] * len(costs)
        cost = 0
        start_left, start_right = 0, candidates-1
        end_left, end_right = len(costs)-candidates, len(costs)-1
        while k > 0 and remaining >= 2 * candidates:
            # search the two windows to find the min price worker
            min_cost, min_idx = 99999, -1
            for i in range(start_left, start_right+1):
                if not hired[i] and costs[i] < min_cost:
                    min_cost, min_idx = costs[i], i
            for i in range(end_left, end_right+1):
                if not hired[i] and costs[i] < min_cost:
                    min_cost, min_idx = costs[i], i

            # hire the worker
            hired[min_idx] = 1
            cost += min_cost
            remaining -= 1
            k -= 1

            # adjust the sliding windows. check whether we hired from the start window or the end window
            if start_left <= min_idx <= start_right:
                start_right += 1
            else:
                end_left -= 1
        if k > 0:
            # hire the k cheapest workers remaining
            not_hired = []
            for idx, val in enumerate(costs):
                if not hired[idx]:
                    not_hired.append(val)
            not_hired.sort()
            for i in range(k):
                cost += not_hired[i]
        return cost