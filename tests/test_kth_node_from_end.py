import pytest
from hypothesis import given, strategies as st

from kth_node_from_end import find_kth_node_from_end
from linked_list_nodes import SinglyListNode


def build_linked_list(values):
    if not values:
        return None

    nodes = [SinglyListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


@pytest.mark.parametrize(
    ("values", "k", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, 4),
        ([1, 2, 3, 4, 5], 1, 5),
        ([1, 2, 3, 4, 5], 5, 1),
        ([9], 1, 9),
        ([], 1, None),
        ([1, 2, 3], 4, None),
        ([1, 2, 3], 0, None),
        ([1, 2, 3], -1, None),
    ],
)
def test_find_kth_node_from_end_examples_and_edges(values, k, expected):
    head = build_linked_list(values)
    node = find_kth_node_from_end(head, k)
    actual = None if node is None else node.val
    assert actual == expected


@given(
    values=st.lists(
        st.integers(min_value=-10**5, max_value=10**5),
        min_size=1,
        max_size=120,
    ),
    k=st.integers(min_value=1, max_value=120),
)
def test_find_kth_node_from_end_matches_oracle(values, k):
    head = build_linked_list(values)
    node = find_kth_node_from_end(head, k)

    expected = values[-k] if k <= len(values) else None
    actual = None if node is None else node.val
    assert actual == expected