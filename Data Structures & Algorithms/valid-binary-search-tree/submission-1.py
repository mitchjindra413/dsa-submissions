# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def explore(node, prev_max, prev_min):
            if not node:
                return True
            if not (prev_min < node.val < prev_max):
                return False
            
            left = explore(node.left, node.val, prev_min)
            right = explore(node.right, prev_max, node.val)

            return left and right
        
        return explore(root, float('inf'), float('-inf'))

            