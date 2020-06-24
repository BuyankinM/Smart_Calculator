from collections import deque

books_stack = deque()

for _ in range(int(input())):
    inp = input()
    if inp == "READ":
        print(books_stack.pop())
    else:
        books_stack.append(inp.split(maxsplit=1)[1])