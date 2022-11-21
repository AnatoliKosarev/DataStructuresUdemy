from linked_lists.Tasks.linked_list import LinkedList


def remove_duplicates(linked_list):
    if len(linked_list) <= 1:
        return linked_list

    current_node = linked_list.head
    visited_values = {current_node.value}

    while current_node.next:
        if current_node.next.value in visited_values:
            if current_node.next is not linked_list.tail:
                current_node.next.next.prev = current_node
            else:
                linked_list.tail = current_node

            current_node.next = current_node.next.next
        else:
            visited_values.add(current_node.next.value)
            current_node = current_node.next

    return linked_list


# def remove_duplicates(linked_list):
#     if len(linked_list) <= 1:
#         return linked_list
#
#     for query_duplicate in linked_list:
#         current_node = query_duplicate.next
#         while current_node:
#             if query_duplicate.value == current_node.value:
#                 if current_node is not linked_list.tail:
#                     current_node.next.prev = current_node.prev
#                 else:
#                     linked_list.tail = current_node.prev
#
#                 current_node.prev.next = current_node.next
#
#             current_node = current_node.next
#
#     return linked_list


ll = LinkedList()
print(ll.generate(5, 0, 3))
print(remove_duplicates(ll))