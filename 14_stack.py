

stack = []

# Push elements into the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after push:", stack)

# Peek at the top element
print("Top element:", stack[-1])

# Pop an element
removed = stack.pop()
print("Removed element:", removed)

print("Stack after pop:", stack)

# Check if stack is empty
if len(stack) == 0:
    print("Stack is empty.")
else:
    print("Stack is not empty.")
