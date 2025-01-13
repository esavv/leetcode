# See: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.soln1(root, p, q)

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
        