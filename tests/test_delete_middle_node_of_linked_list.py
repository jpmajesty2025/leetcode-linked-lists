import pytest
from hypothesis import given, strategies as st

from delete_middle_node_of_linked_list import deleteMiddle
from linked_list_nodes import SinglyListNode


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
        ([1], []),
        ([1, 2], [1]),
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([1, 2, 3, 4, 5], [1, 2, 4, 5]),
        ([-2, 0, -2, 3], [-2, 0, 3]),
    ],
)
def test_delete_middle_examples(values, expected):
    head, _ = build_linked_list(values)

    result = deleteMiddle(head)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


def test_delete_middle_preserves_surviving_node_identity():
    head, original_nodes = build_linked_list([1, 2, 3, 4, 5])

    result = deleteMiddle(head)

    _, result_nodes = values_and_nodes(result)
    expected_nodes = original_nodes[:]
    del expected_nodes[len(original_nodes) // 2]
    assert result_nodes == expected_nodes


@given(st.lists(st.integers(), max_size=100))
def test_delete_middle_matches_oracle_and_preserves_values(values):
    head, original_nodes = build_linked_list(values)

    result = deleteMiddle(head)

    expected_values = values[:]
    if expected_values:
        del expected_values[len(expected_values) // 2]

    actual_values, result_nodes = values_and_nodes(result)
    expected_nodes = original_nodes[:]
    if expected_nodes:
        del expected_nodes[len(expected_nodes) // 2]

    assert actual_values == expected_values
    assert result_nodes == expected_nodes
    assert [node.val for node in result_nodes] == actual_values
