# See: https://leetcode.com/problems/odd-even-linked-list/
class Solution(object):
    def oddEvenList(self, head):
        return self.soln1(head)

    # scan to end, scan again to move evens to end. linear time, constant space
    def soln1(self, head):
        curr, end = head, None
        n = 0
        while curr:
            n += 1
            curr, end = curr.next, curr

        curr, prev = head, None
        even = False
        for _ in range(n):
            if even:
                end.next = curr
                prev.next = curr.next
                curr.next = None
                end, curr = curr, prev.next
            else:
                curr, prev = curr.next, curr
            even = not even

        return head