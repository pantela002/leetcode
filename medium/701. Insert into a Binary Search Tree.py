# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        pom = root
        while pom:
            if pom.val > val:
                if pom.left:
                    pom=pom.left
                else:
                    pom.left = TreeNode(val)
                    break
            else:
                if pom.right:
                    pom=pom.right
                else:
                    pom.right = TreeNode(val)
                    break
        return root
