import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from swapping_kth_nodes_in_linked_list import swap_nodes


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


def expected_values(values, k):
    expected = values[:]
    expected[k - 1], expected[-k] = expected[-k], expected[k - 1]
    return expected


@pytest.mark.parametrize(
    ("values", "k", "expected"),
    [
        ([7], 1, [7]),
        ([1, 2, 3, 4, 5], 1, [5, 2, 3, 4, 1]),
        ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4], 4, [4, 2, 3, 1]),
        ([-2, 0, -2, 3], 2, [-2, -2, 0, 3]),
    ],
)
def test_swap_nodes_examples(values, k, expected):
    head, _ = build_linked_list(values)

    result = swap_nodes(head, k)

    actual_values, _ = values_and_nodes(result)
    assert actual_values == expected


@pytest.mark.parametrize("k", [0, -1, -10])
def test_swap_nodes_rejects_non_positive_k(k):
    head, _ = build_linked_list([1, 2, 3])

    with pytest.raises(ValueError, match="at least 1"):
        swap_nodes(head, k)


@pytest.mark.parametrize("values, k", [(None, 1), ([], 1), ([1, 2, 3], 4)])
def test_swap_nodes_rejects_k_larger_than_list(values, k):
    head, _ = build_linked_list(values or [])

    with pytest.raises(ValueError, match="cannot exceed"):
        swap_nodes(head, k)


@given(
    values=st.lists(st.integers(), min_size=1, max_size=100),
    k=st.integers(min_value=1, max_value=100),
)
def test_swap_nodes_matches_oracle_and_preserves_links(values, k):
    head, original_nodes = build_linked_list(values)

    if k > len(values):
        with pytest.raises(ValueError):
            swap_nodes(head, k)
        return

    original_next = {id(node): node.next for node in original_nodes}
    result = swap_nodes(head, k)

    actual_values, result_nodes = values_and_nodes(result)
    assert actual_values == expected_values(values, k)
    assert result_nodes == original_nodes
    assert all(node.next is original_next[id(node)] for node in result_nodes)
