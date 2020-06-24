from collections import deque

students_que = deque()

for _ in range(int(input())):
    inp = input()
    if inp.startswith("READY"):
        students_que.appendleft(inp.replace("READY ", ""))
    elif inp == "PASSED":
        print(students_que.pop())
    else:
        students_que.appendleft(students_que.pop())