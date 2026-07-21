import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from reverse_nodes_in_even_length_groups import reverse_even_length_groups


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


def expected_groups(values):
    expected = []
    group_length = 1
    index = 0

    while index < len(values):
        group = values[index : index + group_length]
        if len(group) % 2 == 0:
            group = group[::-1]
        expected.extend(group)
        index += group_length
        group_length += 1

    return expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([5, 2, 6, 3, 9, 1, 7, 3, 8, 4], [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]),
        ([1, 1, 0, 6], [1, 0, 1, 6]),
        ([1, 1, 0, 6, 5], [1, 0, 1, 5, 6]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 3, 2, 4, 5, 6, 7, 8, 9]),
        ([-1, 0, -1, 2, 2], [-1, -1, 0, 2, 2]),
    ],
)
def test_reverse_even_length_groups(values, expected):
    head, original_nodes = build_linked_list(values)

    result = reverse_even_length_groups(head)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    assert actual_values == expected
    assert following is None
    assert sorted(id(node) for node in result_nodes) == sorted(
        id(node) for node in original_nodes
    )


def test_reverse_even_length_groups_handles_none():
    assert reverse_even_length_groups(None) is None


@given(st.lists(st.integers(), max_size=100))
def test_reverse_even_length_groups_matches_oracle_and_preserves_nodes(values):
    head, original_nodes = build_linked_list(values)

    result = reverse_even_length_groups(head)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    assert actual_values == expected_groups(values)
    assert following is None
    assert sorted(id(node) for node in result_nodes) == sorted(
        id(node) for node in original_nodes
    )
