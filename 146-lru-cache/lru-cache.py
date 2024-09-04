class LRUCache:
    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.nextNode = None
            self.prevNode = None
  
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.nextNode = self.tail
        self.tail.prevNode = self.head
        self.mapping = {}
    
    def remove(self, node: 'LRUCache.Node') -> None:
        prev = node.prevNode
        nextNode = node.nextNode
        prev.nextNode = nextNode
        nextNode.prevNode = prev
    
    def add(self, node: 'LRUCache.Node') -> None:
        last = self.tail.prevNode
        last.nextNode = node
        node.prevNode = last
        node.nextNode = self.tail
        self.tail.prevNode = node

    def get(self, key: int) -> int:
        """
        if key in map:
            move the currNode to the end of the list
            remove previous occurence of the key in our list
            update map accordingly
        else:
            return -1
            
        """
        if key in self.mapping:
            node = self.mapping[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        if key in map:
            change the mapped value to the new value and remove it from our list
        else:
            evict the first node and add the currNode to the end of the list
            update the map accordingly
        """
        if key in self.mapping:
            node = self.mapping[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if self.size == self.capacity:
                l_node = self.head.nextNode
                self.remove(l_node)
                del self.mapping[l_node.key]
                self.size -= 1
            node = self.Node(key, value)
            self.add(node)
            self.mapping[key] = node
            self.size += 1
            

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)