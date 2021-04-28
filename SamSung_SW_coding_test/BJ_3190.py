# 백준 3190 뱀
# 구현, 자료구조, 시뮬레이션, 덱, 큐
# 골드 5
# 58분

import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

A_loc = [[] for _ in range(N)]
for _ in range(K):
    x, y = list(map(int, sys.stdin.readline().split()))
    # 사과는 1행 1열로 따짐 -> 1부터 시작
    A_loc[x-1].append(y-1)

L = int(sys.stdin.readline())

L_list = [tuple(sys.stdin.readline().split()) for _ in range(L)]
# 종료 시그널
L_list.append([-1])

time = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
command_index = 0
x, y = 0, 0

Snake_q = deque([(x, y)])
dx, dy = direction[command_index]

while L_list:
    time += 1

    x += dx
    y += dy

    if not (-1 < x < N and -1 < y < N):
        break

    if (x, y) in Snake_q:
        break

    Snake_q.append((x, y))
    if y in A_loc[x]:
        A_loc[x].remove(y)
    else:
        Snake_q.popleft()

    if int(L_list[0][0]) == time:
        _, command = L_list.pop(0)

        if command == 'L':
            command_index = (command_index - 1) % 4
        else:
            # command == 'D'
            command_index = (command_index + 1) % 4

        dx, dy = direction[command_index]

print(time)
