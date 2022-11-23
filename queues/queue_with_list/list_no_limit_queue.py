from queues import messages as m


class ListNoLimitQueue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)
        return self.list

    def dequeue(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        return self.list[0]

    def is_empty(self):
        return len(self.list) <= 0

    def delete(self):
        if self.is_empty():
            return m.QUEUE_EMPTY_MSG

        self.list.clear()
        return self.list


lnlq = ListNoLimitQueue()
print(lnlq.is_empty())
print(lnlq.enqueue(1))
print(lnlq.enqueue(2))
print(lnlq.peek())
print(lnlq.dequeue())
print(lnlq.dequeue())
print(lnlq.is_empty())
print(lnlq.enqueue(1))
print(lnlq.enqueue(1))
print(lnlq.is_empty())
print(lnlq.delete())
print(lnlq.is_empty())