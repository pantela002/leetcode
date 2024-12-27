from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = []
        stack.append(root)
        while stack:
            pom1 = stack.pop()
            pom2 = pom1.left
            pom1.left = pom1.right
            pom1.right = pom2
            if pom1.left:
                stack.append(pom1.left)
            if pom1.right:
                stack.append(pom1.right)
        return root
