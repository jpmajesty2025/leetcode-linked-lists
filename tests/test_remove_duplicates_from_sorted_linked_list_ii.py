import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from remove_duplicates_from_sorted_linked_list_ii import delete_duplicates


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


def distinct_values(values):
    return [
        value
        for index, value in enumerate(values)
        if (index == 0 or value != values[index - 1])
        and (index == len(values) - 1 or value != values[index + 1])
    ]


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [2, 3]),
        ([1, 2, 2, 3, 3, 4], [1, 4]),
        ([1, 2, 3, 3, 3], [1, 2]),
        ([1, 1, 1], []),
        ([-2, -2, 0, 1, 1, 3], [0, 3]),
    ],
)
def test_delete_duplicates_examples(values, expected):
    head, _ = build_linked_list(values)

    result = delete_duplicates(head)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


@given(
    st.lists(st.integers(min_value=-100, max_value=100), max_size=100).map(sorted)
)
def test_delete_duplicates_matches_oracle_and_preserves_unique_nodes(values):
    head, original_nodes = build_linked_list(values)

    result = delete_duplicates(head)

    expected_values = distinct_values(values)
    actual_values, result_nodes = values_and_nodes(result)
    expected_nodes = [
        node
        for index, node in enumerate(original_nodes)
        if (index == 0 or values[index] != values[index - 1])
        and (index == len(values) - 1 or values[index] != values[index + 1])
    ]

    assert actual_values == expected_values
    assert result_nodes == expected_nodes
    assert [node.val for node in result_nodes] == actual_values
