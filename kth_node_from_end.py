'''
Given the head of a linked list and an integer k, return the kth node from the end.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2, return the node with value 4, as it is the 2nd node from the end.
'''

from typing import Optional

from linked_list_nodes import SinglyListNode


def find_kth_node_from_end(head: SinglyListNode, k: int) -> Optional[SinglyListNode]:
    if k < 1:
        return None
    
    left = head
    right = head    
    for _ in range(k):
        if right:
            right = right.next
        else:
            return None

    while right:
        left = left.next
        right = right.next
    return left