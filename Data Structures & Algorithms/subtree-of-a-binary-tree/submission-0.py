# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def __init__(self):
        self.res = False  # Default to False, since we are searching for a match

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.check(root, subRoot)
        return self.res

    def check(self, node, subroot):
        if not node:  # Base case: If the current node is None, return
            return
        if self.recurse(node, subroot):  # If the current subtree matches, set res to True
            self.res = True
        self.check(node.left, subroot)  # Continue checking the left subtree
        self.check(node.right, subroot)  # Continue checking the right subtree

    def recurse(self, node, subtreenode):
        if not node and not subtreenode:  # Both nodes are None, subtree matches
            return True
        if not node or not subtreenode or node.val != subtreenode.val:  # Mismatch
            return False
        # Check left and right subtrees
        return self.recurse(node.left, subtreenode.left) and self.recurse(node.right, subtreenode.right)
