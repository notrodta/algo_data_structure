from collections import deque
queue = deque([])
queue.append("rod")
queue.append("rod1")
queue.append("rod2")
queue.append("rod3")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
print(len(queue))
