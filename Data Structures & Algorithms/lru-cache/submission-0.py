class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.store:
            node = self.store[key]
            self._remove_from_list(node)
            self._add_to_list(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]
            node.val = value
            self._remove_from_list(node)
            self._add_to_list(node)
        else:
            node = Node(key, value)
            self.store[key] = node
            self._add_to_list(node)

            if len(self.store) > self.capacity:
                node = self.head.next
                self._remove_from_list(node)
                self.store.pop(node.key)

    
    def _remove_from_list(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_list(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node
        
