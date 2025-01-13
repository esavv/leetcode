# See: https://leetcode.com/problems/path-sum/
class Solution(object):
    def hasPathSum(self, root, targetSum):
        return self.soln2(root, targetSum)
        # return self.soln1(root, targetSum)

    # recursive approach
    def soln2(self, root, targetSum):
        if not root:
            return False

        res = False
        if root.left:
            res = res or self.soln2(root.left, targetSum - root.val)
        if root.right:
            res = res or self.soln2(root.right, targetSum - root.val)
        if not root.left and not root.right and root.val == targetSum:
            res = True
        return res

    # iterative postorder DFS approach
    def soln1(self, root, targetSum):
        if not root:
            return False
		
        stack, sum = [], 0
        while root or stack:
            while root:
                sum += root.val
                if root.right:
                    stack.append((root.right, sum + root.right.val))
                stack.append((root, sum))
                root = root.left

            root, sum = stack.pop()

            if root.right and stack and root.right == stack[-1][0]:
                stack.pop()
                stack.append((root, sum))
                root = root.right
            else:
                if not root.left and not root.right and sum == targetSum:
                    return True
                root = None
        return False
        