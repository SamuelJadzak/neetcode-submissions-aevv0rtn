"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dummy = Node(0)
        dummy.next = head
        node = dummy
        nodeset = {}
        while node:
            nodeset.update({node : Node(node.val if node != dummy else 0)})
            node = node.next
        prevnodecopy = nodeset[dummy]
        node = head
        while node:
            nodecopy = nodeset[node]
            prevnodecopy.next = nodecopy

            if node.random == None:
                nodecopy.random = None
            else: 
                nodecopy.random = nodeset[node.random]
            prevnodecopy = nodecopy
            node = node.next
        return nodeset[dummy.next]




            