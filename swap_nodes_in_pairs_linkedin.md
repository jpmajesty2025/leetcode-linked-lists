# Swapping Nodes in Pairs: A Careful Pointer Exercise

### Problem: Given a linked list, swap every two adjacent nodes and return the new head. Node values must remain unchanged; only next pointers may be modified.


Example:

```text
1 → 2 → 3 → 4 → 5
```

Goal:

```text
2 → 1 → 4 → 3 → 5
```

Return head → 2.

Simple enough. Easy to visualize. But beware of the pointers! Each pair swap requires a careful sequence:

1. Save the node after the current pair to retain the rest of the list.
2. Point the second node back to the first.
3. Point the first node to the saved remainder.
4. Properly connect the previous swapped pair - the left end of the list really - to the new pair.
5. Continue with the next two nodes.

For a pair `A → B → C`, the local transformation is:

```text
A → B → C
B → A → C
```

We know nothing about C: could be `None` or a node, with possibly more nodes after.

```python
def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = head.next
    previous = None
    current = head

    while current and current.next:
        first = current
        second = current.next
        remainder = second.next

        second.next = first
        first.next = remainder

        if previous:
            previous.next = second

        previous = first
        current = remainder

    return new_head
```

Some interesting details:

- The returned head is the second node of the first pair. Capture with `new_head`. 
- An odd final node has no partner, so it remains in place. 
- The assignment `first.next = remainder` points the tail of the current pair to what might be the final node in the list or might be the first node in another pair to be swapped in the next iteration.
 - The loop condition `if current and current.next` determines this.
- Notice that `previous` is only set if we get through at least one iteration, i.e. if there is a pair to swap. 
- Second iteration -> there is another pair to swap. And `previous` is set from the last iteration, so `previous.next = second` executes.
- This is where the tail of the prior pair gets hooked to the head of the newly swapped pair, i.e. the tail of pair before the swap. 
- It initially was pointed at the head of the next pair before the swap.
- Thus `previous.next = second` overrides `first.next = remainder` in all iterations after the first.
- This is a subtlety of the pointer management needed for this algorithm.

Each node processed once, using a constant number of pointers:

- **O(n) time**
- **O(1) extra space**

Linked-list algorithms are often won or lost in the order of pointer assignments. Before changing a link, save anything that would otherwise become unreachable.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering #Pointers