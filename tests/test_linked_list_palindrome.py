from linked_list_nodes import SinglyListNode
from linked_list_palindrome import is_palindrome


def test_empty_list_is_palindrome():
    assert is_palindrome(None) is True


def test_palindrome_and_restoration():
    nodes = [SinglyListNode(value) for value in [1, 2, 2, 1]]
    for first, second in zip(nodes, nodes[1:]):
        first.next = second

    assert is_palindrome(nodes[0]) is True
    assert [nodes[0].val, nodes[0].next.val, nodes[0].next.next.val, nodes[0].next.next.next.val] == [1, 2, 2, 1]
