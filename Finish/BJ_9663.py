# 백준 9663 N-Queen
# 브루트포스 알고리즘, 백트래킹
# 골드 5

import sys


def isvalid(x):
    for i in range(x):

        if board[i] == board[x] or \
                abs(board[i] - board[x]) == x - i:
            return 0

    return 1


def search(x):
    global result

    if x == N:
        result += 1

    else:
        for idx in range(N):
            board[x] = idx
            if isvalid(x):
                search(x+1)

N = int(sys.stdin.readline())
board = [0] * N
result = 0
search(result)

print(result)
