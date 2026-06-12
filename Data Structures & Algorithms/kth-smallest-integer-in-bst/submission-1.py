# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k

        def inorder(node):
            nonlocal res, count
            if not node:
                return

            inorder(node.left)
            if count == 0:
                return 
            count -= 1
            if count == 0:
                res = node.val
                return 
            inorder(node.right)
        
        inorder(root)
        return res

            