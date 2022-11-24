from linked_lists.messages import NODE_REPR_MSG
from queues import messages as m


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'<Value: {self.value}, Next: {self.next.value if self.next else self.next}>'


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        result = ''

        for node in self:
            if node != self.head and node != self.tail:
                node_status = ''
            else:
                node_status = 'HEAD' if node == self.head else 'TAIL'

            result += NODE_REPR_MSG.format(node_status=node_status, node=node)

        if self.head and self.tail and self.head == self.tail:
            result += NODE_REPR_MSG.format(node_status='TAIL', node=self.tail)

        if not result:
            return m.QUEUE_EMPTY_MSG

        return result

    def enqueue(self, value):
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
            return self

        self.tail.next = self.tail = node

        return self

    def dequeue(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        result = self.head

        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return result

    def peek(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        return self.head

    def is_empty(self):
        return self.head is None

    def delete(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        self.head = self.tail = None

        return self


llq = LinkedListQueue()
print(llq.enqueue(1))

print(llq.enqueue(2))
print(llq.enqueue(3))

print(llq.dequeue())
print(llq)

print(llq.peek())
print(llq.is_empty())

print(llq.dequeue())
print(llq.dequeue())
print(llq)

print(llq.enqueue(2))
print(llq.enqueue(1))
print(llq.enqueue(3))
print(llq)

print(llq.delete())