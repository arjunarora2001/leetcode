# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BRUTE-FORCE:
        #   go through every single node
        #   put them into a set
        #   sort the set
        #   return the k-th element
        # first, go to the smallest node possible
        # do a dfs and keep traversing left
        def dfs(root):
            if not root:
                return
            # print(root.val)
            nodeSet.add(root.val)
            # print(nodeSet)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            return
        nodeSet = set()
        # print(nodeSet)
        dfs(root)
        # print(nodeSet)
        nodeSet = sorted(nodeSet)
        return nodeSet[k - 1]