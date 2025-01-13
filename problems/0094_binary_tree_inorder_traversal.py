# See: https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution(object):
    def inorderTraversal(self, root):
        return self.soln2(root)
        # return self.soln1(root)
    
    # DFS with recursion
    def soln2(self, root):
        def dfs(root, res):
            if not root:
                return

            if root.left:
                dfs(root.left, res)
            res.append(root.val)
            if root.right:
                dfs(root.right, res)
            return

        res = []
        dfs(root, res)
        return res
 
    # DFS with stack
    def soln1(self, root):
        res, stack = [], []

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)

            root = root.right

        return res