from linked_lists.Tasks.linked_list import LinkedList


def partition(linked_list, partition_value):
    if len(linked_list) <= 1:
        return linked_list

    current_node = linked_list.head.next

    while current_node:
        next_node = current_node.next
        if current_node.value < partition_value:

            if current_node is not linked_list.tail:
                current_node.next.prev = current_node.prev
            else:
                linked_list.tail = current_node.prev

            current_node.prev.next = current_node.next
            current_node.next = linked_list.head
            linked_list.head.prev = current_node
            current_node.prev = None
            linked_list.head = current_node

        current_node = next_node

    return linked_list


ll = LinkedList()
print(ll.generate(5, 0, 10))
ll.add_at_the_end(2)
ll.add_at_the_end(3)
print(ll)
print(partition(ll, 5))