"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head

        while curr:
            temp = curr.next
            curr.next = Node(curr.val, temp)
            curr = curr.next.next

        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        c = dummy
        curr = head
        while curr:
            c.next = curr.next
            c = c.next
            curr = curr.next.next

        return dummy.next

        