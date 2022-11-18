from linked_lists.messages import LIST_EMPTY_MSG, CREATE_LIST_FIRST_MSG, INDEX_ERROR_MSG, NODE_REPR_MSG


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

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

            result += NODE_REPR_MSG.format(node_status=node_status, node_value=node.value)

        if self.head and self.tail and self.head == self.tail:
            result += NODE_REPR_MSG.format(node_status='TAIL', node_value=self.tail.value)

        if not result:
            return LIST_EMPTY_MSG

        return result

    @classmethod
    def create_dll(cls, value):
        dll = DoubleLinkedList()
        init_node = Node(value)
        dll.head = dll.tail = init_node

        return dll

    def insert_node(self, value, index):
        insert_node = Node(value)
        list_length = len(self)

        if index > list_length:
            return INDEX_ERROR_MSG.format(length=list_length)

        if not self.head:
            return CREATE_LIST_FIRST_MSG.format(method_name='create_dll', list_type='dll')

        if index == 0:
            insert_node.next = self.head
            self.head.prev = insert_node
            self.head = insert_node
            return self

        if index == -1:
            self.tail.next = insert_node
            insert_node.prev = self.tail
            self.tail = insert_node
            return self

        curr_node = self.head
        for i in range(index - 1):
            curr_node = curr_node.next

        if curr_node == self.tail:
            insert_node.prev = curr_node
            curr_node.next = insert_node
            self.tail = insert_node
            return self

        insert_node.prev = curr_node
        insert_node.next = curr_node.next
        curr_node.next.prev = insert_node
        curr_node.next = insert_node

        return self

    def reverse_traversal(self):
        curr_node = self.tail

        while curr_node:
            print(curr_node.value, end=' <- ')

            curr_node = curr_node.prev


print(DoubleLinkedList().insert_node(1, 0))
dll1 = DoubleLinkedList.create_dll(0)
print(dll1)
print(dll1.insert_node(1, 1))
print(dll1.insert_node(3, -1))
print(dll1.insert_node(2, 2))
print(dll1.insert_node(-1, 0))

dll1.reverse_traversal()
