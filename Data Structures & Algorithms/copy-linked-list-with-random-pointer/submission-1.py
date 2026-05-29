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
        nodes = {}

        dummy = Node(0)
        prev = dummy
        cur = head
        
        while cur:
            random_node = None
            if cur.random != None and cur.random not in nodes:
                nodes[cur.random] = Node(cur.random.val)
                random_node = nodes[cur.random]
            elif cur.random != None and cur.random in nodes:
                random_node = nodes[cur.random]
            

            if cur not in nodes:
                nodes[cur] = Node(cur.val)
            copy_node = nodes[cur]
            copy_node.random = random_node

            prev.next = copy_node
            prev = copy_node
            cur = cur.next
        
        return dummy.next
        
            