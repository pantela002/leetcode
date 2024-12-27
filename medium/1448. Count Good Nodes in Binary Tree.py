# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        good = 0
        stack.append([root, root.val])
        while stack:
            pom = stack.pop()
            node , max_val = pom[0], pom[1]
            if node:
                if node.val >= max_val:
                    good+=1
                stack.append([node.right, max(node.val, max_val)])
                stack.append([node.left, max(node.val, max_val)])
        return good

                    
                    
