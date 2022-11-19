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

            result += NODE_REPR_MSG.format(node_status=node_status, node_value=[node.value, node.prev, node.next])

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

    def delete_node(self, index):
        list_length = len(self)

        if index > list_length:
            return INDEX_ERROR_MSG.format(length=list_length)

        if not self.head:
            return CREATE_LIST_FIRST_MSG.format(method_name='create_dll', list_type='dll')

        if list_length == 1:
            self.head = self.tail = None
        elif index == 0 or index == 1:
            self.head = self.head.next
            self.head.prev = None
        elif index == -1 or index == list_length:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            curr_node = self.head
            for i in range(index - 2):
                curr_node = curr_node.next

            node_to_delete = curr_node.next
            curr_node.next = node_to_delete.next
            node_to_delete.next.prev = curr_node

        return self

    def delete_dll(self):
        for n in self:
            n.prev = None
            # if set head and tail to None - other nodes won't be deleted, because each node references the previous
            # one, so we need to set prev attr to None first, then after setting head to None each Node will be removed
            # one after another from the memory as no object will be referencing it

        self.head = self.tail = None

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

# dll1.reverse_traversal()

print(dll1.delete_node(7))
print(dll1.delete_node(-1))

print(dll1.delete_dll())