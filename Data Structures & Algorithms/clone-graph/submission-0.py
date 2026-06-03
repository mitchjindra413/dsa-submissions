"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
            
        new_nodes = {}
        seen = set()

        def clone_node_val(node, new_nodes):
            if node in new_nodes:
                return new_nodes[node]
            else:
                new_nodes[node] = Node(node.val)
                return new_nodes[node]

        def explore(node, new_nodes, seen):
            if not node:
                return
            if node in seen:
                return
            seen.add(node)
            
            
            clone_node = clone_node_val(node, new_nodes)
            for neighbor in node.neighbors:
                clone_neighbor = clone_node_val(neighbor, new_nodes)
                clone_node.neighbors.append(clone_neighbor)
                explore(neighbor, new_nodes, seen)
        
        explore(node, new_nodes, seen)
        return new_nodes[node]

        