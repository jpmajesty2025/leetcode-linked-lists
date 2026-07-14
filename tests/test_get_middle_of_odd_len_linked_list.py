import pytest
from hypothesis import given, strategies as st

from get_middle_of_odd_len_linked_list_v1 import get_middle as get_middle_v1
from get_middle_of_odd_len_linked_list_v2 import get_middle as get_middle_v2
from linked_list_nodes import SinglyListNode


def build_linked_list(values):
    if not values:
        return None

    nodes = [SinglyListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


@pytest.mark.parametrize(
    "values",
    [
        [1],
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [-5, -3, -1, 0, 2, 4, 7],
    ],
)
def test_get_middle_examples_and_edge_cases(values):
    expected = values[len(values) // 2]
    head = build_linked_list(values)

    assert get_middle_v1(head) == expected

    head = build_linked_list(values)
    assert get_middle_v2(head) == expected


@given(
    values=st.lists(
        st.integers(min_value=-10**5, max_value=10**5),
        min_size=1,
        max_size=101,
    ).filter(lambda xs: len(xs) % 2 == 1)
)
def test_get_middle_v1_v2_match_oracle_on_odd_lengths(values):
    expected = values[len(values) // 2]

    head_v1 = build_linked_list(values)
    head_v2 = build_linked_list(values)

    assert get_middle_v1(head_v1) == expected
    assert get_middle_v2(head_v2) == expected
    assert get_middle_v1(build_linked_list(values)) == get_middle_v2(build_linked_list(values))


def test_get_middle_empty_list_current_behavior():
    with pytest.raises(AttributeError):
        get_middle_v1(None)

    with pytest.raises(AttributeError):
        get_middle_v2(None)