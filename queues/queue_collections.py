from collections import deque

coll_queue = deque(maxlen=3)
print(coll_queue)

# adding elements
coll_queue.append(1)
coll_queue.append(2)
coll_queue.append(3)
print(coll_queue)

# if max_len set and number of elements exceeds it - first elements get exchanged for newly added
coll_queue.append(4)
print(coll_queue)

# getting first element
print(coll_queue.popleft())
print(coll_queue)

# removing all elements
coll_queue.clear()
print(coll_queue)
