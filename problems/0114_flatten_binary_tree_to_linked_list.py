# See: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
class Solution(object):
    def flatten(self, root):
        return self.soln2(root)
        # return self.soln1(root)
        
    # soln #2 on 5/29/2025
    # recursive traversal with in-place flattening
    def soln2(self, root):
        def dfs(node):
            if not node:
                return None
        
            lDescendant = dfs(node.left)
            rDescendant = dfs(node.right)

            if lDescendant:
                lDescendant.right = node.right
                node.right = node.left
                node.left = None

            if rDescendant:
                return rDescendant
            elif lDescendant:
                return lDescendant
            return node
        
        dfs(root)
        return

    # soln #1 on 5/29/2025
    # recursive pre-order traversal saved to array
    def soln1(self, root):
        if not root:
            return root

        nodeList = []
        # implements pre-order DFS traversal, and saves "visits" to nodeList
        def dfs(node):
            if not node:
                return
            nodeList.append(node)
            dfs(node.left)
            dfs(node.right)

        # traverse the tree
        dfs(root)

        # clear the root's left child
        root.left = None

        # traverse the nodeList from index 1 to end, adding each node to the right side of the updated tree / linked list
        curr = root
        for i in range(1, len(nodeList)):
            curr.right = nodeList[i]
            nodeList[i].left = None
            curr = nodeList[i]
        return