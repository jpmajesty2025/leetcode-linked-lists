---
name: linked-lists
description: Provide linked-list algorithm patterns, invariants, refactoring guidance, and testing practices.
author: Project
version: 1.0.0
---

# Linked Lists

Use this skill for singly or doubly linked-list algorithms involving reversal, deletion, pairwise operations, midpoint and twin calculations, duplicate removal, cycles, or positional queries.

## Invariants

- Save a successor before overwriting a next pointer.
- Track a predecessor when removing or reconnecting nodes.
- Verify termination at None and verify the intended node set and ordering.
- Make index conventions explicit.
- State which middle is selected for even-length lists.
- Treat cyclic-list handling as a separate contract.

## Patterns

- Use a sentinel before head when an operation may replace the head; return sentinel.next.
- Use slow and fast pointers for midpoint, splitting, and cycle detection.
- For reversal, maintain prev, current, and next_node; save next_node before mutation.
- For range reversal, keep the range tail fixed and repeatedly insert the following node at the range front.
- For sorted duplicate removal, either bypass repeated nodes or skip a complete duplicate run.
- For positional operations, maintain a fixed pointer gap and validate positions when required.

## Testing

Test None and singleton inputs where allowed, two-node cases, head, tail, middle, prefix, suffix, whole-list, odd/even lengths, duplicate, negative, and zero values. Use an independent oracle. Check node identity and ordering when nodes move, next-link preservation when only values change, restoration after temporary mutation, termination, and absence of cycles.

Prefer O(n) time and O(1) auxiliary space for in-place linked-list transformations.
