from queues import messages as m


class CircularLimitListQueue:
    def __init__(self, limit):
        self.items = [None] * limit  # creates a list of None with length = limit, which avoids memory allocation
        self.start = -1
        self.top = -1
        self.limit = limit

    def __repr__(self):
        return f'Queue with capacity {self.limit} start: {self.start}, top: {self.top}, items: {self.items}'

    def enqueue(self, value):
        if self.is_full():
            return m.QUEUE_FULL_MSG

        if self.start == -1:
            self.start = 0

        if self.top == self.limit - 1:
            self.top = 0
        else:
            self.top += 1

        self.items[self.top] = value

        return self

    def dequeue(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        result = self.items[self.start]
        self.items[self.start] = None

        if self.start == self.top:
            self.start = self.top = -1
        elif self.start == self.limit - 1:
            self.start = 0
        else:
            self.start += 1

        return result

    def peek(self):
        return self.items[self.start]

    def is_empty(self):
        return self.start == -1

    def is_full(self):
        return (self.start - self.top == 1) or (self.start == 0 and self.top == self.limit - 1)

    def delete(self):
        self.start = self.top = -1
        self.items = [None] * self.limit
        return self


cllq = CircularLimitListQueue(3)
cllq.enqueue(1)
cllq.enqueue(2)
cllq.enqueue(3)
print(cllq.items)
print(cllq.is_full())
print(cllq.enqueue(3))
print(cllq)

print(cllq.dequeue())
print(cllq)
print(cllq.peek())
print(cllq.dequeue())
print(cllq)
cllq.enqueue(1)
print(cllq)
print(cllq.dequeue())
print(cllq)
print(cllq.dequeue())
print(cllq)
cllq.enqueue(1)
cllq.enqueue(1)
print(cllq)
print(cllq.delete())