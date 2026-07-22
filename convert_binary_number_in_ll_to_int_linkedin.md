# Converting a Binary Linked List to an Integer—Without Reversing It

A linked list such as:

```text
1 → 0 → 1 → 1
```

represents the binary number:

```text
1011₂
```

The goal is to return its decimal value:

```text
1011₂ = 11₁₀
```

A tempting approach is to reverse the linked list, start at the least significant bit, and accumulate powers of two.

That can work—but reversing a list is an unnecessary side effect for a read-only conversion problem.

A cleaner solution processes the bits from left to right:

```python
value = 0
current = head

while current:
    value = (value << 1) | current.val
    current = current.next

return value
```

## The key idea

Every time we read another binary digit:

1. Shift the current value left by one bit.
2. Add the incoming bit.

In arithmetic form:

```text
value = value × 2 + bit
```

In bitwise form:

```text
value = (value << 1) | bit
```

Because every node is guaranteed to contain either `0` or `1`, bitwise OR safely appends the new bit.

## Step-by-step trace

For:

```text
1 → 0 → 1 → 1
```

| Current bit | Previous value | Calculation | New value |
|---|---:|---|---:|
| 1 | 0 | `(0 << 1) \| 1` | 1 |
| 0 | 1 | `(1 << 1) \| 0` | 2 |
| 1 | 2 | `(2 << 1) \| 1` | 5 |
| 1 | 5 | `(5 << 1) \| 1` | 11 |

The final result is `11`.

## Why this approach is better

- **O(n) time:** each node is visited once.
- **O(1) extra space:** only `value` and `current` are needed.
- **No mutation:** the original node order and links remain unchanged.
- **Simple invariant:** after processing a node, `value` equals the decimal value of every bit seen so far.

This is a useful pattern beyond linked lists: whenever digits arrive from most significant to least significant, update the running number with:

```text
running_value = running_value × base + next_digit
```

For binary, the base is `2`.

#LinkedList #Algorithms #DataStructures #Python #LeetCode #BitManipulation #SoftwareEngineering #ProblemSolving #CodingInterview #ComputerScience