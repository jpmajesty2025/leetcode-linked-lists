'''
reverse a single linked list
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev