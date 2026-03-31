# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy_head = ListNode()  # Dummy head to simplify list creation
        current = dummy_head

        while l1 or l2 or carry:
            # Get values from the current nodes or 0 if one list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(val=total % 10)

            # Move to the next node
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next