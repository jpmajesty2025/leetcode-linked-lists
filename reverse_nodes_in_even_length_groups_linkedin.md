# Why This In-Place Linked-List Reversal Looks Different (But Isn’t)

When working through **Reverse Nodes in Even Length Groups**, I initially found the reversal loop less intuitive than the version used in a typical “reverse a sub-list” problem.

Both are in-place reversals. They simply use different pointer-rewiring patterns.

Here is the core loop:

```python
previous = following_group
node = current

for _ in range(actual_group_length):
    next_node = node.next
    node.next = previous
    previous = node
    node = next_node
```

The crucial invariant is:

- `previous` is the portion of the group that has already been reversed.
- `node` is the next node still waiting to be processed.
- `next_node` saves the original successor before `node.next` is overwritten.

The clever detail is this initialization:

```python
previous = following_group
```

Instead of starting with `previous = None`, we start with the first node after the current group.

Suppose we need to reverse the group `2 -> 3` in this list:

```text
1 -> 2 -> 3 -> 4
```

`following_group` is node `4`.

### Step 1

```text
previous = 4
node = 2
```

Save node `3`, then point `2` to `4`:

```text
2 -> 4
```

Now:

```text
previous = 2
node = 3
```

### Step 2

Save node `4`, then point `3` to `2`:

```text
3 -> 2 -> 4
```

Now `previous` is the new head of the reversed group.

Finally, reconnect the preceding group:

```python
previous_group_tail.next = previous
```

So the list becomes:

```text
1 -> 3 -> 2 -> 4
```

Why seed `previous` with the node after the group?

Because it reconnects the new tail automatically. The original first node in the group becomes the reversed group’s tail, and its `next` pointer is set to `following_group` during the first iteration.

This is different from another common in-place approach: repeatedly taking the next node in a range and inserting it at the range front. That technique is also correct, but it has a different mental model.

The important takeaway: there is no single “the” in-place linked-list reversal algorithm.

Different pointer patterns can all be correct if they preserve the same fundamentals:

1. Save the successor before overwriting `next`.
2. Keep a pointer to the already-processed portion.
3. Reconnect the reversed range to its predecessor and successor.
4. Verify that the list still terminates and includes every original node exactly once.

Once you identify the loop invariant, pointer-heavy linked-list code becomes much easier to reason about.

#LinkedList #Algorithms #DataStructures #Python #LeetCode #SoftwareEngineering #ProblemSolving #CodingInterview #ComputerScience #CleanCode