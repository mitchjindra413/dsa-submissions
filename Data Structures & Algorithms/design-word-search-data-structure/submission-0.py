class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        
        cur.end = True

    def search(self, word: str) -> bool:

        def find(node, idx):
            if not node:
                return False
            if idx == len(word):
                return node.end
            
            char = word[idx]
            if char in node.children:
                return find(node.children[char], idx + 1)
            
            if char == ".":
                for child in node.children:
                    if find(node.children[child], idx + 1):
                        return True

            return False
        
        return find(self.root, 0)

        
