from stack.messages import STACK_IS_FULL_MSG, STACK_EMPTY_MSG, STACK_LIMIT_REPR


class ListLimitStack:
    def __init__(self, limit):
        self.limit = limit
        self.list = []

    def __repr__(self):
        return STACK_LIMIT_REPR.format(limit=self.limit, list_length=len(self.list), list=self.list)

    def push(self, value):
        if self.is_full():
            return STACK_IS_FULL_MSG

        self.list.append(value)
        return self

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

    def is_full(self):
        return len(self.list) >= self.limit

    def is_empty(self):
        return len(self.list) == 0

    def delete(self):
        self.list.clear()
        return self.list


lls = ListLimitStack(1)
print(lls.push(1))
print(lls.is_full())
print(lls.push(2))
print(lls.delete())