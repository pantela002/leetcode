# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) and (not q):
            return True
        if not ( p and q and p.val==q.val):
            return False
        stack = []
        stack.append([p,q])
        while stack:
            pom = stack.pop()
            x,y = pom[0], pom[1]
            if (x.left and y.left and x.left.val == y.left.val):
                stack.append([x.left,y.left])
            elif (not x.left and not y.left):
                pass
            else:
                return False
            if (x.right and y.right and x.right.val==y.right.val):
                stack.append([x.right,y.right])
            elif (not x.right and not y.right):
                pass
            else:
                return False
        return True

         
         