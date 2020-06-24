from collections import deque

my_que = deque()

for _ in range(int(input())):
    inp = input()
    if inp == "DEQUEUE":
        my_que.pop()
    else:
        my_que.appendleft(inp.replace("ENQUEUE ", ""))

while my_que:
    print(my_que.pop())