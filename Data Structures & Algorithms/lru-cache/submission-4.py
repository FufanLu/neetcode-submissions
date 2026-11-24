class Node:
    def __init__(self, val=0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = 0


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._deleteNode(node)
        self._addToHead(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._deleteNode(node)
            self._addToHead(node)
        else:
            self.cache[key] = Node(value)
            node = self.cache[key]
            node.key = key
            self._addToHead(node)
            if len(self.cache) > self.capacity:
                del_node = self.tail.prev
                d_key = del_node.key
                self._deleteNode(del_node)
                del self.cache[d_key]
            

    
    def _addToHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def _deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        
