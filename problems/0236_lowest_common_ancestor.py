# See: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.soln4(root, p, q)
        # return self.soln3(root, p, q)
        # return self.soln1(root, p, q)

    # soln #2 on 3/3/2025
    # iterative post-order dfs
    def soln4(self, root, p, q):
        stack1, stack2 = [], []
        while root or stack1:
            while root:
                stack1.append(root)
                stack2.append(root)
                root = root.left
            root = stack1.pop()
            root = root.right
        graph = {}
        lcaNode = None
        while stack2:
            root = stack2.pop()
            graph[root.val] = 0
            if root.val == p.val or root.val == q.val:
                graph[root.val] += 1
            if root.left and graph[root.left.val] >= 1:
                graph[root.val] += 1
            if root.right and graph[root.right.val] >= 1:
                graph[root.val] += 1
            if graph[root.val] >= 2:
                lcaNode = root
                break
        return lcaNode

    # soln #1 on 3/3/2025
    # recursive dfs
    def soln3(self, root, p, q):
        lcaNode = [None]

        def dfs(node):
            if not node or lcaNode[0] != None:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr = (node.val == p.val or node.val == q.val)

            if curr + left + right == 2:
                lcaNode[0] = node

            return curr or left or right

        dfs(root)
        return lcaNode[0]

    # recursive DFS each tree to find p- and q-paths, then compare the paths
    def soln1(self, root, p, q):
        p_path, q_path = [], []
	
        def dfs(root, target, path):
            if root.left and dfs(root.left, target, path):
                path.append(root)
                return True
            if root.right and dfs(root.right, target, path):
                path.append(root)
                return True
            if root.val == target.val:
                path.append(root)
                return True
            return False

        dfs(root, p, p_path)
        dfs(root, q, q_path)

        left, right = 0, 0
        while left < len(p_path) and right < len(q_path) and p_path[left].val != q_path[right].val:
            if len(p_path) - left > len(q_path) - right:
                left += 1
            elif len(p_path) - left < len(q_path) - right:
                right += 1
            else:
                left += 1
                right += 1
        return p_path[left]
        