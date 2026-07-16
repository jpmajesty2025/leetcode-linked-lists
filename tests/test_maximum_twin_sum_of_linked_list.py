import pytest
from hypothesis import given, strategies as st

from linked_list_nodes import SinglyListNode
from maximum_twin_sum_of_linked_list import pair_sum


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
        ([1, 4], 5),
        ([1, 2, 3, 4], 5),
        ([5, 4, 3, 2, 1, 0], 5),
        ([7, 7, 7, 7], 14),
        ([-10, 2, 3, -4], 5),
    ],
)
def test_pair_sum_examples(values, expected):
    head, _ = build_linked_list(values)

    assert pair_sum(head) == expected


def test_pair_sum_rejects_lists_without_a_pair():
    with pytest.raises(ValueError):
        pair_sum(None)

    head, _ = build_linked_list([1])
    with pytest.raises(ValueError):
        pair_sum(head)


@given(
    st.lists(
        st.integers(min_value=-10**5, max_value=10**5),
        min_size=2,
        max_size=100,
    ).filter(lambda values: len(values) % 2 == 0)
)
def test_pair_sum_matches_array_oracle_and_restores_list(values):
    head, original_nodes = build_linked_list(values)
    original_values, _ = values_and_nodes(head)

    actual = pair_sum(head)

    expected = max(
        values[index] + values[-1 - index]
        for index in range(len(values) // 2)
    )
    restored_values, restored_nodes = values_and_nodes(head)

    assert actual == expected
    assert restored_values == original_values
    assert restored_nodes == original_nodes
