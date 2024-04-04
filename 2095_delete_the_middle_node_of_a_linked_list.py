# See: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
class Solution(object):
    def deleteMiddle(self, head):
        if not head.next:
            return None

        slow, fast, prev = head, head, None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        return head