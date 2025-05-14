# See: https://leetcode.com/problems/rotate-list/
class Solution(object):
    def rotateRight(self, head, k):
        return self.soln1(head, k)
        
    # soln #1 on 5/14/2025
    # two passes
    def soln1(self, head, k):
        # handle n in (0,1) edge cases
        if not head or not head.next:
            return head

        # calculate n & identify the tail of the list
        curr, n = head, 1
        while curr.next:
            n += 1
            curr = curr.next
        tail = curr

        # calculate modK
        modK = k % n

        # handle modK == 0 edge case
        if modK == 0:
            return head

        # identify the new head and new tail, modK-1 and modK nodes from the back
        newTailIdx = n - modK
        newHead, newTail = None, None
        curr, idx = head, 1
        while curr:
            if idx == newTailIdx:
                newTail = curr
                newHead = curr.next
                break
            curr = curr.next
            idx += 1

        # update the list: break newTail > newHead connection, connect oldTail > oldHead
        newTail.next = None
        tail.next = head
        return newHead
