# See: https://leetcode.com/problems/relative-ranks/
import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        return self.soln2(score)
        # return self.soln1(score)

    # one priority queue with editorial help
    def soln2(self, score):
        n = len(score)
        score_tup = []
        for idx, val in enumerate(score):
            score_tup.append((-val, idx))
        heapq.heapify(score_tup)

        res = [0] * n
        for i in range(1,n+1):
            _, idx = heapq.heappop(score_tup)
            place = str(i)
            if i == 1:
                place = 'Gold Medal'
            elif i == 2:
                place = 'Silver Medal'
            elif i == 3:
                place = 'Bronze Medal'
            res[idx] = place
        return res

    # two priority queues
    def soln1(self, score):
        score_tup = []
        for idx, val in enumerate(score):
            score_tup.append((-val, idx))
        heapq.heapify(score_tup)

        places_tup = []
        for i in range(1,len(score)+1):
            _, idx = heapq.heappop(score_tup)
            place = str(i)
            if i == 1:
                place = 'Gold Medal'
            elif i == 2:
                place = 'Silver Medal'
            elif i == 3:
                place = 'Bronze Medal'
            places_tup.append((idx, place))
        heapq.heapify(places_tup)

        res = []
        while places_tup:
            _, place = heapq.heappop(places_tup)
            res.append(place)
        return res
        