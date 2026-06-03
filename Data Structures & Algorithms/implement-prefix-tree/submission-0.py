class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node(0)

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        return cur.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        
        def explore(node):
            if not node:
                return False
            if node.end:
                return True
            
            for child in node.children.values():
                if explore(child):
                    return True
            
            return False

        return explore(cur)

        
        