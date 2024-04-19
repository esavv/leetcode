# See: https://leetcode.com/problems/maximum-depth-of-binary-tree/
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
        