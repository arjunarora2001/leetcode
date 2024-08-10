# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    def dfs(self, node):
        left = self.dfs(node.left) if node.left else 0
        right = self.dfs(node.right) if node.right else 0
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # distance between the longest depth on the right side and the left side
        # not that - because if we have a very imbalanced tree, the longest path may be on a singular side
        self.dfs(root)
        return self.diameter