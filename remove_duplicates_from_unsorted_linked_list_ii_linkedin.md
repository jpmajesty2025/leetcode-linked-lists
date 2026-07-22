# Removing Every Duplicate from an Unsorted Linked List

This problem is similar to ordinary deduplication, but the requirement is different.

Given:

```text
1 → 3 → 2 → 3 → 1 → 4
```

we must remove **every node** whose value appears more than once:

```text
2 → 4
```

We cannot keep the first occurrence and remove only later ones. We need to know the total frequency of each value before deciding which nodes are safe to keep.

A clean solution uses two passes:

1. **Count frequencies**
   - Traverse the list once.
   - Store each value and its count in a dictionary.

2. **Remove repeated values**
   - Traverse the list again with `previous` and `current` pointers.
   - If `frequencies[current.val] > 1`, bypass the node.
   - Otherwise, advance `previous` because the node is unique.

A sentinel before the head makes deletion uniform, including when the first value is duplicated:

```text
Before:  1 → 3 → 2 → 3 → 1 → 4
Counts:  1:2, 3:2, 2:1, 4:1
After:         2 → 4
```

The two passes are still linear overall:

- **Expected O(n) time**
- **O(n) extra space** for the frequency dictionary
- **O(1) pointer space**
- Original order is preserved for values that occur exactly once

A one-pass solution is possible with more bookkeeping, but when a value appears again, its first occurrence may be far behind. Removing that earlier node requires tracking its predecessor and maintaining additional state.

The two-pass frequency-map approach is easier to reason about, easier to test, and asymptotically optimal when we want expected O(n) time.

This problem highlights an important distinction: recognizing that a value has appeared before is not the same as knowing whether it will appear again.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Hashing #Pointers #Programming #SoftwareEngineering