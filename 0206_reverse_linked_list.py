# See: https://leetcode.com/problems/reverse-linked-list/
class Solution(object):
    def reverseList(self, head):
        return self.soln3(head)
        # return self.soln2(head)
        # return self.soln1(head)
    
    # iterative approach
    def soln3(self, head):
        if head is None or head.next is None:
            return head
        
        prev = None
        cur = head
        next = head.next
        cur.next = prev

        while next is not None:
            prev = cur
            cur = next
            next = next.next
            cur.next = prev
        return cur

    # recursive approach
    def soln2(self, head):
        if head is None or head.next is None:
            return head

        last = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return last

    # recursive approach - inefficient
    def soln1(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        curr = head

        while curr.next is not None:
            prev = curr
            curr = curr.next

        prev.next = None
        curr.next = self.reverseList(head)
        return curr