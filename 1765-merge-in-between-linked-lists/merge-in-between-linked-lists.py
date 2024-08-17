# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aList = list1
        counter = 0
        while counter < a - 1:
            counter += 1
            aList = aList.next
        # ans head now at 2
        bList = aList
        while counter < b + 1:
            counter += 1
            bList = bList.next
        aList.next = list2
        tmp = list2
        while tmp.next:
            tmp = tmp.next
        tmp.next = bList
        return list1
