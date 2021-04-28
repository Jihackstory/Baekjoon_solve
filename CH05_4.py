import sys
from collections import deque


def bfs(x, y):

    que = deque()
    que.append((x, y))

    while que:

        x, y = que.popleft()
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            if not ((-1 < nx < n) and (-1 < ny < m)):
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print(bfs(0, 0))
