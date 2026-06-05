# See: https://leetcode.com/problems/search-a-2d-matrix/  
class Solution(object):
    def searchMatrix(self, matrix, target):
        return self.soln1(matrix, target)

    # soln #1 from 6/05/2025
    # binary search: roll out the matrix into 1d array 
    def soln1(self, matrix, target):
        m = len(matrix)
        if m == 0: return False# example: matrix = []
        n = len(matrix[0])
        if n == 0: return False# example: matrix = [[]]
            
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
        
        numVals = m * n
        left, right = 0, numVals - 1
        while left < right - 1:
            mid = left + (right - left) // 2
            # figure out what index in the matrix mid corresponds to
            midVal = matrix[mid // n][mid % n]
            if midVal == target:
                return True
            if midVal < target:
                left = mid
            elif midVal > target:
                right = mid

        # if we make it out of the loop, we should check left & right a final time
        leftVal = matrix[left // n][left % n]
        rightVal = matrix[right // n][right % n]
        if leftVal == target or rightVal == target:
            return True
        return False

