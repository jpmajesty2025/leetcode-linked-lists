import pytest
from hypothesis import given, strategies as st

from convert_binary_number_in_ll_to_int import get_decimal_value
from linked_list_nodes import SinglyListNode


def build_linked_list(bits):
    nodes = [SinglyListNode(bit) for bit in bits]
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


def expected_decimal_value(bits):
    return int("".join(map(str, bits)), 2) if bits else 0


@pytest.mark.parametrize(
    ("bits", "expected"),
    [
        ([], 0),
        ([0], 0),
        ([1], 1),
        ([1, 0, 1], 5),
        ([1, 0, 0, 1], 9),
        ([0, 0, 1, 0, 1], 5),
        ([0, 0, 0, 0], 0),
        ([1, 1, 1, 1], 15),
        ([1, 0, 1, 0, 1, 0, 1, 0], 170),
    ],
)
def test_get_decimal_value(bits, expected):
    head, original_nodes = build_linked_list(bits)

    result = get_decimal_value(head)

    actual_values, result_nodes, following = values_and_nodes(head, len(bits))
    assert result == expected
    assert actual_values == bits
    assert result_nodes == original_nodes
    assert following is None


@given(st.lists(st.integers(min_value=0, max_value=1), max_size=100))
def test_get_decimal_value_matches_oracle_without_mutating_list(bits):
    head, original_nodes = build_linked_list(bits)

    result = get_decimal_value(head)

    actual_values, result_nodes, following = values_and_nodes(head, len(bits))
    assert result == expected_decimal_value(bits)
    assert actual_values == bits
    assert result_nodes == original_nodes
    assert following is None
