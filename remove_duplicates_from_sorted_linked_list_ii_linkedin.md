# Removing All Duplicates from a Sorted Linked List

Today’s problem: given a sorted singly linked list, remove **every node** whose value appears more than once. Only values that occur exactly once should remain.

For example:

```text
Input:  1 → 2 → 3 → 3 → 4 → 4 → 5
Output: 1 → 2 → 5
```

This is different from the simpler duplicate-removal problem, where we keep one copy of each repeated value. Here, an entire duplicate run must be removed.

A clean solution uses a sentinel node and two pointers:

1. Place a sentinel before the original head. This uniformaly handles duplicate runs at the beginning.
2. Keep `previous` at the last node known to be unique.
3. Use `current` to scan the unresolved part of the list.
4. When `current` and `current.next` have the same value, save that value and skip every node in the duplicate run.
5. Connect `previous.next` to the first node after the run.
6. If the current value is unique, advance both pointers.
7. Return `sentinel.next` as the new head.

The key invariant is that `previous` always points to a node that is safe to keep. When a duplicate run is found, we do not keep any node from that run.

Because the input is sorted, equal values are adjacent. That ordering lets us process each node in a single pass without a set or array.

The algorithm:

```python
def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    sentinel = ListNode(0)
    sentinel.next = head
    previous = sentinel
    current = head

    while current:
        if current.next and current.val == current.next.val:
            duplicate_value = current.val
            while current and current.val == duplicate_value:
                current = current.next
            previous.next = current
        else:
            previous = current
            current = current.next

    return sentinel.next
```

- Runs in **O(n) time** — each node is visited at most a constant number of times
- Uses **O(1) extra space** — only a sentinel and a few pointers
- Preserves the original node objects that contain unique values

Sorted input can turn a frequency-tracking problem into a simple local traversal. The sentinel pattern also removes special cases when the head belongs to a duplicate group. 

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering #CodingJourney