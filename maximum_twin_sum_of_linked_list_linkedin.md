# Maximum Twin Sum: Tying Useful Techniques Together

Problem statement: In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1. The twin sum is defined as the sum of a node and its twin. Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example:
```text
1 → 4 → 2 → 3

Twin sums: (1 + 3) and (4 + 2)
Maximum: 6
```

A straightforward approach is to copy the values into an array and use indexes. That works, but it requires O(n) extra space.

A more efficient linked-list solution is:

1. Use slow and fast pointers to find the start of the second half.
2. Reverse the second half in place.
3. Walk through the first half and the reversed second half together.
4. Track the largest twin sum.
5. Reverse the second half again to restore the original list.

```text
First half:             1 → 4
Reversed second half:   3 → 2

Twin comparisons:       1 + 3, 4 + 2
```

```python
def pair_sum(head: Optional[ListNode]) -> int:
    if head is None or head.next is None:
        raise ValueError("pair_sum requires an even-length list with at least two nodes")

    slow = head
    fast = head
    first_half_tail = None

    while fast and fast.next:
        first_half_tail = slow
        slow = slow.next
        fast = fast.next.next

    first_half_tail.next = None
    reversed_second_half = reverse(slow)

    left = head
    right = reversed_second_half
    maximum = None
    while right:
        twin_sum = left.val + right.val
        maximum = twin_sum if maximum is None else max(maximum, twin_sum)
        left = left.next
        right = right.next

    restored_second_half = reverse(reversed_second_half)
    first_half_tail.next = restored_second_half
    return maximum
```

Because the second half is reversed again before returning, the caller receives the original list structure unharmed. We get:

- **O(n) time** — each node is visited a constant number of times
- **O(1) extra space** — only a few pointers are used
- **Original list preserved** — the temporary reversal is undone

This problem was interesting because the slick elegant solution came from stringing together a couple of basic techniques you might not think tp combine.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering