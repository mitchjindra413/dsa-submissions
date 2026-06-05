# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def explore(node, prev_max_val):
            if not node:
                return 0
            
            if node.val >= prev_max_val:
                valid = 1
            else:
                valid = 0
            new_max_val = max(prev_max_val, node.val)
            valid += explore(node.left, new_max_val)
            valid += explore(node.right, new_max_val)

            return valid
        
        return explore(root, float("-inf"))