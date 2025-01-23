# See: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
from collections import deque
class Solution(object):
    def goodNodes(self, root):
        return self.soln2(root)
        # return self.soln1(root)

    # iterative BFS
    def soln2(self, root):
        q = deque([(root, float("-inf"))])
        good = 0

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                good +=1
                maxVal = node.val
            if node.left:
                q.append((node.left, maxVal))
            if node.right:
                q.append((node.right, maxVal))

        return good

    # recursive post-order DFS
    def soln1(self, root):
        def dfs(root, maxVal):
            # handle the current root
            curr = 0
            if root.val >= maxVal:
                curr = 1
                maxVal = root.val

            # recurse down the tree
            left, right = 0, 0
            if root.left:
                left = dfs(root.left, maxVal)
            if root.right:
                right = dfs(root.right, maxVal)

            return curr + left + right

        return dfs(root, float("-inf"))