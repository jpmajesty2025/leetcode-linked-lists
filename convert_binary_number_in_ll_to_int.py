'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def get_decimal_value(head: Optional[ListNode]) -> int:
    value = 0
    current = head

    while current:
        value = (value << 1) | current.val
        current = current.next

    return value