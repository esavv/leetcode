# See: https://leetcode.com/problems/binary-tree-upside-down/
class Solution(object):
    def upsideDownBinaryTree(self, root):
        return self.soln2(root)
        # return self.soln1(root)
        
    # soln #2 on 4/29/2025
    # iterative DFS
    def soln2(self, root):
        newRoot = None
        parent, sibling = None, None
        stack = []
        while root:
            stack.append((root, parent, sibling))
            parent, sibling = root, root.right
            root = root.left

        while stack:
            root, parent, sibling = stack.pop()

            if not newRoot:
                newRoot = root

            root.right = parent
            root.left = sibling

            if parent:
                parent.right = None
                parent.left = None
        
        return newRoot

    # soln #1 on 4/29/2025
    # recursive DFS
    def soln1(self, root):
        newRoot = [None]

        def dfs(node, parent, sibling):
            # base case
            if not node:
                return

            # find the left-most leaf
            if node.left:
                dfs(node.left, node, node.right)

            # once we find it, save it (this should only execute once)
            if not newRoot[0]:
                newRoot[0] = node

            # now, update the left-leaf's pointers
            node.right = parent
            node.left = sibling

            # then, update its parent's pointers (ensure the parent is now a leaf)
            if parent:
                parent.right = None
                parent.left = None

        dfs(root, None, None)
        return newRoot[0]