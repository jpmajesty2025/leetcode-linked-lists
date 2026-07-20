'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
'''
from typing import Optional
from linked_list_nodes import SinglyListNode as ListNode

def is_palindrome( head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l2 = l.copy()
        l2.reverse()
        for idx, val in enumerate(l):
            if l2[idx] != val:
                return False
        return True