from linked_lists.messages import NODE_REPR_MSG, LIST_EMPTY_MSG, CREATE_LIST_FIRST_MSG, INDEX_ERROR_MSG


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return (f'<Value: {self.value}, '
                f'Previous: {self.prev.value if self.prev is not None else self.prev}, '
                f'Next: {self.next.value if self.next is not None else self.next}>')


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

            if current_node is self.head:
                break

    def __len__(self):
        counter = 0

        for _ in self:
            counter += 1

        return counter

    def __repr__(self):
        result = ''

        for node in self:
            if node != self.head and node != self.tail:
                node_status = ''
            else:
                node_status = 'HEAD' if node == self.head else 'TAIL'

            result += NODE_REPR_MSG.format(node_status=node_status, node=node)

        if self.head and self.tail and self.head is self.tail:
            result += NODE_REPR_MSG.format(node_status='TAIL', node=self.tail)

        if not result:
            return LIST_EMPTY_MSG

        return result

    @classmethod
    def create_cdll(cls, value):
        csdll = CircularDoubleLinkedList()
        init_node = Node(value)
        csdll.head = csdll.head.prev = csdll.head.next = csdll.tail = csdll.tail.prev = csdll.tail.next = init_node

        return csdll

    def insert_node(self, value, index):
        insert_node = Node(value)
        list_length = len(self)

        if not self.head:
            return CREATE_LIST_FIRST_MSG.format(method_name='create_cdll', list_type='cdll')

        if index > list_length:
            return INDEX_ERROR_MSG.format(length=list_length)

        if index == 0 or index == 1:
            insert_node.prev = self.tail
            insert_node.next = self.head
            self.head.prev = self.tail.next = self.head = insert_node
        elif index == -1 or index == list_length:
            insert_node.prev = self.tail
            insert_node.next = self.head
            self.tail.next = self.tail = self.head.prev = insert_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            insert_node.prev = current_node
            insert_node.next = current_node.next
            current_node.next.prev = current_node.next = insert_node

        return self

    def delete_node(self, index):
        list_length = len(self)

        if not self.head:
            return CREATE_LIST_FIRST_MSG.format(method_name='create_cdll', list_type='cdll')

        if index > list_length:
            return INDEX_ERROR_MSG.format(length=list_length)

        if list_length == 1:
            self.head = self.tail = None
        elif index == 0 or index == 1:
            self.head.next.prev = self.tail
            self.tail.next = self.head = self.head.next  # first self.tail.next = self.head.next, then self.head = self.head.next
        elif index == -1:
            self.tail.prev.next = self.head
            self.head.prev = self.tail = self.tail.prev
        else:
            current_node = self.head
            for _ in range(index - 2):
                current_node = current_node.next

            node_to_delete = current_node.next
            current_node.next = node_to_delete.next
            node_to_delete.next.prev = current_node

        return self

    def delete_cdll(self):
        for node in self:
            node.prev = None

        self.head = self.tail = None

        return self

    def reverse_traversal(self):
        current_node = self.tail

        while current_node:
            yield current_node
            current_node = current_node.prev

            if current_node is self.tail:
                break


cdll1 = CircularDoubleLinkedList.create_cdll(1)
print(cdll1)

# cdll1 = CircularDoubleLinkedList()
# print(cdll1)

print(cdll1.insert_node(0, 0))
print(cdll1.insert_node(-1, 1))

print(cdll1.insert_node(2, -1))
print(cdll1.insert_node(3, 4))

print(cdll1.insert_node(10, 2))
print(cdll1.insert_node(20, 5))

# for n in cdll1.reverse_traversal():
#     print(n, end=' -> ')

print(cdll1.delete_node(4))

print(cdll1.delete_cdll())