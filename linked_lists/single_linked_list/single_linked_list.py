class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        result = ''

        while node:
            if node != self.head and node != self.tail:
                node_state = ''
            else:
                node_state = 'HEAD' if node == self.head else 'TAIL'

            result += f'Node {node_state}: {node.value}\n'
            node = node.next

        if self.head and self.tail and self.head == self.tail:
            result += f'Node TAIL: {self.tail.value}\n'

        if not result:
            result = 'List is empty'

        return result

    def __len__(self):
        counter = 0

        for _ in self:
            counter += 1

        return counter

    def delete_node_by_index(self, index):
        if index > len(self):
            return 'Index is incorrect'

        if index == 0 or index == 1:
            if self.head == self.tail:
                self.tail = self.head = None
                return self

            self.head = self.head.next
            return self

        temp_node = self.head
        for i in range(index - 2):  # traverse to the previous node to the one we have to delete
            temp_node = temp_node.next

        node_to_delete = temp_node.next
        temp_node.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = temp_node

        return self

    def delete_linked_list(self):
        self.head = self.tail = None
        return self

    def list_contains_node(self, value):
        for node in self:
            if node.value == value:
                return True

        return False

    def insert_node_by_index(self, value, index):
        new_node = Node(value)

        if index and index > len(self) - 1:
            return 'Index specified is incorrect ! It\'s larger than list length !'

        if self.head is None:
            self.head = new_node
            self.tail = new_node

            return self

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            return self

        if index == -1:
            self.tail.next = new_node
            self.tail = new_node

            return self

        temp_node = self.head
        for i in range(index - 1):
            temp_node = temp_node.next

        new_node.next = temp_node.next
        temp_node.next = new_node

        if self.tail == temp_node:
            self.tail = new_node

        return self

    def insert_node_by_node_value(self, value, value_to_insert_after=None, first=None, last=None):
        if not value_to_insert_after and not first and not last:
            return 'One of the arguments: value_to_insert_after, first, last has to be not empty'
        if first and last:
            return 'First and last arguments cannot be passed simultaneously'

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

            return self

        if first:
            new_node.next = self.head
            self.head = new_node

        if last:
            self.tail.next = new_node
            self.tail = new_node

            return self

        for node in self:
            if node.value == value_to_insert_after:
                new_node.next = node.next
                node.next = new_node

                if new_node.next is None:
                    self.tail = new_node

                return self

        return 'No such value_to_insert_after exists'


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


# single_linked_list1 = SingleLinkedList()
# node1 = Node(1)
# node2 = Node(2)
#
# print('Creating single linked list')
# print('===================================================')
#
# single_linked_list1.head = node1
# single_linked_list1.head.next = node2
# single_linked_list1.tail = node2
# print(single_linked_list1)
#
# print('Inserting head node into single linked list')
# print('===================================================')
#
# node_new_head = Node(3)
# node_new_head.next = single_linked_list1.head
# single_linked_list1.head = node_new_head
# print(single_linked_list1)
#
# print('Inserting tail node into single linked list')
# print('===================================================')
#
# node_new_tail = Node(4)
# single_linked_list1.tail.next = node_new_tail
# single_linked_list1.tail = node_new_tail
# print(single_linked_list1)
#
# print('Inserting middle node into single linked list')
# print('===================================================')
# new_middle_node = Node(5)
# for node in single_linked_list1:
#     if node.value == 2:
#         new_middle_node.next = node.next
#         node.next = new_middle_node
#
# print(single_linked_list1)
#
# print(single_linked_list1.insert_node_by_node_value(0, first=True))
# print(single_linked_list1.insert_node_by_node_value(7, last=True))
# print(single_linked_list1.insert_node_by_node_value(8, 7))
# print(single_linked_list1.insert_node_by_node_value(10, value_to_insert_after=2))
# print(single_linked_list1.insert_node_by_node_value(11, value_to_insert_after=11))


new_single_linked_list = SingleLinkedList()
print(new_single_linked_list.insert_node_by_index(value=0, index=0))
print(new_single_linked_list.insert_node_by_index(value=1, index=-1))
print(new_single_linked_list.insert_node_by_index(value=2, index=1))
print(new_single_linked_list.insert_node_by_index(value=3, index=0))
print(new_single_linked_list.insert_node_by_index(value=4, index=2))

print(new_single_linked_list.delete_node_by_index(5))

print(new_single_linked_list.delete_linked_list())