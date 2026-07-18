'''
Delete the middle node from a singly linked list in place.

For a list of length n, the middle is the node at zero-based index n // 2.
For even-length lists this selects the second of the two central nodes.

A slow pointer advances one node at a time while a fast pointer advances two.
When fast reaches the end, slow is at the middle and previous points to the
node before it. The algorithm runs in O(n) time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    previous = None

    while fast and fast.next:
        previous = slow
        slow = slow.next
        fast = fast.next.next

    previous.next = slow.next
    return head
