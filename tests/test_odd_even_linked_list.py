import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from odd_even_linked_list import odd_even_list


def build_linked_list(values):
    nodes = [SinglyListNode(value) for value in values]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following
    return (nodes[0] if nodes else None), nodes


def values_and_nodes(head, expected_length):
    values = []
    nodes = []
    current = head

    for _ in range(expected_length):
        if current is None:
            break
        values.append(current.val)
        nodes.append(current)
        current = current.next

    return values, nodes, current


def expected_odd_even_order(values):
    return values[::2] + values[1::2]


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        ([-1, 0, -1, 2, 0], [-1, -1, 0, 0, 2]),
    ],
)
def test_odd_even_list(values, expected):
    head, original_nodes = build_linked_list(values)

    result = odd_even_list(head)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    expected_nodes = original_nodes[::2] + original_nodes[1::2]

    assert actual_values == expected
    assert result_nodes == expected_nodes
    assert following is None


@given(st.lists(st.integers(), max_size=100))
def test_odd_even_list_matches_oracle_and_preserves_node_order(values):
    head, original_nodes = build_linked_list(values)

    result = odd_even_list(head)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    expected_nodes = original_nodes[::2] + original_nodes[1::2]

    assert actual_values == expected_odd_even_order(values)
    assert result_nodes == expected_nodes
    assert following is None
