# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
        return None
        # if not root or p == root or q == root:
        #     return root
        # if (p.val < root.val) and (q.val < root.val):
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if (p.val > root.val) and (q.val > root.val):
        #     return self.lowestCommonAncestor(root.right, p, q)

        # return root
        