from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.popleft()
print(queue)
print(list(queue))