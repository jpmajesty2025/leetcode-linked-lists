import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from reverse_linked_list_ii import reverse_between


def build_linked_list(values):
    nodes = [SinglyListNode(value) for value in values]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    return (nodes[0] if nodes else None), nodes


def values_and_nodes(head):
    values = []
    nodes = []
    current = head
    while current is not None:
        values.append(current.val)
        nodes.append(current)
        current = current.next
    return values, nodes


def expected_reversal(values, left, right):
    expected = values[:]
    expected[left - 1 : right] = reversed(expected[left - 1 : right])
    return expected


@pytest.mark.parametrize(
    ("values", "left", "right", "expected"),
    [
        ([], 1, 1, []),
        ([1], 1, 1, [1]),
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 1, 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 3, 5, [1, 2, 5, 4, 3]),
        ([1, 2, 3, 4], 1, 4, [4, 3, 2, 1]),
        ([-1, 2, 2, -1], 2, 3, [-1, 2, 2, -1]),
    ],
)
def test_reverse_between_examples(values, left, right, expected):
    head, _ = build_linked_list(values)

    result = reverse_between(head, left, right)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


def test_reverse_between_handles_none():
    assert reverse_between(None, 1, 1) is None


@given(
    values=st.lists(st.integers(), min_size=1, max_size=100),
    bounds=st.tuples(st.integers(min_value=1, max_value=100), st.integers(min_value=1, max_value=100)),
)
def test_reverse_between_matches_array_oracle_and_preserves_nodes(values, bounds):
    left, right = sorted(bounds)
    if right > len(values):
        return

    head, original_nodes = build_linked_list(values)
    original_values = values[:]

    result = reverse_between(head, left, right)

    actual_values, result_nodes = values_and_nodes(result)
    assert actual_values == expected_reversal(original_values, left, right)
    assert sorted(id(node) for node in result_nodes) == sorted(
        id(node) for node in original_nodes
    )
    assert [node.val for node in result_nodes] == actual_values
