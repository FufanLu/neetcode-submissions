# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow
        second = mid.next
        mid.next = None
        curr = second
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        second = prev
        curr = head

        while second:
            temp1 = curr.next
            curr.next = second
            temp2 = second.next
            second.next = temp1
            second = temp2
            curr = curr.next.next
            
            
        
        