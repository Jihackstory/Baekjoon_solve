# 백준 13460 구슬 탈출 2
# 구현, 그래프이론, 그래프탐색, 너비우선탐색, BFS
# 골드 2

import sys
import copy


def move(_board, command, ball):
    if ball == O_loc:
        return _board, ball

    if command == 'U':
        while 1:

            if _board[ball[0] - 1][ball[1]] == '.':
                tmp = _board[ball[0] - 1][ball[1]]
                _board[ball[0] - 1][ball[1]] = _board[ball[0]][ball[1]]
                _board[ball[0]][ball[1]] = tmp
                ball[0] -= 1
            elif _board[ball[0] - 1][ball[1]] == 'O':
                _board[ball[0]][ball[1]] = '.'
                ball[0] -= 1
                break
            else:
                break

    elif command == 'D':
        while 1:

            if _board[ball[0] + 1][ball[1]] == '.':
                tmp = _board[ball[0] + 1][ball[1]]
                _board[ball[0] + 1][ball[1]] = _board[ball[0]][ball[1]]
                _board[ball[0]][ball[1]] = tmp
                ball[0] += 1
            elif _board[ball[0] + 1][ball[1]] == 'O':
                _board[ball[0]][ball[1]] = '.'
                ball[0] += 1
                break
            else:
                break

    elif command == 'R':
        while 1:
            if _board[ball[0]][ball[1] + 1] == '.':
                tmp = _board[ball[0]][ball[1] + 1]
                _board[ball[0]][ball[1] + 1] = _board[ball[0]][ball[1]]
                _board[ball[0]][ball[1]] = tmp
                ball[1] += 1
            elif _board[ball[0]][ball[1] + 1] == 'O':
                _board[ball[0]][ball[1]] = '.'
                ball[1] += 1
                break
            else:
                break

    elif command == 'L':
        while 1:

            if _board[ball[0]][ball[1] - 1] == '.':
                tmp = _board[ball[0]][ball[1] - 1]
                _board[ball[0]][ball[1] - 1] = _board[ball[0]][ball[1]]
                _board[ball[0]][ball[1]] = tmp
                ball[1] -= 1
            elif _board[ball[0]][ball[1] - 1] == 'O':
                _board[ball[0]][ball[1]] = '.'
                ball[1] -= 1
                break
            else:
                break

    return _board, ball


def search(board, R, B, count):
    global result
    visited[R[0]][R[1]][B[0]][B[1]] = True

    if B == O_loc:
        return

    elif R == O_loc:
        if result > count:
            result = count
        return

    if count > 10:
        return

    # command_list = ['U', 'D', 'R', 'L']
    command_list = ['L', 'D', 'U', 'R']
    for command in command_list:
        tmp_board, tmp_R = move(copy.deepcopy(board), command, R[:])
        tmp_board, tmp_B = move(tmp_board, command, B[:])
        tmp_board, tmp_R = move(tmp_board, command, tmp_R)

        if not visited[tmp_R[0]][tmp_R[1]][tmp_B[0]][tmp_B[1]]:
            search(tmp_board, tmp_R[:], tmp_B[:], count + 1)
            visited[tmp_R[0]][tmp_R[1]][tmp_B[0]][tmp_B[1]] = False

    visited[R[0]][R[1]][B[0]][B[1]] = False


N, M = list(map(int, sys.stdin.readline().split()))

init_board = []
for idx in range(N):
    tmp = list(sys.stdin.readline().strip())
    if 'R' in tmp:
        R_loc = [idx, tmp.index('R')]
    if 'B' in tmp:
        B_loc = [idx, tmp.index('B')]
    if 'O' in tmp:
        O_loc = [idx, tmp.index('O')]
    init_board.append(tmp)

result = 100
visited = [[[[0 for _ in range(M)] for _ in range(N)]for _ in range(M)]for _ in range(N)]

search(init_board, R_loc, B_loc, 0)
if result > 10:
    print(-1)
else:
    print(result)
