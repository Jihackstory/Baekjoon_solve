# 백준 15685 드래곤 커브
# 구현, 시뮬레이션
# 골드 4
#

import sys


def rotation(input_q):

    new_que = []
    dx, dy = input_q[-1]

    while input_q:

        row, col = input_q.pop()
        # 기준점을 통한 평행이동
        row -= dx
        col -= dy

        # 회전
        nr = col
        nc = -1 * row

        # 평행이동 복귀
        nr += dx
        nc += dy

        # 사용 체크
        board[nr][nc] = 1
        new_que.append([nr, nc])

    return new_que


def generator(row, col, dist, gen):

    que = [[row, col]]
    board[row][col] = 1
    nr = row + d_list[dist][0]
    nc = col + d_list[dist][1]
    que.append([nr, nc])
    board[nr][nc] = 1

    for _ in range(gen):
        tmp = que.copy()
        new_que = rotation(tmp)
        que += new_que[1:]


n = int(sys.stdin.readline())

board = [[0 for _ in range(101)] for _ in range(101)]
d_list = [(0, 1), (-1, 0), (0, -1), (1, 0)]
data = []

for idx in range(n):
    x, y, d, g = list(map(int, sys.stdin.readline().split()))
    generator(y, x, d, g)

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j]*board[i+1][j]*board[i][j+1]*board[i+1][j+1]:
            result += 1

print(result)


