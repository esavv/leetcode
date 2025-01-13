# See: https://leetcode.com/problems/add-two-numbers/
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        return self.soln4(l1, l2, 0)
        # return self.soln3(l1, l2, 0)
        # return self.soln2(l1, l2)
        # return self.soln1(l1, l2)

    # soln3 but with improvements from the community
    def soln4(self, l1, l2, rem):
        if not l1 and not l2 and not rem:
            return None
        res = ListNode()
        total = rem
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        res.val = total % 10
        res.next = self.soln4(l1, l2, total // 10)
        return res

    # recursive approach
    def soln3(self, l1, l2, rem):
        if not l1 and not l2:
            if rem == 1:
                return ListNode(val=1)
            return None
        res = ListNode()
        if l1 and l2:
            sum = l1.val + l2.val + rem
            res.val = sum % 10
            res.next = self.soln3(l1.next, l2.next, sum // 10)
        elif l1:
            sum = l1.val + rem
            res.val = sum % 10
            res.next = self.soln3(l1.next, None, sum // 10)
        elif l2:
            sum = l2.val + rem
            res.val = sum % 10
            res.next = self.soln3(None, l2.next, sum // 10)
        return res

    # linear out-of-place approach
    def soln2(self, l1, l2):
        left, right = l1, l2
        remainder = 0
        lmul, rmul = 1, 1
        while left:
            remainder += (left.val * lmul)
            lmul *= 10
            left = left.next
        while right:
            remainder += (right.val * rmul)
            rmul *= 10
            right = right.next
        if remainder == 0:
            return ListNode()
        res = ListNode()
        node, prev = res, None
        while remainder > 0:
            node.val = remainder % 10
            node.next = ListNode()
            node, prev = node.next, node
            remainder = remainder // 10
        prev.next = None
        return res

    # linear in-place approach
    def soln1(self, l1, l2):
        left, right, lprev, rprev = l1, l2, None, None
        llen, rlen = 0, 0
        remainder = 0
        while left and right:
            sum = left.val + right.val + remainder
            if sum > 9:
                remainder = 1
                sum = sum % 10
            else:
                remainder = 0
            left.val, right.val = sum, sum
            left, right, lprev, rprev = left.next, right.next, left, right
            llen, rlen = llen+1, rlen+1
        while left:
            sum = left.val + remainder
            if sum > 9:
                remainder = 1
                sum = sum % 10
            else:
                remainder = 0
            left.val = sum
            left, lprev = left.next, left
            llen += 1
        while right:				
            sum = right.val + remainder
            if sum > 9:
                remainder = 1
                sum = sum % 10
            else:
                remainder = 0
            right.val = sum
            right, rprev = right.next, right
            rlen +=1
        if remainder == 1:
            if llen >= rlen:
                lprev.next = ListNode(val=1)
            else:
                rprev.next = ListNode(val=1)
        if llen >= rlen:
            return l1
        else:
            return l2        
