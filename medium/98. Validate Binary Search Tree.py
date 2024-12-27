# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        high = 99999999999999
        low = -999999999999999
        stack.append([root, low, high])
        while stack:
            pom = stack.pop()
            node,l,h = pom[0],pom[1],pom[2]
            if node:
                if node.val >= h or node.val <= l:
                    return False
                stack.append([node.right, node.val, h])
                stack.append([node.left, l, node.val])
        return True

        #       5
        #      / \
        #     4   6
        #        / \
        #       3   7
