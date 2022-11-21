from linked_lists.messages import NODE_REPR_MSG, LIST_EMPTY_MSG
from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return (f'<Value: {self.value}, '
                f'Previous: {self.prev.value if self.prev is not None else self.prev}, '
                f'Next: {self.next.value if self.next is not None else self.next}>')


class LinkedList:
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

            result += NODE_REPR_MSG.format(node_status=node_status, node=node)

        if self.head and self.tail and self.head is self.tail:
            result += NODE_REPR_MSG.format(node_status='TAIL', node=self.tail)

        if not result:
            return LIST_EMPTY_MSG

        return result

    def add_at_the_end(self, value):
        list_length = len(self)
        insert_node = Node(value)

        if list_length == 0:
            self.head = self.tail = insert_node
        else:
            insert_node.prev = self.tail
            self.tail.next = self.tail = insert_node

    def generate(self, n,  min_value, max_value):
        self.head = self.tail = None

        for _ in range(n):
            self.add_at_the_end(randint(min_value, max_value))

        return self


if __name__ == '__main__':
    ll = LinkedList()
    print(ll.generate(5, 0, 99))
