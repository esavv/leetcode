# See: https://leetcode.com/problems/same-tree/
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        return self.soln3(p, q)
        # return self.soln2(p, q)
        # return self.soln1(p, q)

    # bfs approach
    def soln3(self, p, q):
        leftp, rightp = deque(), deque()
        leftq, rightq = deque(), deque()
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        leftp.append(p)
        leftq.append(q)

        while (leftp or rightp) or (leftq or rightq):
            while leftp or leftq:
                rootp = leftp.popleft()
                rootq = leftq.popleft()
                if rootp.left or rootq.left:
                    if not (rootp.left and rootq.left and (rootp.left.val == rootq.left.val)):
                        return False
                    rightp.append(rootp.left)
                    rightq.append(rootq.left)
                if rootp.right or rootq.right:
                    if not (rootp.right and rootq.right and (rootp.right.val == rootq.right.val)):
                        return False
                    rightp.append(rootp.right)
                    rightq.append(rootq.right)

            while rightp or rightq:
                rootp = rightp.popleft()
                rootq = rightq.popleft()
                if rootp.left or rootq.left:
                    if not (rootp.left and rootq.left and (rootp.left.val == rootq.left.val)):
                        return False
                    leftp.append(rootp.left)
                    leftq.append(rootq.left)
                if rootp.right or rootq.right:
                    if not (rootp.right and rootq.right and (rootp.right.val == rootq.right.val)):
                        return False
                    leftp.append(rootp.right)
                    leftq.append(rootq.right)
        return True

    # recursive dfs approach
    def soln2(self, p, q):
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            res = True
            if left.left or right.left:
                res = res and dfs(left.left, right.left)
            if left.right or right.right:
                res = res and dfs(left.right, right.right)
            return res

        return dfs(p, q)

    # iterative dfs approach
    def soln1(self, p, q):
        rootp, rootq = p, q
        stackp, stackq = [], []
        
        while (rootp or stackp) or (rootq or stackq):
            while rootp or rootq:
                if not (rootp and rootq and (rootp.val == rootq.val)):
                    return False
                stackp.append(rootp)
                stackq.append(rootq)
                rootp = rootp.left
                rootq = rootq.left

            rootp = stackp.pop()
            rootq = stackq.pop()
            rootp = rootp.right
            rootq = rootq.right
        return True        