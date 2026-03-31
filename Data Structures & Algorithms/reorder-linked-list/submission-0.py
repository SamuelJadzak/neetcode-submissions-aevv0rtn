class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None 
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        l1, l2 = head, prev
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

            tail.next = l2
            l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        
            