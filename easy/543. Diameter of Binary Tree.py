# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    res = 0
    def md(self, root):
            
            if not root:
                return 0
            a,b = self.md(root.left),self.md(root.right)
            if self.res < a+b:
                self.res = a+b
            return 1+max(a,b)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.md(root)
        return self.res



