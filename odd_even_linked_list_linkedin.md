# A Slick Linked-List Pattern: Leap-Frogging Odd and Even Pointers

Some linked-list problems look like they need extra lists, arrays, or complicated bookkeeping.

But the “group odd-indexed nodes first, then even-indexed nodes” problem has a wonderfully compact in-place solution.

Given:

```text
1 → 2 → 3 → 4 → 5
```

we want:

```text
1 → 3 → 5 → 2 → 4
```

The key is to run two pointer chains at the same time:

```python
odd = head
even = head.next
even_head = even
```

- `odd` tracks the tail of the odd-positioned chain.
- `even` tracks the tail of the even-positioned chain.
- `even_head` remembers where the even chain begins, so we can append it later.

Then the pointers leap-frog through the list:

```python
while even and even.next:
    odd.next = even.next
    odd = odd.next

    even.next = odd.next
    even = even.next

odd.next = even_head
```

## What is happening?

Start here:

```text
1 → 2 → 3 → 4 → 5
↑   ↑
odd even
```

### First pass

Link the next odd node after the odd chain:

```text
1 → 3
```

Then link the next even node after the even chain:

```text
2 → 4
```

The two chains are now:

```text
Odd:  1 → 3
Even: 2 → 4
```

### Second pass

The odd pointer claims node `5`:

```text
Odd:  1 → 3 → 5
Even: 2 → 4
```

There is no next even node to claim, so the loop ends.

Finally, attach the even chain after the odd chain:

```text
1 → 3 → 5 → 2 → 4
```

## The loop invariant

After each iteration:

- the odd chain contains processed odd-indexed nodes in their original order;
- the even chain contains processed even-indexed nodes in their original order;
- `odd` and `even` point to the tails of those chains;
- `even_head` still points to the first even node.

That invariant makes the final connection simple:

```python
odd.next = even_head
```

## Why this is a great pattern

- **O(n) time:** each node is visited a constant number of times.
- **O(1) extra space:** no new lists or arrays.
- **Stable order:** odd nodes retain their original order, as do even nodes.
- **In place:** it rewires existing `next` pointers without replacing nodes.

The broader lesson: when a linked-list problem asks you to partition nodes while preserving order, consider maintaining separate chains with their own tail pointers—then concatenate them once traversal is complete.

#LinkedList #Algorithms #DataStructures #Python #LeetCode #SoftwareEngineering #ProblemSolving #CodingInterview #ComputerScience #CleanCode