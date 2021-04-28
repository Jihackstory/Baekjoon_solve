# 백준 14500 테트로미노
# 구현, 브루트포스 알고리즘
# 골드 5
#

import sys


def search(row, col, level, value):
    global result

    if level == 4:
        if result < value:
            result = value
        return

    for r_idx in d_list:
        r_tmp = row + r_idx[0]
        c_tmp = col + r_idx[1]

        if (-1 < r_tmp < N) and (-1 < c_tmp < M) and visited[r_tmp][c_tmp] == 0:
            visited[r_tmp][c_tmp] = 1
            search(r_tmp, c_tmp, level + 1, value + data[r_tmp][c_tmp])
            visited[r_tmp][c_tmp] = 0


def exception(row, col):
    global result
    for i in excep_block:
        try:
            num = data[row][col] \
                  + data[row + i[0][0]][col + i[0][1]] \
                  + data[row + i[1][0]][col + i[1][1]] \
                  + data[row + i[2][0]][col + i[2][1]]
        except:
            num = 0
        result = max(result, num)


N, M = map(int, sys.stdin.readline().split())
d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = 0
visited = [[0 for i in range(M)] for _ in range(N)]
excep_block = [[[0, 1], [0, 2], [-1, 1]],
               [[0, 1], [0, 2], [1, 1]],
               [[1, 0], [2, 0], [1, 1]],
               [[1, 0], [1, -1], [2, 0]]]

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        search(r, c, 1, data[r][c])
        visited[r][c] = 0
        exception(r, c)

print(result)
