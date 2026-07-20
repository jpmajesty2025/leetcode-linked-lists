'''
Remove every node whose value appears more than once in a sorted linked list.

The ``previous`` pointer always identifies the last node known to be unique.
When a duplicate run is found, all nodes with that value are skipped at once;
otherwise, both pointers advance. A sentinel handles duplicate runs at the
head uniformly.

The algorithm runs in O(n) time and uses O(1) auxiliary space.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(0)
    sentinel.next = head
    previous = sentinel
    current = head

    while current:
        if current.next and current.val == current.next.val:
            duplicate_value = current.val
            while current and current.val == duplicate_value:
                current = current.next
            previous.next = current
        else:
            previous = current
            current = current.next

    return sentinel.next
