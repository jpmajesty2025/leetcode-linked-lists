# Reversing a Sublist: A Linked-List Pointer Exercise

The problem: given a singly linked list and two 1-indexed positions, `left` and `right`, reverse only the nodes between those positions.

For example:

```text
Input:  1 → 2 → 3 → 4 → 5
Range:  left = 2, right = 4

Output: 1 → 4 → 3 → 2 → 5
```

One possible approach, if you have a `reverse(head)` function, is to locate the sublist within the main list, detach it, reverse it, then reattach it. This works but is overly complicated.

Instead, we can reverse the selected range in place, shifting one node at a time, while keeping the rest of the list connected.

A clean solution uses a temporary sentinel node and the **head-insertion** technique:

1. Place a sentinel before the original head. This makes reversing a range beginning at position 1 follow the same logic as any other range.
2. Move a pointer to the node immediately before the reversal range.
3. Keep a pointer to the first node in the range because it becomes the range’s tail after reversal.
4. Repeatedly detach the node after the range tail.
5. Insert that node immediately after the node before the range.
6. Continue until all nodes in the selected range have moved into reverse order.
7. Return the sentinel’s next node as the new head.

In the prior example, for the range `2 → 3 → 4`, `1` is the node right before the reversal range and `2` will become the tail of the reversed range. So the head-insertion steps look like this:

```text
1 → 2 → 3 → 4 → 5

Move 3 aftter 1:
1 → 3 → 2 → 4 → 5

Move 4 after 1:
1 → 4 → 3 → 2 → 5
```

```python
def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    if head is None or left == right:
        return head

    sentinel = ListNode(0)
    sentinel.next = head
    before_range = sentinel
    for _ in range(left - 1):
        before_range = before_range.next

    range_tail = before_range.next
    for _ in range(right - left):
        node = range_tail.next
        range_tail.next = node.next
        node.next = before_range.next
        before_range.next = node

    return sentinel.next
```


The algorithm uses:

- **O(n) time** — the list is traversed a bounded number of times
- **O(1) extra space** — only a few pointers and one temporary sentinel are needed

This problem is a good reminder that a carefully chosen invariant can simplify edge cases. By keeping the range’s tail fixed and inserting each following node at the front, the reversal becomes a sequence of small, predictable pointer updates.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Pointers #Programming #SoftwareEngineering