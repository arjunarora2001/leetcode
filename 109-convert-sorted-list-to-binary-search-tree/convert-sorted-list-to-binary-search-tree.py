# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # need a way to constantly find the middle of the linked list: fast and slow pointers
        def getMiddle(root):
            slow = root
            fast = root
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        middle = getMiddle(head)
        node = TreeNode(middle.val)
        node.right = self.sortedListToBST(middle.next)
        middle.next = None
        node.left = self.sortedListToBST(head)
        return node