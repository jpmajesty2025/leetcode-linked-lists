# Linked List Reversal: A Small Problem with an Important Pointer Lesson

Reversing a singly linked list is a great example of how a seemingly simple algorithm can depend on preserving just one critical piece of information.

At first glance, two pointers might seem sufficient:

- `prev` — the node behind the current node
- `curr` — the node we are processing

All we need to do is reverse the direction of the `curr` pointer, right? But if we set `curr.next = prev`, we just lost lost our forward pointer and orphaned the rest of the list. There is now nothing pointed at the node that follows `curr`. Bad news! But fear not. We use a temporary pointer to capture the next node first, then we safely divert `curr.next` to point back at `prev`. Here is the canonical algorithm:

```python
def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        next_node = curr.next #temp pointer at next node to avoid losing the rest of the list
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

The final solution reverses the list in place with:

- **O(n) time**, because each node is visited once
- **O(1) extra space**, because no new list is created

This is a useful reminder that pointer algorithms are often less about the number of pointers and more about preserving the information that would otherwise be overwritten.

Small problem, valuable lesson: before mutating a link, make sure you still have a way to reach what comes next.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering