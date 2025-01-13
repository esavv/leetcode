# See: https://leetcode.com/problems/path-sum-iii/
from collections import deque
class Solution(object):
    def pathSum(self, root, targetSum):
        return self.soln6(root, targetSum)
        # return self.soln5(root, targetSum)
        # return self.soln4(root, targetSum)
        # return self.soln3(root, targetSum)
        # return self.soln2(root, targetSum)
        # return self.soln1(root, targetSum)

    # pathSum memorization (from other user solutions), but implemented iteratively
    def soln6(self, root, targetSum):
        num, currPathSum = 0, 0
        stack, cache = [], {0:1}
        prev = None
        while root or stack:
            while root and (not prev or root.left != prev) and (not prev or root.right != prev):
                stack.append(root)

                currPathSum += root.val
                oldPathSum = currPathSum - targetSum
                num += cache.get(oldPathSum, 0)
                cache[currPathSum] = cache.get(currPathSum, 0) + 1

                prev = root
                root = root.left

            if root and root.left == prev:
                prev = root
                root = root.right
            elif not root and prev.right:
                root = prev.right
            else:
                prev = stack.pop()

                cache[currPathSum] -= 1
                currPathSum -= prev.val

                if stack:
                    root = stack[-1]
                else:
                    root = None

        return num

    # solution 4 but recursively
    def soln5(self, root, targetSum):
        if not root:
            return 0
        pathSums = {}

        def dfs(root):
            num = 0

            if root.left:
                num += dfs(root.left)
            if root.right:
                num += dfs(root.right)

            pathSums[root] = [root.val]
            if root.val == targetSum:
                num += 1
            if root.left and pathSums[root.left]:
                for path in pathSums[root.left]:
                    pathSums[root].append(path + root.val)
                    if path + root.val == targetSum:
                        num += 1
                pathSums.pop(root.left)
            if root.right and pathSums[root.right]:
                for path in pathSums[root.right]:
                    pathSums[root].append(path + root.val)
                    if path + root.val == targetSum:
                        num += 1
                pathSums.pop(root.right)

            return num
        return dfs(root)

    # store subtree pathSums in a dict and bubble them up
    def soln4(self, root, targetSum):
        num = 0
        stack, pathSums = [], {}
        prev = None
        while root or stack:
            while root and (not prev or root.left != prev) and (not prev or root.right != prev):
                stack.append(root)
                prev = root
                root = root.left

            if root and root.left == prev:
                prev = root
                root = root.right
            elif not root and prev.right:
                root = prev.right
            else:
                prev = stack.pop()

                pathSums[prev] = [prev.val]
                if prev.val == targetSum:
                    num += 1
                if prev.left and pathSums[prev.left]:
                    for path in pathSums[prev.left]:
                        pathSums[prev].append(path + prev.val)
                        if path + prev.val == targetSum:
                            num += 1
                    pathSums.pop(prev.left)
                if prev.right and pathSums[prev.right]:
                    for path in pathSums[prev.right]:
                        pathSums[prev].append(path + prev.val)
                        if path + prev.val == targetSum:
                            num += 1
                    pathSums.pop(prev.right)

                if stack:
                    root = stack[-1]
                else:
                    root = None
        return num

    # soln2 but saving all subpath states to speed up popping (pushing is still slow)  
    def soln3(self, root, targetSum):
        num = 0
        nodeStack, valStack = [], []
        prev = None
        while root or nodeStack:
            while root and (not prev or root.left != prev) and (not prev or root.right != prev):
                nodeStack.append(root)
                newVals = []
                if valStack:
                    newVals = valStack[-1][:]
                newVals.append(0)
                for i in range(len(newVals)):
                    newVals[i] += root.val
                    if newVals[i] == targetSum:
                        num += 1
                valStack.append(newVals)
                prev = root
                root = root.left

            if root and root.left == prev:
                prev = root
                root = root.right
            elif not root and prev.right:
                root = prev.right
            else:
                prev = nodeStack.pop()
                valStack.pop()
                if nodeStack:
                    root = nodeStack[-1]
                else:
                    root = None
        return num

    # just DFS, but calculate subpath values with a 2nd stack
    def soln2(self, root, targetSum):
        num = 0
        nodeStack, valStack = [], []
        prev = None
        while root or nodeStack:
            while root and (not prev or root.left != prev) and (not prev or root.right != prev):
                nodeStack.append(root)
                valStack.append(0)
                for i in range(len(valStack)):
                    valStack[i] += root.val
                    if valStack[i] == targetSum:
                        num += 1
                prev = root
                root = root.left

            if root and root.left == prev:
                prev = root
                root = root.right
            elif not root and prev.right:
                root = prev.right
            else:
                prev = nodeStack.pop()
                valStack.pop()
                for i in range(len(valStack)):
                    valStack[i] -= prev.val
                if nodeStack:
                    root = nodeStack[-1]
                else:
                    root = None
        return num

    # naive BFS + DFS. basically brute force with lots of repetitive calculations
    def soln1(self, root, targetSum):
        num = 0
        lqueue, rqueue = deque(), deque()
        if root:
            lqueue.append(root)
        while lqueue or rqueue:
            while lqueue:
                node = lqueue.popleft()
                num += self.path(node, targetSum)
                if node.left:
                    rqueue.append(node.left)
                if node.right:
                    rqueue.append(node.right)
            while rqueue:
                node = rqueue.popleft()
                num += self.path(node, targetSum)
                if node.left:
                    lqueue.append(node.left)
                if node.right:
                    lqueue.append(node.right)
        return num

    def path(self, root, targetSum):
        num = 0
        stack = []
        prev = None
        val = 0
        while root or stack:
            while root and (not prev or root.left != prev) and (not prev or root.right != prev):
                stack.append(root)
                val += root.val
                if val == targetSum:
                    num += 1
                prev = root
                root = root.left

            if root and root.left == prev:
                prev = root
                root = root.right
            elif not root and prev.right:
                root = prev.right
            else:
                prev = stack.pop()
                val -= prev.val
                if stack:
                    root = stack[-1]
                else:
                    root = None
        return num