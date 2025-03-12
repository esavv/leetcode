# See: https://leetcode.com/problems/delete-node-in-a-bst/
class Solution(object):
    def deleteNode(self, root, key):
        return self.soln3(root, key)
        # return self.soln2(root, key)
        # return self.soln1(root, key)

    # soln #2 from 3/12/2025
    # soln2 with improvements
    def soln3(self, root, key):
        if not root:
            return None
        
        if root.val > key:
            root.left = self.soln3(root.left, key)
        elif root.val < key:
            root.right = self.soln3(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left and not root.right:
                root = root.left
            elif not root.left and root.right:
                root = root.right
            else:
                parent = root.left
                while parent.right:
                    parent = parent.right
                parent.right = root.right
                root = root.left
        return root

    # soln #1 from 3/12/2025
    # recursion without BST logic
    def soln2(self, root, key):

        def findAndDelete(node, root):
            if not node:
                return None

            if node.val == key:
                # node is a leaf
                if not node.left and not node.right:
                    if node == root:
                        root = None
                    return None

                # node has 1 child
                if node.left and not node.right:
                    if node == root:
                        root = node.left
                    return node.left
                if node.right and not node.left:
                    if node == root:
                        root = node.right
                    return node.right

                # node has 2 children
                if node.left and node.right:

                    # demote node.right
                    parent = node.left
                    while parent.right:
                        parent = parent.right
                    parent.right = node.right

                    # promote node.left
                    if node == root:
                        root = node.left
                    return node.left
            else:
                node.left = findAndDelete(node.left, root)
                node.right = findAndDelete(node.right, root)
                return node

        root = findAndDelete(root, root)
        return root

    # naive. arbitrary promote left child over right child
    def soln1(self, root, key):
        prev, curr = None, root
        prevLeft = True
        while curr and curr.val != key:
            prev = curr
            if curr.val < key:
                prevLeft = False
                curr = curr.right
            else:
                prevLeft = True
                curr = curr.left

        # empty root or no key
        if not curr:
            return root

        # key is a leaf
        if not curr.left and not curr.right:
            if key == root.val:
                return None
            if prevLeft:
                prev.left = None
            else:
                prev.right = None
            return root

        # key has 1 child
        if curr.left and not curr.right:
            if key == root.val:
                return curr.left
            if prevLeft:
                prev.left = curr.left
            else:
                prev.right = curr.left
            return root
        if curr.right and not curr.left:
            if key == root.val:
                return curr.right
            if prevLeft:
                prev.left = curr.right
            else:
                prev.right = curr.right
            return root

        # key has 2 children
        if key == root.val:
            root = curr.left
        else:	
            if prevLeft:
                prev.left = curr.left
            else:
                prev.right = curr.left

        leaf = curr.left
        while leaf.right:
            leaf = leaf.right

        leaf.right = curr.right
        return root