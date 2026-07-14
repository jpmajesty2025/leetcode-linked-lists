# Linked List Cycle Detection

The classic **Linked List Cycle** problem:

> Given the head of a (singly) linked list, determine whether the list contains a cycle.

A cycle means that while traversing `next` pointers, you eventually revisit a node instead of reaching the end of the list.

One option: use a `set` to track visited nodes

```python
def has_cycle_with_set(head):
    seen = set()
    curr = head
    while curr is not None:
        node_id = id(curr)          # in CPython id() returns the memory address of the object
        if node_id in seen:
            return True
        seen.add(node_id)
        curr = curr.next
    return False
```

It works and it is easy to reason about...but it costs **O(n)** extra space. We can do better!

The more elegant approach is **Floyd’s Cycle Detection Algorithm** (a.k.a. the *Tortoise and Hare*), which solves it in:

- **Time:** `O(n)`
- **Space:** `O(1)`

## Floyd Cycle Detection - the main idea:

Use two pointers:

- `slow` moves 1 step at a time
- `fast` moves 2 steps at a time
- Start them at the head of the list
- If there is a cycle, `fast` will catch up to `slow`. Why? 
    - Eventually both pointers enter the loop.
    - If they do not point to the same node, then `fast` is 'behind' `slow` and gaining on it. With each pointer increment, the gap between `fast` and `slow` shrinks by 1.
    - Example: suppose the cycle contains five nodes and `fast` is one node past `slow`. It is also four nodes behind. In four steps, `fast` catches up to `slow`.

- Note: if there is no cycle, `fast` (or `fast.next`) becomes `None` in a finite number of steps.
    - Specifically, if the length of the linked list is:
        - odd (2k+1 for some k) -> `fast` lands on the last node in k steps and `fast.next` is None.
        - even (2k for some k) -> `fast` lands on the next-to-last node at step k-1 and at the k-th step it jumps off the end of the list. Then `fast` is None.

## Python sketch of Floyd algorithm

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False
```

This was a fun problem: 
- simple statement 
- an easy but suboptimal solution (using hashing!) 
- the elegant surprise and deep algorithmic insight of Floyd's algorithm.

A bit of folklore: None other than Donald Knuth attributed the algorithm to Robert W. Floyd, in 1969, in The Art of Computer Programming, vol. II: Seminumerical Algorithms. However, no such algorithm appears in any of Floyd's published work. Nonetheless, the attribution remains to this day.

#LearningInPublic #Python #Algorithms #DataStructures #LeetCode #LinkedList #FloydCycleDetection #SoftwareEngineering