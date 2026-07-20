from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    seen = set()
    previous = None
    current = head

    while current:
        if current.val in seen:
            previous.next = current.next
        else:
            seen.add(current.val)
            previous = current
        current = current.next

    return head
