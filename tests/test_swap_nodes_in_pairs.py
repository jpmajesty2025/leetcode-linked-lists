import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from swap_nodes_in_pairs import swap_pairs


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


def expected_pairwise_values(values):
    expected = values[:]
    for index in range(0, len(expected) - 1, 2):
        expected[index], expected[index + 1] = (
            expected[index + 1],
            expected[index],
        )
    return expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([-2, -2, 0, 1, 1], [-2, -2, 1, 0, 1]),
    ],
)
def test_swap_pairs_examples(values, expected):
    head, _ = build_linked_list(values)

    result = swap_pairs(head)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


@given(st.lists(st.integers(), max_size=100))
def test_swap_pairs_matches_pairwise_oracle_and_preserves_nodes(values):
    head, original_nodes = build_linked_list(values)

    result = swap_pairs(head)

    actual_values, result_nodes = values_and_nodes(result)
    expected_nodes = original_nodes[:]
    for index in range(0, len(expected_nodes) - 1, 2):
        expected_nodes[index], expected_nodes[index + 1] = (
            expected_nodes[index + 1],
            expected_nodes[index],
        )

    assert actual_values == expected_pairwise_values(values)
    assert result_nodes == expected_nodes
    assert sorted(id(node) for node in result_nodes) == sorted(
        id(node) for node in original_nodes
    )


@given(st.lists(st.integers(), max_size=100))
def test_swap_pairs_does_not_mutate_node_values(values):
    head, original_nodes = build_linked_list(values)
    original_values_by_id = {id(node): node.val for node in original_nodes}

    result = swap_pairs(head)

    _, result_nodes = values_and_nodes(result)
    assert all(node.val == original_values_by_id[id(node)] for node in result_nodes)
