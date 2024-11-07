# See: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)

    # BFS queue approach
    def soln2(self, nums):
        left, right = deque(), deque()
        mid = (len(nums)-1) // 2
        root = TreeNode(val=nums[mid])
        left.append((root, 0, mid-1, mid+1, len(nums)-1))
        while left or right:
            while left:
                parent, leftStart, leftEnd, rightStart, rightEnd = left.popleft()
                if leftEnd >= leftStart:
                    mid = leftStart + (leftEnd - leftStart) // 2
                    parent.left = TreeNode(val=nums[mid])
                    right.append((parent.left, leftStart, mid-1, mid+1, leftEnd))
                if rightEnd >= rightStart:
                    mid = rightStart + (rightEnd - rightStart) // 2
                    parent.right = TreeNode(val=nums[mid])
                    right.append((parent.right, rightStart, mid-1, mid+1, rightEnd))
            while right:
                parent, leftStart, leftEnd, rightStart, rightEnd = right.popleft()
                if leftEnd >= leftStart:
                    mid = leftStart + (leftEnd - leftStart) // 2
                    parent.left = TreeNode(val=nums[mid])
                    left.append((parent.left, leftStart, mid-1, mid+1, leftEnd))
                if rightEnd >= rightStart:
                    mid = rightStart + (rightEnd - rightStart) // 2
                    parent.right = TreeNode(val=nums[mid])
                    left.append((parent.right, rightStart, mid-1, mid+1, rightEnd))
        return root

    # recursive approach
    def soln1(self, nums):
        def addChildren(parent, leftStart, leftEnd, rightStart, rightEnd):
            if leftEnd >= leftStart:
                mid = leftStart + (leftEnd - leftStart) // 2
                parent.left = TreeNode(val=nums[mid])
                addChildren(parent.left, leftStart, mid-1, mid+1, leftEnd)
            if rightEnd >= rightStart:
                mid = rightStart + (rightEnd - rightStart) // 2
                parent.right = TreeNode(val=nums[mid])
                addChildren(parent.right, rightStart, mid-1, mid+1, rightEnd)
            return

  