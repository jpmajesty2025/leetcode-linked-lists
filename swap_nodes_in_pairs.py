'''
Given a linked list, swap every two adjacent nodes and return the new head.
Node values must remain unchanged; only next pointers may be modified.

For each pair of nodes A -> B, the algorithm:
1. Saves the node after the pair so the remainder of the list is not lost.
2. Links B to A, reversing the pair.
3. Links the previous pair to B, when a previous pair exists.
4. Links A to the saved remainder and continues with the next pair.

If the list has an odd number of nodes, the final unpaired node remains in
its original position. The algorithm runs in O(n) time and uses O(1) extra
space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = head.next
    previous = None
    current = head

    while current and current.next:
        first = current
        second = current.next
        remainder = second.next

        second.next = first
        first.next = remainder

        if previous:
            previous.next = second

        previous = first
        current = remainder

    return new_head
