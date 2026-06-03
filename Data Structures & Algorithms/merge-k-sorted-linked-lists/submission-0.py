# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        prev = dummy
        while len(lists) > 0:
            smallest_node = lists[0]
            idx = 0
            for i, head in enumerate(lists):
                if smallest_node.val > head.val:
                    smallest_node = head
                    idx = i
            prev.next = smallest_node
            prev = prev.next
            lists[idx] = smallest_node.next
            if smallest_node.next == None:
                lists.pop(idx)
        
        return dummy.next