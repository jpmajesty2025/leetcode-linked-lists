'''
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). 
The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

Example 1:
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]

Example 2:
Input: head = [1,1,0,6]
Output: [1,0,1,6]

Example 3:
Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
'''
from typing import Optional

from linked_list_nodes import SinglyListNode as ListNode


def reverse_even_length_groups(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(0)
    sentinel.next = head
    previous_group_tail = sentinel
    current = head
    intended_group_length = 1

    while current is not None:
        group_tail = current
        actual_group_length = 1
        while (
            actual_group_length < intended_group_length
            and group_tail.next is not None
        ):
            group_tail = group_tail.next
            actual_group_length += 1

        following_group = group_tail.next

        if actual_group_length % 2 == 0:
            previous = following_group
            node = current
            for _ in range(actual_group_length):
                next_node = node.next
                node.next = previous
                previous = node
                node = next_node

            previous_group_tail.next = previous
            previous_group_tail = current
        else:
            previous_group_tail = group_tail

        current = following_group
        intended_group_length += 1

    return sentinel.next

n1 = ListNode(5)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4

head= n1
result = reverse_even_length_groups(head)
while result:
    print(result.val, end=" -> ")
    result = result.next