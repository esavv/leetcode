# See: https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        return self.soln2(s)
        # return self.soln1(s)

    # soln #1 from 3/01/2025
    # recursive approach
    def soln2(self, s):
        def decode(k, idx):
            decoded = ''
            while idx < len(s):
                while idx < len(s) and ord('a') <= ord(s[idx]) <= ord('z'):
                    decoded += s[idx]
                    idx += 1
                if idx < len(s) and s[idx] == ']':
                    idx += 1
                    break
                num = ''
                while idx < len(s) and ord('0') <= ord(s[idx]) <= ord('9'):
                    num += s[idx]
                    idx += 1
                if len(num) > 0:
                    substr, idx = decode(int(num), idx+1)
                    decoded += substr
            return decoded * k, idx
        return decode(1, 0)[0]

    # recursive approach. n = input string length, k = # of expansions required
    def soln1(self, s):
        def decode(idx, k):
            ans, res = '', ''
            while idx < len(s) and s[idx] != ']':
                while idx < len(s) and 'a' <= s[idx] <= 'z':
                    res += s[idx]
                    idx += 1
                k_str = ''
                while idx < len(s) and '0' <= s[idx] <= '9':
                    k_str += s[idx]
                    idx += 1
                if idx < len(s) and s[idx] == '[':
                    substr, idx = decode(idx + 1, int(k_str))
                    res += substr
            for _ in range(k):
                ans += res
            return ans, idx + 1
        res, _ = decode(0, 1)
        return res
