# See: https://leetcode.com/problems/rotate-image/
class Solution(object):
    def rotate(self, matrix):
        return self.soln1(matrix)

    # soln #1 on 5/21/2025
    # rotate layer by layer
    def soln1(self, matrix):
        n = len(matrix)
        if n == 1: return

        def rotateLayer(start, length):
            x, y = start, start
            tempTop = [0] * (length)
            tempRight = [0] * (length)
            tempBot = [0] * (length)
            tempLeft = [0] * (length)
            # copy the current matrix into tmp space
            for i in range(length):
                tempTop[i] = matrix[x][y+i]
                tempRight[i] = matrix[x+i][y+length]
                tempBot[i] = matrix[x+length][y+length-i]
                tempLeft[i] = matrix[x+length-i][y]
            # rotate each edge over to the next
            for i in range(length):
                matrix[x+i][y+length] = tempTop[i]
                matrix[x+length][y+length-i] = tempRight[i]
                matrix[x+length-i][y] = tempBot[i]
                matrix[x][y+i] = tempLeft[i]

        numLayers = n // 2
        start = 0
        length = n-1
        for _ in range(numLayers):
            rotateLayer(start, length)
            start += 1
            length -= 2
        return