'''
Remove the nth node from the end of a singly linked list.

A sentinel node and two pointers maintain a gap of n nodes between ``right``
and ``left``. When ``right`` reaches the end, ``left`` points to the node
before the target, so the target can be removed in place.

The algorithm runs in O(n) time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def remove_nth_from_end(
    head: Optional[ListNode], n: int
) -> Optional[ListNode]:
    if n < 1:
        raise ValueError("n must be at least 1")

    sentinel = ListNode(0)
    sentinel.next = head
    right = sentinel

    for _ in range(n):
        if right.next is None:
            raise ValueError("n cannot exceed the list length")
        right = right.next

    left = sentinel
    while right.next is not None:
        right = right.next
        left = left.next

    left.next = left.next.next
    return sentinel.next
