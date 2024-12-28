# See: https://leetcode.com/problems/decode-string/
class Solution(object):
    def decodeString(self, s):
        return self.soln1(s)

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
