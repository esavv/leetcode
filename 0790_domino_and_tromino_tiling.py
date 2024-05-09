# See: https://leetcode.com/problems/domino-and-tromino-tiling/
class Solution(object):
    def numTilings(self, n):
        return self.soln4(n)
        # return self.soln3(n)
        # return self.soln2(n)
        # return self.soln1(n)

    # linear time, constant space solution
    def soln4(self, n):
        prev1, prev2, prev3 = 5, 2, 1
        if n == 1:
            return prev3
        if n == 2:
            return prev2
        if n == 3:
            return prev1
        double_sum = 0
        for i in range(4,n+1):
            double_sum += 2*prev3
            ans = 2 + prev1 + prev2 + double_sum
            prev1, prev2, prev3 = ans, prev1, prev2
        return ans % (10 ** 9 + 7)

    # space improvements over soln2
    def soln3(self, n):
        tilings = {}
        for x in range(1,n+1):
            var = 1
            if x >= 3:
                var = 2
            tilings[x] = var
            for y in range(1,x):
                z = x-y
                new_var = tilings[y]
                if z >= 3:
                    new_var = new_var * 2
                tilings[x] += new_var
        ans = tilings[n]
        return ans % (10 ** 9 + 7)

    # time improvements over soln1
    def soln2(self, n):
        tilings = {}
        for x in range(1,n+1):
            var = 1
            if x >= 3:
                var = 2
            tup = ([x], var)
            tilings[x] = [tup]
            for y in range(x-1, 0, -1):
                z = x-y
                for tiling, var in tilings[y]:
                    new_tiling = list(tiling)
                    new_tiling.append(z)
                    new_var = var
                    if z >= 3:
                        new_var = new_var * 2
                    tup = (new_tiling, new_var)
                    tilings[x].append(tup)
        ans = 0
        for _, var in tilings[n]:
            ans += var
        return ans % (10 ** 9 + 7)

    # first attempt, pretty slow
    def soln1(self, n):
        tilings = {}
        for x in range(1,n+1):
            tilings[x] = [[x]]
            for y in range(x-1, x - x//2 - 1, -1):
                z = x-y
                for tiling in tilings[y]:
                    if len([i for i in range(1,z) if i in tiling]) == 0:
                        new_tiling = list(tiling)
                        new_tiling.append(z)
                        tilings[x].append(new_tiling)
            if x % 2 == 0:
                tilings.pop(x/2)
        ans = 0
        for tiling in tilings[n]:
            elem_counts = {}
            multiplier = 1
            for elem in tiling:
                if elem in elem_counts:
                    elem_counts[elem] += 1
                else:
                    elem_counts[elem] = 1
                if elem >= 3:
                    multiplier = multiplier * 2
            num_variations = self.fact(len(tiling))
            for elem in elem_counts:
                num_variations = num_variations / self.fact(elem_counts[elem])
            num_variations = num_variations * multiplier
            ans += num_variations
        return ans % (10 ** 9 + 7)

    def fact(n):
        ans = 1
        for i in range(2,n+1):
            ans = ans * i
        return ans	
