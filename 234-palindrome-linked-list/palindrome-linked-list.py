# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is now the midpoint of the list
        # now we need to reverse the list from slow to fast
        reverse = None
        curr = slow
        while curr:
            nextTemp = curr.next
            curr.next = reverse
            reverse = curr
            curr = nextTemp
        
        while reverse:
            if head.val != reverse.val:
                return False
            head = head.next
            reverse = reverse.next
        return True