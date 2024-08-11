# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # simple bfs
        ans = []
        if not root:
            return ans
        # queue = collections.deque([root])
        queue = collections.deque()
        queue.append(root)
        # print(queue[-1].val)
        # ans.append(root.val)
        # simply return the last element of the queue at any given point
        # after returning it, go through the level and push each element's children into the queue
        while queue:
            size = len(queue)
            ans.append(queue[-1].val) # we now have the right-most element
            for i in range(size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return ans