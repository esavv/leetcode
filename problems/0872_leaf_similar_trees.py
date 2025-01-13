# See: https://leetcode.com/problems/leaf-similar-trees/
from collections import deque
class Solution(object):
    def leafSimilar(self, root1, root2):
        # return self.soln3(root1, root2)
        return self.soln2(root1, root2)
        # return self.soln1(root1, root2)

    # iterative attempt #2, now with more ugliness
    def soln3(self, root1, root2):
        stack1, stack2 = deque(), deque()
        leafs1, leafs2 = [], []
        count1 = count2 = 0

        while (root1 or root2) or (stack1 or stack2):
            while root1:
                stack1.append(root1)
                root1 = root1.left
            if stack1:
                root1 = stack1.pop()
                if not root1.left and not root1.right:
                    leafs1.append(root1.val)
                    count1 += 1
                root1 = root1.right

            while root2:
                stack2.append(root2)
                root2 = root2.left
            if stack2:
                root2 = stack2.pop()
                if not root2.left and not root2.right:
                    leafs2.append(root2.val)
                    count2 += 1
                root2 = root2.right
            
            if count1 > 0 and count2 > 0:
                minidx = min(count1, count2) - 1
                if leafs1[minidx] != leafs2[minidx]:
                    return False
        return count1 == count2

    # iterative attempt
    def soln2(self, root1, root2):
        leaf1 = self.lvs(root1)
        leaf2 = self.lvs(root2)

        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True

    def lvs(self, root):
        stack = deque()
        leafs = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.left and not root.right:
                leafs.append(root.val)
            root = root.right
        return leafs

    # first attempt with recursion
    def soln1(self, root1, root2):
        def getLeaves(root, leafList):
            if not root:
                return
            if not root.left and not root.right:
                leafList.append(root.val)
            getLeaves(root.left, leafList)
            getLeaves(root.right, leafList)

        leaf1, leaf2 = [], []
        getLeaves(root1, leaf1)
        getLeaves(root2, leaf2)

        if len(leaf1) != len(leaf2):
            return False
        for i in range(len(leaf1)):
            if leaf1[i] != leaf2[i]:
                return False
        return True