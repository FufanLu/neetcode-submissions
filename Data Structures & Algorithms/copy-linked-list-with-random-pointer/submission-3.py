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
            node = Node(curr.val)
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = curr.next.next

        curr = head
        while curr:
            new_node = curr.next
            new_node.random = curr.random.next if curr.random else None
            curr = curr.next.next

        dummy = Node(1)
        curr = dummy
        while head:
            node = head.next
            curr.next = node
            curr = curr.next
            head = head.next.next

        return dummy.next






        