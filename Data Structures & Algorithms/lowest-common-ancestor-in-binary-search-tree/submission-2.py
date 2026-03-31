# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.helper(root, p.val, q.val)
        return self.res
        
    def helper(self, node, p, q):
        ancestor = False
        if not node:
            return False
        ret1 = self.helper(node.left, p, q)
        ret2 = self.helper(node.right, p, q)
        if node.val == p or node.val == q:
            ancestor = True
        if ancestor and (ret1 or ret2):
            self.res = node
        if ret1 and ret2:
            self.res = node
        return ancestor or ret1 or ret2

        
        
        
