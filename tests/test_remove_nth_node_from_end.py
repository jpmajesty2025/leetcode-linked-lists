import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from remove_nth_node_from_end_of_linked_list import remove_nth_from_end


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
    ("values", "n", "expected"),
    [
        ([1], 1, []),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([-1, 0, -1, 2], 3, [-1, -1, 2]),
    ],
)
def test_remove_nth_from_end_examples(values, n, expected):
    head, _ = build_linked_list(values)

    result = remove_nth_from_end(head, n)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


@pytest.mark.parametrize("n", [0, -1, -10])
def test_remove_nth_from_end_rejects_non_positive_n(n):
    head, _ = build_linked_list([1, 2, 3])

    with pytest.raises(ValueError, match="at least 1"):
        remove_nth_from_end(head, n)


@pytest.mark.parametrize(
    ("values", "n"),
    [([], 1), ([1, 2, 3], 4), ([1, 2, 3], 10)],
)
def test_remove_nth_from_end_rejects_n_larger_than_list(values, n):
    head, _ = build_linked_list(values)

    with pytest.raises(ValueError, match="cannot exceed"):
        remove_nth_from_end(head, n)


@given(
    values=st.lists(st.integers(), max_size=100),
    n=st.integers(min_value=0, max_value=105),
)
def test_remove_nth_from_end_matches_oracle_and_preserves_nodes(values, n):
    head, original_nodes = build_linked_list(values)

    if n < 1 or n > len(values):
        with pytest.raises(ValueError):
            remove_nth_from_end(head, n)
        return

    result = remove_nth_from_end(head, n)

    expected_values = values[:]
    del expected_values[-n]
    actual_values, result_nodes = values_and_nodes(result)
    expected_nodes = original_nodes[:]
    del expected_nodes[-n]

    assert actual_values == expected_values
    assert result_nodes == expected_nodes
    assert sorted(id(node) for node in result_nodes) == sorted(
        id(node) for node in original_nodes if node in expected_nodes
    )
