# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft: bool):
            if not root:
                return
            if not root.left and not root.right and isLeft:
                self.ans += root.val
                return
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return self.ans