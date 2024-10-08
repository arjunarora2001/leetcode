# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(-1)
        iterator = ans
        while l1 and l2:
            added = l1.val + l2.val + carry
            if added >= 10:
                added %= 10
                carry = 1
            else:
                carry = 0
            iterator.next = ListNode(added)
            iterator = iterator.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                val = l1.val + carry
                if val >= 10:
                    val %= 10
                    carry = 1
                else:
                    carry = 0
                iterator.next = ListNode(val)
                iterator = iterator.next
                l1 = l1.next
        elif l2:
            while l2:
                val = l2.val + carry
                if val >= 10:
                    val %= 10
                    carry = 1
                else:
                    carry = 0
                iterator.next = ListNode(val)
                iterator = iterator.next
                l2 = l2.next
        if carry:
            iterator.next = ListNode(1)
        return ans.next