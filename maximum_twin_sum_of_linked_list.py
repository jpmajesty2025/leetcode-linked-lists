'''
Find the maximum twin sum in an even-length singly linked list.

Twin nodes are paired from opposite ends of the list. For example, the
pairs in 1 -> 2 -> 3 -> 4 are (1, 4) and (2, 3).

The algorithm finds the start of the second half with slow and fast pointers,
reverses that half in place, and compares it with the first half. The second
half is reversed again before returning so the caller's list is preserved.
It runs in O(n) time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode
from reverse_linked_list import reverse


def pair_sum(head: Optional[ListNode]) -> int:
    if head is None or head.next is None:
        raise ValueError("pair_sum requires an even-length list with at least two nodes")

    slow = head
    fast = head
    first_half_tail = None

    while fast and fast.next:
        first_half_tail = slow
        slow = slow.next
        fast = fast.next.next

    first_half_tail.next = None
    reversed_second_half = reverse(slow)

    left = head
    right = reversed_second_half
    maximum = None
    while right:
        twin_sum = left.val + right.val
        maximum = twin_sum if maximum is None else max(maximum, twin_sum)
        left = left.next
        right = right.next

    restored_second_half = reverse(reversed_second_half)
    first_half_tail.next = restored_second_half
    return maximum
