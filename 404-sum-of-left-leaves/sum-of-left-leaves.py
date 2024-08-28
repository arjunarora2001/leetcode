# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, side) -> int:
            if not root:
                return
            if not root.left and not root.right and side == "Left":
                self.ans += root.val
                return
            dfs(root.left, "Left")
            # dfs(root.left)
            dfs(root.right, "Right")
        dfs(root, "Root")
        return self.ans