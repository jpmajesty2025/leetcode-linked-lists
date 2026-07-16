# Removing Duplicates from a Sorted Linked List: Let the Ordering Do the Work

Removing duplicates from a sorted linked list is actually quite simple. 

Because equal values appear next to one another, we only need one pointer: `current`. 

- We keep it fixed on the first instance of a value
- If the value in the current node is the same as in the next node, then bypass the next node by making `current.next` point to the node after the duplicate.
- Else, if the value in the current node is different from that of the next node, then all duplicates of the value in current node have been removed. So we advance `current` to the next node and continue. 

```python
def delete_duplicates( head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
```

Example: 

```text
1 → 1 → 1 → 2 → 3 → 3 =>
1 → 1 → 2 → 3 → 3 =>
1 → 2 → 3 → 3 =>
1 → 2 → 3
```

The algorithm preserves the first occurrence of every value, keeps the list sorted, and modifies the list in place:

- **O(n) time** — each node is examined at most once
- **O(1) extra space** — no additional list or set is needed

By the way, you may wonder what happens to the bypassed nodes. Suppose you are maintaining a long-run linked list structure. Memory management is a legit concern. Those bypassed nodes are orphaned and unreachable but they are also 'stuck' to the list because they point at a node and we did not modify the pointer of the duplicate node itself. 

These duplicates are removed in the sense that if you walk the new list you will never encounter them. But a useful question is: What happens to the memory allocated for these dead nodes? 

For some languages, like Python and Java, the garbage collection system automatically detects that nothing references them and frees up the memory. 

However, for a language such as C++ you either need to explictly deallocate the dead node to avoid a memory leak or else adhere to modern C++ best practices and use so-called 'smart pointers' to avoid memory management mistakes like leaks and dangling pointers. Here is a C++ snippet 

```cpp
if (curr->val == curr->next->val) {
    ListNode* temp = curr->next;
    curr->next = curr->next->next;
    delete temp; // Properly deallocates the memory
}
```
#LearningInPublic #Algorithms #DataStructures #Python #LinkedLists #Programming #SoftwareEngineering #MemoryManagement #MemoryLeaks #DanglingPointers