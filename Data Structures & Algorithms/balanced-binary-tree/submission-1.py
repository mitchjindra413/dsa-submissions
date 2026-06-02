# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        res = self._height(root)
        return res[1]
    
    def _height(self, root):
        if not root:
            return (0, True)

        left_h, left_valid = self._height(root.left)
        right_h, right_valid = self._height(root.right)
        dif = abs(left_h - right_h)

        if not left_valid or not right_valid or dif > 1:
            return (0, False)
        else:
            return (1 + max(right_h, left_h), True)

