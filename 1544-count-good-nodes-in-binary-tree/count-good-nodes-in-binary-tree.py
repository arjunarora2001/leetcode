# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Cannot do BFS as it would be difficult to keep track.
    # Must do DFS as all nodes must be visited
    # Must maintain a local maximum for the path we are taking
    # - makes me think we may need a helper function
    # - probably need to start a dfs branch from each node
    # start at the root and make it as good
    # if root.left: 
    #   dfs(root.left, localMax)
    #       if root.val <= localMax:
    #           goodNodes++
    #       if root.left:
    #           dfs(root.left, localMax)
    goodNodeCount = 0
    # node X is good if there are NO nodes greater than X on its path
    def dfs(self, root, localMax):
        if root.val >= localMax:
            self.goodNodeCount += 1
            localMax = root.val
        if root.left:
            self.dfs(root.left, localMax)
        if root.right:
            self.dfs(root.right, localMax)
        return

        
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        localMax = root.val
        self.goodNodeCount += 1
        if root.left:
            self.dfs(root.left, localMax)
        if root.right:
            self.dfs(root.right, localMax)
        return self.goodNodeCount