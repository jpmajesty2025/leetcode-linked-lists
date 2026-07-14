from linked_list_nodes import SinglyListNode as ListNode


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
one.next = two
two.next = three
head = one

print(head.val)
print(head.next.val)
print(head.next.next.val)

def get_sum(head):
    ans = 0
    while head:
        ans += head.val
        head = head.next
    
    return ans

def get_sum(head):
    if not head:
        return 0
    
    return head.val + get_sum(head.next)

# Let prev_node be the node at position i - 1
def add_node(prev_node, node_to_add):
    node_to_add.next = prev_node.next
    prev_node.next = node_to_add

def delete_node(prev_node):
    prev_node.next = prev_node.next.next