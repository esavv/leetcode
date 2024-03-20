# See: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxc = 0
        for c in candies:
            maxc = max(c, maxc)

        result = [False] * len(candies)
        for i, c in enumerate(candies):
            result[i] = c >= maxc - extraCandies
        return result
        