# Removing Duplicates from a Sorted Linked List: Let the Ordering Do the Work

Removing duplicates from a linked list can be deceptively simple when the list is already sorted.

Because equal values appear next to one another, we only need one pointer: `current`.

```python
current = head
while current and current.next:
    if current.val == current.next.val:
        current.next = current.next.next
    else:
        current = current.next
```

When two adjacent nodes contain the same value, we bypass the duplicate by changing one link. When the values differ, we move forward. The important detail is that we do **not** advance `current` after removing a duplicate—the next node might contain the same value too.

For example:

```text
1 → 1 → 1 → 2 → 3 → 3
                ↓
1 → 2 → 3
```

The algorithm preserves the first occurrence of every value, keeps the list sorted, and modifies the list in place:

- **O(n) time** — each node is examined at most once
- **O(1) extra space** — no additional list or set is needed

Pay close attention to input constraints. They are probably useful. The sorted order gives uu valuable information we would otherwise need a hash set to discover.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering