from linked_lists.messages import LIST_EMPTY_MSG, CREATE_LIST_FIRST_MSG, INDEX_ERROR_MSG, NODE_REPR_MSG


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        if not self.head:
            return LIST_EMPTY_MSG

        current_node = self.head

        while current_node:
            yield current_node

            current_node = current_node.next

            if current_node is self.head:
                break

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

    def __len__(self):
        counter = 0

        for _ in self:
            counter += 1

        return counter

    @classmethod
    def create_scll(cls, value):
        scll = SinglyCircularLinkedList()
        init_node = Node(value)
        scll.head = scll.tail = init_node
        scll.head.next = scll.tail.next = init_node
        return scll

    def insert_node(self, value, index):
        insert_node = Node(value)

        if index and index > len(self):
            return INDEX_ERROR_MSG.format(length=len(self))

        if not self.head:
            return CREATE_LIST_FIRST_MSG.format(method_name='create_scll', list_type='scll')

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.tail.next = insert_node
            return self

        if index == -1:
            self.tail.next = insert_node
            insert_node.next = self.head
            self.tail = insert_node
            return self

        temp_node = self.head
        for i in range(index - 1):
            temp_node = temp_node.next

        insert_node.next = temp_node.next
        temp_node.next = insert_node

        if temp_node == self.tail:
            self.tail = insert_node

        return self

    def delete_node(self, index):
        list_length = len(self)

        if index > list_length:
            return INDEX_ERROR_MSG.format(length=list_length)

        if list_length == 1:
            self.head = None
            self.tail = None
            return self

        if index == 0 or index == 1:
            self.tail.next = self.head.next
            self.head = self.head.next
            return self

        if index == -1:
            current_node = self.head
            for i in range(list_length - 2):
                current_node = current_node.next

            current_node.next = self.head
            self.tail = current_node
            return self

        current_node = self.head
        for i in range(index - 2):
            current_node = current_node.next  # iterate to the node which goes before the node to delete

        node_to_delete = current_node.next
        current_node.next = node_to_delete.next

        if node_to_delete == self.tail:
            self.tail = current_node

        return self

    def delete_list(self):
        self.head = self.tail = None
        return self


scll1 = SinglyCircularLinkedList.create_scll(0)
print(scll1)
scll1.insert_node(1, 1)
print(scll1)
print(scll1.insert_node(2, -1))
print(scll1.insert_node(3, 3))
print(scll1.insert_node(4, 0))

print(scll1.delete_node(5))
print(scll1.delete_node(-1))

# print(scll1.delete_list())
