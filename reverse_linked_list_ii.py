'''
Reverse a 1-indexed range of nodes in a singly linked list in place.

The head-insertion technique moves each node after ``left`` to the front of
the active range. A temporary sentinel makes ranges beginning at the head
follow the same pointer logic as ranges in the middle of the list.

The algorithm runs in O(n) time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    if head is None or left == right:
        return head

    sentinel = ListNode(0)
    sentinel.next = head
    before_range = sentinel
    for _ in range(left - 1):
        before_range = before_range.next

    range_tail = before_range.next
    for _ in range(right - left):
        node = range_tail.next
        range_tail.next = node.next
        node.next = before_range.next
        before_range.next = node

    return sentinel.next