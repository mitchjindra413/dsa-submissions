# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def _explore(root):
            if not root: 
                return 0
            
            left = _explore(root.left)
            right = _explore(root.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)
        
        _explore(root)
        return self.diameter

        