'''
Check whether a singly linked list is a palindrome.

The second half is temporarily reversed for O(n) time and O(1) auxiliary
space, then restored before the function returns.
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode
from reverse_linked_list import reverse


def is_palindrome(head: Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse(slow)
    try:
        left = head
        right = reversed_second_half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    finally:
        reverse(reversed_second_half)
