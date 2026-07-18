'''
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode
from reverse_linked_list import reverse

def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right or not head.next:
        return head
    
    cnt = 1
    left_portion_tail = None
    middle_portion_new_tail = head
    while cnt < left:
        left_portion_tail = middle_portion_new_tail
        middle_portion_new_tail = middle_portion_new_tail.next
        cnt += 1
    
    middle_portion_old_tail = middle_portion_new_tail
    while cnt < right:
        middle_portion_old_tail = middle_portion_old_tail.next
        cnt += 1
    head_rest_of_list = middle_portion_old_tail.next
    middle_portion_old_tail.next = None

    reversed_middle = reverse(middle_portion_new_tail)
    if left_portion_tail:
        left_portion_tail.next = reversed_middle
    else:
        head = reversed_middle
    middle_portion_new_tail.next = head_rest_of_list
    return head