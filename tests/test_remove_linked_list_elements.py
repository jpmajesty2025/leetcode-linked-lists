import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from remove_linked_list_elements import remove_elements


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


@pytest.mark.parametrize(
    ("values", "target", "expected"),
    [
        ([], 1, []),
        ([1], 1, []),
        ([1], 2, [1]),
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([7, 1, 2], 7, [1, 2]),
        ([1, 2, 7], 7, [1, 2]),
        ([1, 7, 2], 7, [1, 2]),
        ([7, 7, 1, 7, 7], 7, [1]),
        ([7, 7], 7, []),
        ([-1, 0, -1, 2, 0], 0, [-1, -1, 2]),
    ],
)
def test_remove_elements(values, target, expected):
    head, original_nodes = build_linked_list(values)

    result = remove_elements(head, target)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    expected_nodes = [
        node for node in original_nodes if node.val != target
    ]

    assert actual_values == expected
    assert result_nodes == expected_nodes
    assert following is None


@given(
    values=st.lists(st.integers(), max_size=100),
    target=st.integers(),
)
def test_remove_elements_matches_oracle_and_preserves_retained_nodes(values, target):
    head, original_nodes = build_linked_list(values)

    result = remove_elements(head, target)

    actual_values, result_nodes, following = values_and_nodes(result, len(values))
    expected_values = [value for value in values if value != target]
    expected_nodes = [
        node for node in original_nodes if node.val != target
    ]

    assert actual_values == expected_values
    assert result_nodes == expected_nodes
    assert following is None
