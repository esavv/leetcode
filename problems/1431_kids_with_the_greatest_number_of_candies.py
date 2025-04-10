# See: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        return self.soln2(candies, extraCandies)
        # return self.soln1(candies, extraCandies)

    # soln #1 from 4/10/2025
    def soln2(self, candies, extraCandies):
        n = len(candies)
        result = [False] * n

        maxCandies = float("-inf")
        for count in candies:
            maxCandies = max(count, maxCandies)

        for i in range(n):
            if candies[i] + extraCandies >= maxCandies:
                result[i] = True

        return result

    # soln #1 from 2/06/2024
    def soln1(self, candies, extraCandies):
        maxc = 0
        for c in candies:
            maxc = max(c, maxc)

        result = [False] * len(candies)
        for i, c in enumerate(candies):
            result[i] = c >= maxc - extraCandies
        return result
        