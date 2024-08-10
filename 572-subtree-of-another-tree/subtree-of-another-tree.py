# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Start from root
        # perform dfs to find a node with the same val as the root of the subtree
        # once we find such a node (if we do) compare root.left and subRoot.left
        # basically perform another dfs of the entire left tree
        # then compare root.right and subRoot.right
        # another dfs of the entire right tree
        # if all checks out, keep traversing until we get a condition where
        # subRoot.left == null and root.left != null
        # subRoot.right == null and root.right != null
        # or root.left != subRoot.left and subRoot.left != null

        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot) -> bool:
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        return root is subRoot