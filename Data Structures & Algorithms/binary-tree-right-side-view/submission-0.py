# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        levels = []
        q = deque([])
        q.append((root, 0))

        while q:
            node, lvl = q.popleft()
            if len(levels) == lvl:
                levels.append([])
            levels[lvl].append(node.val)

            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl + 1))
        
        res = []
        for lvl in levels:
            res.append(lvl[-1])

        return res