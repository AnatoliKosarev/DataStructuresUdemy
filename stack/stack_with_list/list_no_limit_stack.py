from stack.messages import STACK_EMPTY_MSG


class ListNoLimitStack:
    def __init__(self):
        self.list = []

    def __repr__(self):
        return '\n'.join(str(v) for v in reversed(self.list))

    def push(self, value):
        self.list.append(value)
        return self.list

    def pop(self):
        try:
            return self.list.pop()
        except IndexError:
            return STACK_EMPTY_MSG

    def peek(self):
        try:
            return self.list[-1]
        except IndexError:
            return STACK_EMPTY_MSG

    def is_empty(self):
        return len(self.list) == 0

    def delete(self):
        self.list.clear()
        # self.list = None
        return self.list


lnls = ListNoLimitStack()
print(lnls.is_empty())
lnls.push(1)
lnls.push(2)
print(lnls.push(3))
print(lnls.pop())
print(lnls.peek())
print(lnls.is_empty())
print(lnls.delete())
print(lnls.pop())
print(lnls.peek())
