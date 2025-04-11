# See: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.soln6(root, p, q)
        # return self.soln5(root, p, q)
        # return self.soln4(root, p, q)
        # return self.soln3(root, p, q)
        # return self.soln1(root, p, q)

    # soln #1 on 4/11/2025
    # recursive approach
    def soln6(self, root, p, q):
        lcaNode = [None]

        def dfs(node, p, q):
            if lcaNode[0] or not node:
                return 0

            curr = node.val == p.val or node.val == q.val
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if curr + left + right == 2:
                lcaNode[0] = node
                return 0

            return curr + left + right

        dfs(root, p, q)
        return lcaNode[0]

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
            # terminating condition
            if not node or lcaNode[0] != None:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            curr = (node.val == p.val or node.val == q.val)

            # check if LCA
            if curr + left + right == 2:
                lcaNode[0] = node

            return curr or left or right

        dfs(root)
        return lcaNode[0]

    # soln #3 on 3/3/2025
    # riff on soln1 with small cleanup
    def soln5(self, root, p, q):
        p_path, q_path = [], []
	
        def dfs(node, target, path):
            if not node:
                return False
            if node.val == target or dfs(node.left, target, path) or dfs(node.right, target, path):
                path.append(node)
                return True
            return False

        dfs(root, p.val, p_path)
        dfs(root, q.val, q_path)

        p_idx, q_idx = 0, len(q_path) - len(p_path)
        if len(p_path) > len(q_path):
            q_idx, p_idx = 0, len(p_path) - len(q_path)

        while p_path[p_idx].val != q_path[q_idx].val:
            p_idx += 1
            q_idx += 1
        return p_path[p_idx]

    # soln #1
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
        