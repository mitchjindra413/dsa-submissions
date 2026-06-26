class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add(word)

        res = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                self._explore(board, res, r, c, trie.root, set(), "")
        
        return list(res)
    
    def _explore(self, board, res, r, c, node, visited, word):
        if r < 0 or r >= len(board):
            return 
        if c < 0 or c >= len(board[r]):
            return
        key = (r, c)
        if key in visited:
            return
        
        char = board[r][c]
        if char not in node.children:
            return

        visited.add(key)
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        new_word = word + char
        if node.children[char].end:
            res.add(new_word)
        for dr, dc in directions:
            self._explore(board, res, r + dr, c + dc, node.children[char], visited, new_word)
        visited.remove(key)


        
        

        
