# See: https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution(object):
    def searchBST(self, root, val):
        return self.soln2(root, val)
        # return self.soln1(root, val)

    # iterative approach with constant space
    def soln2(self, root, val):
        while root is not None and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        return root

    # recursive approach
    def soln1(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)