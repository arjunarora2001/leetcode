"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # do a BFS
        # at each level, pop an element. the next value in the queue at that time will be the next pointer
        # at each level, store a static array of nodes of that level? may not be constant memory
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        counter = 0
        while queue:
            elem = queue.popleft()
            counter += 1
            # we can use log since we know it's a perfect binary tree
            if math.log2(counter + 1) == math.floor(math.log2(counter + 1)):
                elem.next = None
            else:
                elem.next = queue[0]
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)
        return root
        