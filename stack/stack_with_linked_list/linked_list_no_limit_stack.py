from stack import messages as m


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'<Value: {self.value}, Next: {self.next.value if self.next else self.next}>'


class LinkedListNoLimitStack:
    def __init__(self):
        self.head = None

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
            node_status = 'HEAD' if node is self.head else ''

            result += m.NODE_REPR_MSG.format(node_status=node_status, node=node)

        if not result:
            return m.STACK_EMPTY_MSG

        return result

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

        return self

    def pop(self):
        if self.is_empty():
            return m.STACK_EMPTY_MSG

        result = self.head
        self.head = self.head.next

        return result

    def peek(self):
        if self.is_empty():
            return m.STACK_EMPTY_MSG
        return self.head

    def is_empty(self):
        return self.head is None

    def delete(self):
        self.head = None
        return self


llnls = LinkedListNoLimitStack()
print(llnls.push(1))
print(llnls.push(2))

print(llnls.peek())

print(llnls.pop())
print(llnls)
print(llnls.is_empty())
print(llnls.pop())
print(llnls)
print(llnls.is_empty())
print(llnls.push(1))
print(llnls.delete())


