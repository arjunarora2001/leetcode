# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Start at root
        # Push root on to the ans
        # Push all of the children on to the queue (all left, right chilren)
        ans = []
        if not root:
            return ans
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            tmpStore = []
            for i in range(size):
                tmp = queue.popleft()
                tmpStore.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            ans.append(tmpStore)
        return ans
        # ans = []
        # if not root:
        #     return ans
        # queue = deque([root])
        # ans.append(root.val)
        # if root.left:
        #     queue.append(root.left)
        # if root.right:
        #     queue.append(root.right)
        # # while queue not empty:
        # while queue:
        #     tmp = []
        #     # first push every member of the queue (all children) into an array
        #     for i in queue:
        #         tmp.append(i.val)
        #     # push that array into ans
        #     ans.append(tmp)
        #     # now pop all elements while extracting their left/right children and putting them into the queue
        #     tmpQueue = queue
        #     for i in tmpQueue:
        #         if i.left:
        #             queue.append(i.left)
        #         if i.right:
        #             queue.append(i.right)
        #         queue.popleft()
        # return ans