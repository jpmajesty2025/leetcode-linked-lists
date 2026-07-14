# Linked List Cycle Detection (LeetCode 141) — #LearningInPublic

Today I worked on the classic **Linked List Cycle** problem:

> Given the head of a linked list, determine whether the list contains a cycle.

A cycle means that while traversing `next` pointers, you eventually revisit a node instead of reaching `None`.

## Why this problem is interesting

At first glance, you might use a `set` to track visited nodes.  
That works — but it costs **O(n)** extra space.

The more elegant approach is **Floyd’s Cycle Detection Algorithm** (a.k.a. the *Tortoise and Hare*), which solves it in:

- **Time:** `O(n)`
- **Space:** `O(1)`

## Floyd Cycle Detection in one idea

Use two pointers:

- `slow` moves 1 step at a time
- `fast` moves 2 steps at a time

If there is a cycle, `fast` will eventually “lap” `slow`, so they meet.  
If there is no cycle, `fast` (or `fast.next`) becomes `None`.

## Python sketch

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

## What I focused on today

- Refactored toward the canonical Floyd implementation
- Centralized linked-list node definitions into a shared module
- Added deterministic + property-based tests with `pytest` + `hypothesis`
- Added a cycle “oracle” checker for stronger validation

Really enjoyed this one — simple problem statement, deep algorithmic insight.

#LearningInPublic #Python #Algorithms #DataStructures #LeetCode #LinkedList #FloydCycleDetection #SoftwareEngineering #Pytest #Hypothesis #TDD