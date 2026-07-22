'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
and return the new head.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    current = head
    sentinel = ListNode(0)
    sentinel.next = head
    previous = sentinel

    while current:
        if current.val == val:
            previous.next = current.next
        else:
            previous = current
        current = current.next

    return sentinel.next