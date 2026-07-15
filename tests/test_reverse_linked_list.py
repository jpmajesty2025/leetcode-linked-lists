import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from reverse_linked_list import reverse


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


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
    ],
)
def test_reverse_examples(values, expected):
    head, _ = build_linked_list(values)

    result = reverse(head)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


def test_reverse_preserves_node_identity():
    head, original_nodes = build_linked_list([1, 2, 3])

    result = reverse(head)

    _, reversed_nodes = values_and_nodes(result)
    assert reversed_nodes == original_nodes[::-1]


@given(st.lists(st.integers(), max_size=100))
def test_reverse_matches_reversed_values_and_preserves_nodes(values):
    head, original_nodes = build_linked_list(values)

    result = reverse(head)

    actual_values, reversed_nodes = values_and_nodes(result)
    assert actual_values == list(reversed(values))
    assert reversed_nodes == original_nodes[::-1]


@given(st.lists(st.integers(), max_size=100))
def test_reversing_twice_restores_original_list(values):
    head, original_nodes = build_linked_list(values)

    restored = reverse(reverse(head))

    actual_values, restored_nodes = values_and_nodes(restored)
    assert actual_values == values
    assert restored_nodes == original_nodes
