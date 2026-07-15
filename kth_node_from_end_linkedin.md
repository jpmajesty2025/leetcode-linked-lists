# More Fun with Linked Lists

Today’s problem: **find the kth node from the end of a singly linked list**.

The naive approach: walk the whole list to find its length, then rewalk to the kth node from the end. It works but it is kind of clunky and somewhat suboptimal. Here is a cleaner two-pointer pattern.

Recall that for the cycle problem, we used "Floyd’s"* cycle detection algorithm (fast + slow with different speeds).  
Here, both pointers move **at the same speed** — but one starts with a **k-node lead**.

## Core idea

1. Start `left` and `right` at `head`.
2. Use a k-iteration for-loop to move `right` forward `k` nodes, into its initial posittion.
    - Note: if `right` marches off the end of the list before the loop exits naturally, the list is too short for the given value of `k`.
    - You need to detect this and exit early, returning None.
3. If you did not exit early, then move both pointers one step at a time.
4. When `right` becomes `None` (steps off the list), `left` is exactly at the **kth node from the end**.

That offset is the whole trick.

## Why this works

By keeping a fixed gap of `k` nodes between pointers, every synchronized move preserves the gap.  
So when the lead pointer runs out of nodes, the lagging pointer must be `k` nodes behind the end.

## Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

## Python sketch

```python
def find_kth_node_from_end(head, k):
    if k < 1:
        return None

    left = head
    right = head

    for _ in range(k):
        if right is None:
            return None
        right = right.next

    while right:
        left = left.next
        right = right.next

    return left
```

*[See my note at the end of that prior post to understand why I used quotes.]

#LearningInPublic #Python #Algorithms #DataStructures #LinkedList #TwoPointers #LeetCode #SoftwareEngineering