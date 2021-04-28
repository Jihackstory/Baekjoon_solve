# 백준 14499 주사위 굴리기
# 구현, 시뮬레이션
# 골드 5
# 124분

import sys
from collections import deque

N, M, row, col, K = map(int, sys.stdin.readline().split())

board = []

for idx in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

command_list = list(map(int, sys.stdin.readline().split()))



dice_r = [0, 0, 0, 0]
dice_c = [0, 0, 0, 0]

r_count, c_count = 0, 0

for command in command_list:
    # print(board)
    # 1: 동쪽, 2: 서쪽
    if command < 3:
        if -1 < col + (-1)**(command + 1) < M:
            col += (-1)**(command + 1)
            c_count += (-1)**(command + 1)

            if board[row][col] == 0:
                board[row][col] = dice_c[c_count % 4]
            else:
                dice_c[c_count % 4] = board[row][col]
                board[row][col] = 0

            dice_r[r_count % 4] = dice_c[c_count % 4]
            dice_r[(r_count + 2) % 4] = dice_c[(c_count + 2) % 4]
            print(dice_c[(c_count + 2) % 4])

    else:
        if -1 < row + (-1)**command < N:
            row += (-1)**command
            r_count += (-1)**command

            if board[row][col] == 0:
                board[row][col] = dice_r[r_count % 4]
            else:
                dice_r[r_count % 4] = board[row][col]
                board[row][col] = 0
            dice_c[c_count % 4] = dice_r[r_count % 4]
            dice_c[(c_count + 2) % 4] = dice_r[(r_count + 2) % 4]
            print(dice_r[(r_count + 2) % 4])

