from collections import Counter

import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from remove_duplicates_from_unsorted_linked_list_ii import delete_duplicates


def build(values):
    nodes = [SinglyListNode(value) for value in values]
    for first, second in zip(nodes, nodes[1:]):
        first.next = second
    return (nodes[0] if nodes else None), nodes


def read(head):
    values = []
    nodes = []
    while head:
        values.append(head.val)
        nodes.append(head)
        head = head.next
    return values, nodes


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 1, 3, 2], [3]),
        ([1, 1, 1], []),
        ([-1, 0, -1, 2, 0], [2]),
    ],
)
def test_examples(values, expected):
    head, _ = build(values)
    result = delete_duplicates(head)
    actual, _ = read(result)
    assert actual == expected


@given(st.lists(st.integers(), max_size=100))
def test_oracle_and_node_identity(values):
    head, original_nodes = build(values)
    result = delete_duplicates(head)

    frequencies = Counter(values)
    expected_values = [value for value in values if frequencies[value] == 1]
    expected_nodes = [
        node
        for value, node in zip(values, original_nodes)
        if frequencies[value] == 1
    ]

    actual_values, result_nodes = read(result)
    assert actual_values == expected_values
    assert result_nodes == expected_nodes
