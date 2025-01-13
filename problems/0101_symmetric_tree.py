# See: https://leetcode.com/problems/symmetric-tree/
class Solution(object):
    def isSymmetric(self, root):
        return self.soln2(root)
        # return self.soln1(root)

    # iterative inorder DFS
    def soln2(self, root):
        stack1, stack2 = [], []
        left, right = root.left, root.right
        while (left and right and left.val == right.val) or (stack1 and stack2 and len(stack1) == len(stack2)):
            while (left and right and left.val == right.val):
                stack1.append(left)
                stack2.append(right)
                left, right = left.left, right.right
            if (left and not right) or (right and not left) or (left and right and left.val != right.val):
                return False
            left, right = stack1.pop(), stack2.pop()
            left, right = left.right, right.left
        if (left and not right) or (right and not left) or (left and right and left.val != right.val) or (len(stack1) != len(stack2)):
            return False
        return True

    # recursive preorder DFS
    def soln1(self, root):
        def dfs(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)