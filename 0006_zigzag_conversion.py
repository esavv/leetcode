# See: https://leetcode.com/problems/zigzag-conversion/
class Solution(object):
    def convert(self, s, numRows):
        return self.soln2(s, numRows)
        # return self.soln1(s, numRows)

    # from community, simulate zigzag with down/up bool. equivalent to soln1
    def soln2(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
            
        row, direction = 0, 1
        for char in s:
            rows[row] += char
            row += direction
            if row == numRows-1:
                direction = -1
            elif row == 0:
                direction = 1

        return "".join(rows)

    # compute zigzag position, then distance from the elbow. linear space & time
    def soln1(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = []
        for _ in range(numRows):
            rows.append("")

        ziglen = 2 * numRows - 2
        idx = 0
        for char in s:
            pos = idx % ziglen
            dist = max(numRows - 1 - pos, pos - numRows + 1)
            row_idx = numRows - 1 - dist
            rows[row_idx] += char
            idx += 1

        return "".join(rows)
        # ans = ""
        # for row in rows:
        #     ans += row
        # return ans
    