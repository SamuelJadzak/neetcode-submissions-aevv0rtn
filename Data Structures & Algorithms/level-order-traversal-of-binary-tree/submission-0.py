# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        if not root:
            return res
        while q:
            level = []
            while q:
                level.append(q.popleft())
            for node in level:
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            levelval = []
            for node in level:
                if node:
                    levelval.append(node.val)
            res.append(levelval)
        return res


