# See: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
class Solution(object):
    def longestZigZag(self, root):
        return self.soln2(root)
        # return self.soln1(root)

    # iterative approach
    def soln2(self, root):
        stack = []
        ans, length, fromleft = 0, 0, False
        while root or stack:
            while root:
                ans = max(ans, length)
                stack.append((root, length, fromLeft))
                root = root.left
                length = length * fromLeft + 1
                fromLeft = False

            root, length, fromLeft = stack.pop()
            root = root.right
            length = length * (not fromLeft) + 1
            fromLeft = True
        return ans

    # recursive approach
    def soln1(self, root):
        def dfs(root, length, fromLeft):
            if not root:
                return 0
            if not root.left and not root.right:
                return length
            if root.left and root.right:
                return max(dfs(root.left, length * fromLeft + 1, False), dfs(root.right, length * (not fromLeft) + 1, True))
            elif root.left:
                return max(length, dfs(root.left, length * fromLeft + 1, False))
            else:
                return max(length, dfs(root.right, length * (not fromLeft) + 1, True))

        return dfs(root, 0, True)
