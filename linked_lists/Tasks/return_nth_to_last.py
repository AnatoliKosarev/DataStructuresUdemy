from linked_lists.Tasks.linked_list import LinkedList


def return_nth_to_last(linked_list, n):
    list_length = len(linked_list)

    if n > list_length or n <= 0:
        return 'Incorrect index'

    current_node = linked_list.head
    for _ in range(list_length - n):
        current_node = current_node.next

    return current_node

# def return_nth_to_last(linked_list, n):
#     pointer1 = linked_list.head
#     pointer2 = linked_list.head
#
#     for _ in range(n):
#         if pointer2 is None:
#             return None
#         pointer2 = pointer2.next
#
#     while pointer2:
#         pointer1 = pointer1.next
#         pointer2 = pointer2.next
#
#     return pointer1

# def return_nth_to_last(linked_list, n, pointer=None):
#     pointer = pointer if pointer else linked_list.head
#
#     if len(linked_list) - n == 0:
#         return pointer
#
#     pointer = pointer.next
#     n += 1
#     return return_nth_to_last(linked_list, n, pointer)


ll = LinkedList()
print(ll.generate(5, 0, 99))
print(return_nth_to_last(ll, 3))