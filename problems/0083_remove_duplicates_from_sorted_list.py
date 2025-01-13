# See: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution(object):
    def deleteDuplicates(self, head):
        return self.soln1(head)

    # linear solution
    def soln1(self, head):
        if not head or not head.next:
            return head
        prev, curr = head, head.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head        