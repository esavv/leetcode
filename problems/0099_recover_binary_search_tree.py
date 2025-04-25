# See: https://leetcode.com/problems/recover-binary-search-tree/
class Solution(object):
    def recoverTree(self, root):
        return self.soln1(root)
        
    # soln #1 on 4/25/2025
    # recursion, doesn't work
    def soln1(self, root):
        invalidNodes = []

        def findInvalidNodes(curr, greaterVal, greaterNode, lesserVal, lesserNode):
            if not curr:
                return

            if curr.val > greaterVal:
                invalidNodes.append((curr, greaterNode))
            elif curr.val < lesserVal:
                invalidNodes.append((curr, lesserNode))
            else:
                findInvalidNodes(curr.left, curr.val, curr, lesserVal, lesserNode)
                findInvalidNodes(curr.right, greaterVal, greaterNode, curr.val, curr)
            return

        findInvalidNodes(root, float("inf"), None, float("-inf"), None)
        
        if len(invalidNodes) == 2:
            first, second = invalidNodes[0][0], invalidNodes[1][0]
        else:
            first, second = invalidNodes[0][0], invalidNodes[0][1]
        first.val, second.val = second.val, first.val

        return