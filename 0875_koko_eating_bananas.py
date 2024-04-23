# See: https://leetcode.com/problems/koko-eating-bananas/
import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        return self.soln3(piles, h)
        # return self.soln2(piles, h)
        # return self.soln1(piles, h)

    # binary search with optimizations & math.ceil cleanup based on other user solutions
    def soln3(self, piles, h):
        maxPile = max(piles)
        total = sum(piles)
		
        if h == len(piles):
            return maxPile
    
        left = (total-1) / h
        right = maxPile+1
        while left < right-1:
            k = (left + right) // 2
            numHours = 0
            for pile in piles:
                numHours += (pile-1) / k + 1
			
            if numHours > h:
                left = k
            else:
                right = k
        return right

    # binary search
    def soln2(self, piles, h):
        maxPile, totalBananas = 0, 0
        for pile in piles:
            maxPile = max(maxPile, pile)
            totalBananas += pile
		
        if h == len(piles):
            return maxPile

        if h >= totalBananas:
            return 1

        left, right = 1, maxPile
        while left < right-1:
            k = (left + right) // 2
            numHours = 0
            for pile in piles:
                numHours += math.ceil(float(pile) / float(k))
			
            if numHours > h:
                left = k
            else:
                right = k
        return right

    # brute force
    def soln1(self, piles, h):
        p = 0
        for pile in piles:
            p = max(p, pile)
		
        if h == len(piles):
            return p

        prev = p
        k = p - 1
        while k > 0:
            numHours = 0
            for pile in piles:
                numHours += math.ceil(float(pile) / float(k))

            if numHours > h:
                return prev

            prev = k
            k -= 1
        return prev