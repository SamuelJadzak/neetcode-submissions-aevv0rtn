/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        if (head === null){
            return null
        }
        let l = null
        let m = head
        let r = head.next
        while (m !== null){
            m.next = l
            l = m
            m = r
            if (r) r = r.next
        }
        return l
    }
}
