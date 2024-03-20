# See: https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        return self.soln2(str1, str2)    
        #return self.soln1(str1, str2)

    def soln2(self, str1, str2):
        mlen = min(len(str1), len(str2))
        gcd = cand = ''
        for i in range(mlen):
            if str1[i] != str2[i]:
                return ''
            cand += str1[i]
            if len(str1) % len(cand) == 0 and len(str2) % len(cand) == 0:
                gcd = cand
        if str1 != gcd * int(len(str1) / len(gcd)) or str2 != gcd * int(len(str2) / len(gcd)):
            return ''
        return gcd

    def soln1(self, str1, str2):
        mlen = min(len(str1), len(str2))
        gcd = cand = ''
        for i in range(mlen):
            if str1[i] != str2[i]:
                return ''
            cand += str1[i]
            if len(str1) % len(cand) != 0 or len(str2) % len(cand) != 0:
                continue
            if str1 == cand * int(len(str1) / len(cand)) and str2 == cand * int(len(str2) / len(cand)):
                gcd = cand
        return gcd
        