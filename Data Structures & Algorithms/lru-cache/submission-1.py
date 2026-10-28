class Node:
    def __init__(self, val=0, prev=None, next=None, key=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._deleteNode(node)
            self._moveToHead(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._deleteNode(node)
            self._moveToHead(node)
        
        else:
            node = Node(key=key, val=value)
            self.cache[key] = node
            self._moveToHead(node)
            if len(self.cache) > self.capacity:
                dele_node = self.tail.prev
                self._deleteNode(dele_node)
                del self.cache[dele_node.key]


            
    
    def _deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _moveToHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        
