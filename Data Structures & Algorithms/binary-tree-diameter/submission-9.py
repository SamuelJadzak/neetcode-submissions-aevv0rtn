from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxDiameter

    def helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0 
        
        height_left = self.helper(node.left)
        height_right = self.helper(node.right)
    
        self.maxDiameter = max(self.maxDiameter, height_left + height_right)
        
        return max(height_left, height_right) + 1

        