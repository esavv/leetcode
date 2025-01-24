# See: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
from collections import deque
class Solution(object):
    def maxLevelSum(self, root):
        return self.soln2(root)
        # return self.soln1(root)

    # iterative BFS with 1 queue
    def soln2(self, root):
        maxSum, maxLevel = float("-inf"), 0
        queue = deque([(root, 1)])
        currSum, currLevel = 0, 1
        while queue:
            node, level = queue.popleft()
            if level > currLevel:
                if currSum > maxSum:
                    maxSum, maxLevel = currSum, currLevel
                currSum, currLevel = 0, level
            currSum += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        if currSum > maxSum:
            maxSum, maxLevel = currSum, currLevel
        return maxLevel

    # iterative BFS with 2 queues
    def soln1(self, root):
        maxSum, maxLevel = float("-inf"), 0
        left, right = deque([root]), deque()

        currLevel = 0
        while left or right:
            if left:
                currSum = 0
                currLevel += 1
                while left:
                    node = left.popleft()
                    currSum += node.val
                    if node.left:
                        right.append(node.left)
                    if node.right:
                        right.append(node.right)
                if currSum > maxSum:
                    maxSum, maxLevel = currSum, currLevel

            if right:
                currSum = 0
                currLevel += 1
                while right:
                    node = right.popleft()
                    currSum += node.val
                    if node.left:
                        left.append(node.left)
                    if node.right:
                        left.append(node.right)
                if currSum > maxSum:
                    maxSum, maxLevel = currSum, currLevel

        return maxLevel
