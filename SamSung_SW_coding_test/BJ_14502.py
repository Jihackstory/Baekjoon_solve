# 백준 14502 연구소
# 그래프 이론, 그래프 탐색, 브루트포스 알고리즘, 너비 우선 탐색 (BFS)
# 골드 5
#

import sys
from collections import deque
import copy


def bfs(x, y, board):

    que = deque()
    que.append((x, y))
    board[x][y] = 2

    while que:
        x, y = que.popleft()

        for idx in range(4):
            nx = x + d[idx][0]
            ny = y + d[idx][1]

            if (-1 < nx < n) and (-1 < ny < m):
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    que.append((nx, ny))


def wall(st, count):
    global result

    if count == 3:
        new_graph = copy.deepcopy(graph)
        for v in loc_v:
            bfs(v[0], v[1], new_graph)
        count_safe = sum(new_graph[i].count(0) for i in range(n))
        result = max(result, count_safe)
        return

    else:
        for idx in range(st, n * m):
            row = idx // m
            col = idx % m

            if graph[row][col] == 0:
                graph[row][col] = 1
                wall(idx, count + 1)
                graph[row][col] = 0


n, m = map(int, sys.stdin.readline().split())
graph = []
loc_v = []
for idx1 in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for idx2 in range(m):
        if graph[-1][idx2] == 2:
            loc_v.append((idx1, idx2))

result = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
wall(0, 0)
print(result)
