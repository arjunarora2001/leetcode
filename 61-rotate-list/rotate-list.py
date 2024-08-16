# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        size = 1
        while tail.next:
            size += 1
            tail = tail.next
        k = k % size
        if k == 0:
            return head
        tmp = head
        ans = None
        for i in range(size - k - 1):
            tmp = tmp.next
        ans = tmp.next
        tmp.next = None
        tail.next = head
        return ans