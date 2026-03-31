"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def helper(node, visited):
            if node:
                if node in visited:
                    return visited[node]
                dcNode = Node(node.val)
                for neighbor in node.neighbors:
                    visited[node] = dcNode
                    result = helper(neighbor, visited)
                    if result is not None:
                        dcNode.neighbors.append(result)
                return dcNode
        return helper(node, {})