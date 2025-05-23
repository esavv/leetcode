# See: https://leetcode.com/problems/gas-station/
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        return self.soln2(gas, cost)
        # return self.soln1(gas, cost)

    # soln #2 on 5/22/2025
    # greedy-ish
    def soln2(self, gas, cost):
        n = len(gas)
        start = 0
        while start < n:
            currSum = gas[start] - cost[start]
            if currSum < 0:
                start += 1
                continue
            end = start
            while currSum >= 0:
                end = (end + 1) % n
                if end == start:
                    return start
                currSum += gas[end] - cost[end]
            # if we make it here, we ran out of gas
            if end < start:
                return -1
            start = end
        return -1

    # soln #1 on 5/22/2025
    # sliding window
    def soln1(self, gas, cost):
        n = len(gas)
        net = [gas[i] - cost[i] for i in range(n)]

        if n == 1:
            return 0 if net[0] >= 0 else -1

        maxSum = 0
        i = 0
        while i < n:
            # explore the current window candidate
            currSum = net[i]
            # move onto the next candidate if this window starts negative
            if currSum <= 0:
                i += 1
                continue
            # otherwise, see if we can expand this window
            if currSum > maxSum:
                maxSum = currSum

            # try to expand the window, wrap to the start if it reaches the end
            j = (i + 1) % n
            while j != i:
                # if the sum dips below 0, we're done with this window
                if currSum + net[j] < 0:
                    break
                # otherwise, confirm the window's expansion
                currSum += net[j]
                # check if we've found a new max
                if currSum > maxSum:
                    maxSum = currSum
                # try to expand the window again
                j = (j + 1) % n

            # if we fully wrapped around, we're done
            if j == i:
                return i
            # if we've wrapped but not fully, we're done checking windows
            if j < i:
                i = n
            # otherwise start looking for the next candidate window
            else:
                i = j + 1
        return -1