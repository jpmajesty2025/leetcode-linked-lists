from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    frequencies = {}
    current = head

    while current:
        frequencies[current.val] = frequencies.get(current.val, 0) + 1
        current = current.next

    sentinel = ListNode(0)
    sentinel.next = head
    previous = sentinel
    current = head

    while current:
        if frequencies[current.val] > 1:
            previous.next = current.next
        else:
            previous = current
        current = current.next

    return sentinel.next
