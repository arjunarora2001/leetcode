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
        
        # BETTER SOLUTION: just do an in-order traversal
        # stop once we have k elements in the in-order traversal
        stack = []
        curr = root
        counter = 0
        while curr or stack:
            # add left children of the root
            while curr:
                stack.append(curr)
                curr = curr.left
            # pop element off stack
            curr = stack.pop()
            # process it
            if (counter := counter + 1) == k:
                return curr.val
            curr = curr.right
        return 0


        # def dfs(root):
        #     if not root:
        #         return
        #     nodeSet.add(root.val)
        #     if root.left:
        #         dfs(root.left)
        #     if root.right:
        #         dfs(root.right)
        #     return
        # nodeSet = set()
        # dfs(root)
        # nodeSet = sorted(nodeSet)
        # return nodeSet[k - 1]