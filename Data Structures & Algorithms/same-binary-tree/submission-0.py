# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.helper(p, q)
        return self.res

    def helper(self, p, q):
        if not p and not q:
            return
        elif not p or not q:
            self.res = False
            return
        if p.val != q.val:
            self.res = False
        self.helper(p.right, q.right)
        self.helper(p.left, q.left)
        return


        

