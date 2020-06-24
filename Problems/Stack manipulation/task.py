from collections import deque

my_stack = deque()

for _ in range(int(input())):
    inp = input()
    if inp == "POP":
        my_stack.pop()
    else:
        my_stack.append(inp.replace("PUSH ", ""))

while my_stack:
    print(my_stack.pop())