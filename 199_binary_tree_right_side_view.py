# See: https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        return self.soln1(root)

    def soln1(self, root):
        if not root:
            return []

        vals = [root.val]
        queue = deque([root, -1])
        prev = None
        while queue:
            node = queue.popleft()
            if node == -1 and queue:
                queue.append(-1)
                vals.append(prev.val)
            elif node != -1:
                if node.left:
                    queue.append(node.left)
                    prev = node.left
                if node.right:
                    queue.append(node.right)
                    prev = node.right
        return vals