# Plan: Refactor + Tests for remove_duplicates_from_sorted_linked_list.py
Date: 2026-07-14
POC: AdaL

## TL;DR
Refactor `delete_duplicates` to a clearer single-pointer implementation (same complexity/behavior), add a dedicated pytest+hypothesis suite, then run full tests.

## Why this change
- Current goal is clarity/maintainability while preserving correctness.
- For sorted-list deduplication, one pointer is sufficient:
  - If `current.val == current.next.val`, bypass duplicate via `current.next = current.next.next`.
  - Else advance `current = current.next`.
- This keeps optimal complexity: `O(n)` time, `O(1)` extra space.

## Proposed code changes

### 1) `remove_duplicates_from_sorted_linked_list.py`
- Replace existing `delete_duplicates` body with canonical single-pointer loop:
  - `while current and current.next`
  - bypass duplicates or advance
  - `return head`
- Keep function name and signature unless a mismatch is found.

### 2) New test file: `tests/test_remove_duplicates_from_sorted_linked_list.py`
Add:
- Helper `build_linked_list(values)` (project-consistent local helper pattern)
- Helper `linked_list_to_list(head)` for assertions
- Parametrized deterministic tests:
  - empty list
  - single element
  - all duplicates
  - mixed duplicate runs
  - negatives/zeros
- Hypothesis property test:
  - generate int lists in constraints (`-100..100`, `max_size=300`)
  - sort before building linked list (problem precondition)
  - oracle compare with `sorted(set(sorted_values))`
  - invariants: output sorted and no adjacent duplicates

## Risks / trade-offs
- Very low regression risk (algorithmic equivalence, simpler control flow).
- Test helper duplication exists across repo; not addressed now to keep blast radius small.

## Validation plan
1. Run `pytest -q` after edits.
2. If failure occurs, inspect only impacted tests and apply surgical fixes.
3. Confirm no unrelated files changed.

## Alternatives considered
- Keep current implementation and add tests only:
  - Rejected: misses readability objective.
- Refactor across all test files into shared helper module:
  - Rejected for now: broader change than requested; higher regression surface.