# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        arr = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            while curr:
                stack.append(curr)
                curr=curr.left
            if not stack:
                return arr
            else:
                pom = stack.pop()
                arr.append(pom.val)
                stack.append(pom.right)
        return arr
                

