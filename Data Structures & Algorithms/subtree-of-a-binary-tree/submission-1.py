# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            return l or r
    
    def isSameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        
        l = self.isSameTree(root.left, subRoot.left)
        r = self.isSameTree(root.right, subRoot.right)

        return l and r