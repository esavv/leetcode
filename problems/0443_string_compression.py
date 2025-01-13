# See: https://leetcode.com/problems/string-compression/
class Solution(object):
    def compress(self, chars):
        return self.soln1(chars)

    # three pointers, linear time & constant space
    def soln1(self, chars):
        if len(chars) <= 1:
            return len(chars)
        left, right, s_end = 0, 0, 0
        while right < len(chars):
            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            group_len = right - left
            chars[s_end] = chars[left]
            s_end += 1
            if group_len > 1:
                group_len_str = list(str(group_len))
                for char in group_len_str:
                    chars[s_end] = char
                    s_end += 1
            left = right
        return s_end