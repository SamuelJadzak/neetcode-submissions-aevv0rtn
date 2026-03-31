# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        if root:
            while q:
                qlen = len(q)
                temp = None
                for i in range(qlen):
                    temp = q.popleft()
                    if temp.left:         
                        q.append(temp.left)
                    if temp.right:
                        q.append(temp.right)
                res.append(temp.val)
        return res