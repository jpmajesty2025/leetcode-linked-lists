# Swapping Nodes in Pairs: A Careful Pointer Exercise

Swapping adjacent nodes in a linked list is a great example of an algorithm that looks simple until you trace every pointer change.

Given a list like:

```text
1 → 2 → 3 → 4 → 5
```

we want:

```text
2 → 1 → 4 → 3 → 5
```

The key constraint is that we swap the **nodes themselves**, not their values. That means each pair requires a careful sequence:

1. Save the node after the current pair so the remainder of the list is not lost.
2. Point the second node back to the first.
3. Point the first node to the saved remainder.
4. Connect the previous swapped pair to the new pair.
5. Continue with the next two nodes.

For a pair `A → B → C`, the local transformation is:

```text
A → B → C
B → A → C
```

There are a few details that make this problem interesting:

- The returned head is the second node of the first pair.
- An odd final node has no partner, so it remains in place.
- Every original node must remain in the result.
- Node values must not be modified.

The iterative solution processes each node once and uses only a constant number of pointers:

- **O(n) time**
- **O(1) extra space**

This problem is a useful reminder that linked-list algorithms are often won or lost in the order of pointer assignments. Before changing a link, save anything that would otherwise become unreachable.

Small steps, precise pointers, correct result.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering #CodingJourney