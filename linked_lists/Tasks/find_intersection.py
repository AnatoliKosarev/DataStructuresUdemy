from linked_lists.Tasks.linked_list import Node
from linked_lists.Tasks.linked_list import LinkedList


def find_intersection(ll1, ll2):
    if ll1.tail is not ll2.tail:
        return 'Lists do not intersect'

    len1 = len(ll1)
    len2 = len(ll2)

    longer_ll = ll1 if len1 > len2 else ll2
    shorter_ll = ll2 if len1 > len2 else ll1
    len_diff = abs(len1 - len2)

    longer_node = longer_ll.head
    shorter_node = shorter_ll.head
    for _ in range(len_diff):
        longer_node = longer_node.next

    while longer_node is not shorter_node:
        longer_node = longer_node.next
        shorter_node = shorter_node.next

    return longer_node


def add_intersection_node(ll1, ll2, value):
    intersection_node = Node(value)
    intersection_node.next = None
    ll1.tail.next = ll1.tail = ll2.tail.next = ll2.tail = intersection_node


ll_a = LinkedList()
print(ll_a.generate(5, 0, 99))

ll_b = LinkedList()
print(ll_b.generate(8, 0, 99))

add_intersection_node(ll_a, ll_b, 7)
print(ll_a)
print(ll_b)

print(find_intersection(ll_a, ll_b))
