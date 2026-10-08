

from collections import deque

queue = deque()

# Add elements to the queue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after adding elements:", queue)

# Remove the first element
removed = queue.popleft()
print("Removed element:", removed)

print("Queue after removing element:", queue)

# Check the first element
print("First element:", queue[0])

# Check if queue is empty
if len(queue) == 0:
    print("Queue is empty.")
else:
    print("Queue is not empty.")
