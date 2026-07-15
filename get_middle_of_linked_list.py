'''
Given the head of a singly linked list, return the middle node of the linked list. Note this code works for both odd and even length linked lists. 

If there are two middle nodes, return the second middle node.
'''
def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow