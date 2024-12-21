# See: https://leetcode.com/problems/delete-node-in-a-bst/
class Solution(object):
    def deleteNode(self, root, key):
        return self.soln1(root, key)

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