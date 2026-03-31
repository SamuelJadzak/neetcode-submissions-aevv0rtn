class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.helper(root, p.val, q.val)
        return self.res

    def helper(self, node, p, q):
        if not node:
            return False

        # Recursive calls for left and right children
        ret1 = self.helper(node.left, p, q)
        ret2 = self.helper(node.right, p, q)

        # Check if the current node is one of the targets
        ancestor = node.val == p or node.val == q

        # If two of the three (ancestor, ret1, ret2) are true, this is the LCA
        if (ancestor and (ret1 or ret2)) or (ret1 and ret2):
            self.res = node

        # Return True if current node or any child contains p or q
        return ancestor or ret1 or ret2

        
