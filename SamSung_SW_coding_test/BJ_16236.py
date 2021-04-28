# 백준 16236 아기 상어
#
# 골드 4
#

import sys
from collections import deque

INF = 1e9

n = int(sys.stdin.readline())
board = []

for row in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

    for col in range(n):
        if board[row][col] == 9:
            now_row = row
            now_col = col
            board[row][col] = 0

size_sh = 2
d_list = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def bfs():
    que = deque()
    que.append((now_row, now_col))
    dist = [[-1 for _ in range(n)] for _ in range(n)]
    dist[now_row][now_col] = 0

    while que:
        v = que.popleft()

        for i in range(4):
            nr = v[0] + d_list[i][0]
            nc = v[1] + d_list[i][1]

            if -1 < nr < n and -1 < nc < n:
                if dist[nr][nc] == -1 and board[nr][nc] <= size_sh:
                    dist[nr][nc] = dist[v[0]][v[1]] + 1
                    que.append((nr, nc))

    return dist


def search(dist):
    near_fish = INF
    for row in range(n):
        for col in range(n):

            if (dist[row][col] != -1) and (0 < board[row][col] < size_sh):
                if near_fish > dist[row][col]:
                    near_row, near_col = row, col
                    near_fish = dist[row][col]

    if near_fish == INF:
        return None

    else:
        return near_row, near_col, near_fish


ate_fish = 0
result = 0

while True:

    value = search(bfs())

    if value == None:
        print(result)
        break

    now_row, now_col = value[0], value[1]
    result += value[2]
    board[now_row][now_col] = 0

    ate_fish += 1

    if ate_fish >= size_sh:
        size_sh += 1
        ate_fish = 0
