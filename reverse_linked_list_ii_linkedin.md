# Reversing a Sublist: A Linked-List Pointer Exercise

Today’s problem: given a singly linked list and two 1-indexed positions, `left` and `right`, reverse only the nodes between those positions.

For example:

```text
Input:  1 → 2 → 3 → 4 → 5
Range:  left = 2, right = 4

Output: 1 → 4 → 3 → 2 → 5
```

The challenge is to reverse the selected range in place while keeping the rest of the list connected.

A clean solution uses a temporary sentinel node and the **head-insertion** technique:

1. Place a sentinel before the original head. This makes reversing a range beginning at position 1 follow the same logic as any other range.
2. Move a pointer to the node immediately before the reversal range.
3. Keep a pointer to the first node in the range. This node becomes the range’s tail after reversal.
4. Repeatedly remove the node after the range tail.
5. Insert that node immediately after the node before the range.
6. Continue until all nodes in the selected range have moved into reverse order.
7. Return the sentinel’s next node as the new head.

For the range `2 → 3 → 4`, the head-insertion steps look like this:

```text
1 → 2 → 3 → 4 → 5

Move 3 before 2:
1 → 3 → 2 → 4 → 5

Move 4 before 3:
1 → 4 → 3 → 2 → 5
```

The original nodes are rearranged; their values are not changed. The sentinel is only a temporary helper and is not returned as part of the list.

The algorithm uses:

- **O(n) time** — the list is traversed a bounded number of times
- **O(1) extra space** — only a few pointers and one temporary sentinel are needed

This problem is a good reminder that a carefully chosen invariant can simplify edge cases. By keeping the range’s tail fixed and inserting each following node at the front, the reversal becomes a sequence of small, predictable pointer updates.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering #CodingJourney