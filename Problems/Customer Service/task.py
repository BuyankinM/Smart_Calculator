from collections import deque

my_que = deque()

for _ in range(int(input())):
    inp = input()
    if inp == "SOLVED":
        my_que.pop()
    else:
        my_que.appendleft(inp.replace("ISSUE ", ""))

while my_que:
    print(my_que.pop())