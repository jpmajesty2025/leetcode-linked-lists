import pytest
from hypothesis import given, strategies as st

from link_list_cycle import has_cycle
from linked_list_nodes import SinglyListNode


def build_linked_list(values, cycle_pos=-1):
    if not values:
        return None

    nodes = [SinglyListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]

    return nodes[0]


def oracle_has_cycle(head):
    seen = set()
    node = head
    while node is not None:
        node_id = id(node)
        if node_id in seen:
            return True
        seen.add(node_id)
        node = node.next
    return False


@pytest.mark.parametrize(
    ("values", "cycle_pos", "expected"),
    [
        ([], -1, False),
        ([1], -1, False),
        ([1], 0, True),
        ([1, 2], -1, False),
        ([1, 2], 0, True),
        ([3, 2, 0, -4], 1, True),
    ],
)
def test_has_cycle_examples_and_edge_cases(values, cycle_pos, expected):
    head = build_linked_list(values, cycle_pos)
    assert has_cycle(head) is expected


@given(
    values=st.lists(st.integers(min_value=-10**5, max_value=10**5), max_size=60),
    cycle_seed=st.integers(min_value=-1, max_value=60),
)
def test_has_cycle_matches_oracle(values, cycle_seed):
    cycle_pos = cycle_seed if 0 <= cycle_seed < len(values) else -1
    head = build_linked_list(values, cycle_pos)
    assert has_cycle(head) == oracle_has_cycle(head)