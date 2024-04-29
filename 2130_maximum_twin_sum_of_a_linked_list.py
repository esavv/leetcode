# See: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
class Solution(object):
    def pairSum(self, head):
        return self.soln3(head)
        # return self.soln2(head)
        # return self.soln1(head)

    # constant space using reversed linked list tip from solutions
    def soln3(self, head):
        # get to the middle
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        prev, curr = None, slow
        while curr:
            nex = curr.next
            curr.next = prev
            prev, curr = curr, nex

        first = head
        second = prev
        ans = 0
        while second:
            twinSum = first.val + second.val
            ans = max(ans, twinSum)
            first, second = first.next, second.next

        return ans

    # use fast & slow pointers and a stack to save a little space...?
    def soln2(self, head):
        stack = []
        fast, slow = head, head
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        ans = 0
        while slow:
            twinSum = stack.pop() + slow.val
            ans = max(ans, twinSum)
            slow = slow.next

        return ans
   
    # linear time & space
    def soln1(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        ans = 0
        left, right = 0, len(vals)-1
        while left < right:
            twinSum = vals[left] + vals[right]
            ans = max(ans, twinSum)
            left, right = left+1, right-1

        return ans