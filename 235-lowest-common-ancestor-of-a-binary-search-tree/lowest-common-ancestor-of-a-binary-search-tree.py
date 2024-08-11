# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val == root.val or q.val == root.val:
            return root
        if (p.val > root.val and q.val < root.val) or (q.val > root.val and p.val < root.val):
            return root
        if (p.val > root.val) and (q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

        # start from root
        # if one of the nodes is greater than root and the other is lower:
        #   return root
        # if both nodes is lower than root:
        #   new lowest = root.left
        # check again if both are greater or equal to new root
        # therefore, it seems like this is a dfs