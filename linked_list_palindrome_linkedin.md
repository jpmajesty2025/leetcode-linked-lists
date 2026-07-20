# Checking Whether a Linked List Is a Palindrome

A linked-list palindrome reads the same forward and backward:

```text
1 → 2 → 2 → 1
```

The challenge is to solve this without copying the values into an array.

A space-efficient approach uses three stages:

1. **Find the midpoint**  
   Use a slow pointer that moves one node at a time and a fast pointer that moves two nodes at a time. When the fast pointer reaches the end, the slow pointer identifies the start of the second half.

2. **Reverse the second half**  
   Reverse the second half in place. For example:

   ```text
   First half:            1 → 2
   Reversed second half:  1 → 2
   ```

3. **Compare both halves**  
   Walk through the first half and the reversed second half together. Any mismatch means the list is not a palindrome.

There is one important engineering detail: reversing the second half temporarily changes the caller’s linked list. A predicate such as `is_palindrome` should not leave behind that mutation.

That is why the comparison is placed inside a `try/finally` block:

```python
reversed_second_half = reverse(slow)

try:
    # Compare the two halves.
    ...
finally:
    # Restore the original list structure.
    reverse(reversed_second_half)
```

The `finally` block runs whether the comparison succeeds, finds a mismatch and returns `False`, or raises an unexpected exception. This guarantees that the list is restored on every exit path.

The result is:

- **O(n) time**
- **O(1) auxiliary space**
- Original node identities and links preserved

The `try/finally` is more than syntax here—it expresses an important ownership rule: temporary mutations must be undone even when the main operation exits early.

#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Palindromes #Programming #SoftwareEngineering #CodingJourney