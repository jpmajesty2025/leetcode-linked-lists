'''
Swap the values of the kth nodes from the beginning and end of a linked list.

Positions are 1-indexed. The list links and node identities remain unchanged;
only the two selected node values are exchanged. The algorithm runs in O(n)
time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if k < 1:
        raise ValueError("k must be at least 1")
    if head is None:
        raise ValueError("k cannot exceed the list length")

    front_node = head
    for _ in range(k - 1):
        if front_node.next is None:
            raise ValueError("k cannot exceed the list length")
        front_node = front_node.next

    back_node = head
    scan = front_node
    while scan.next is not None:
        scan = scan.next
        back_node = back_node.next

    front_node.val, back_node.val = back_node.val, front_node.val
    return head
