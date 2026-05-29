# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward  = head
        i = n
        while forward and i != 0:
            forward = forward.next
            i -= 1
        
        prev = None
        remove = head
        while forward:
            forward = forward.next
            prev = remove
            remove = remove.next
        
        if not prev:
            return head.next
        
        prev.next = remove.next
        return head
