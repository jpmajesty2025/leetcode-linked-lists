# Removing Duplicates from an Unsorted Linked List

When a linked list is sorted, duplicate values are adjacent and easy to remove. But when the list is unsorted, equal values may be far apart:

```text
1 → 3 → 2 → 3 → 1 → 4
```

The goal is to keep the first occurrence of each value:

```text
1 → 3 → 2 → 4
```

A neighboring-node comparison is no longer enough, so the solution uses:

1. A `seen` set for values already retained.
2. A `previous` pointer to the last node kept.
3. A `current` pointer to scan the list.

For each node:

- If its value is new, add it to `seen` and advance both pointers.
- If its value has already been seen, bypass the node with `previous.next = current.next`.
- Do not advance `previous` after deleting a node. Only advance `current`.

The set identifies duplicates, while the two pointers remove duplicate nodes in place.

Complexity:

- **Expected O(n) time**
- **O(n) extra space** for the set
- **O(1) pointer space**
- Original order is preserved

Without hashing, constant extra space is possible, but repeated searches would make the algorithm O(n²) time complexity. Why? When you encounter a particular number in a node, you need to use another pointer to scan the rest of the list for other instances of that value and remove any found. 

This is a useful example of trading memory for speed: when sorted order is unavailable, a set restores efficient duplicate detection.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Hashing #Pointers #Programming #SoftwareEngineering