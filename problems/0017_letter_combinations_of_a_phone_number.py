# See: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        return self.soln2(digits)
        # return self.soln1(digits)

    numpad = {
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z']
    }

    # recursive approach
    def soln2(self, digits):
        combos = []
        if not digits:
            return combos
        if len(digits) == 1:
            for c in self.numpad[digits[0]]:
                combos.append(c)
        else:
            for c in self.numpad[digits[0]]:
                for combo in self.soln2(digits[1:]):
                    combos.append(c + combo)
        return combos

    # iterative approach
    def soln1(self, digits):
        combos = []
        for i in range(len(digits)):
            new_combos = []
            for c in self.numpad[digits[i]]:
                if not combos:
                    new_combos.append(c)
                else:
                    for combo in combos:
                        new_combos.append(combo + c)
            combos = new_combos
        return combos