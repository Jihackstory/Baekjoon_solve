# 백준 12100 2048 (Easy)
# 구현, 브루트포스 알고리즘, 시뮬레이션
# 골드 2

import sys
import copy


def search(data, level):
    visited_q.append(data)

    if level > 4:
        return

    for command in range(4):
        # command=2
        tmp_data = move(copy.deepcopy(data), command)

        if tmp_data not in visited_q:
            search(tmp_data, level+1)
            visited_q.pop()


def move(_data, direction):
    global result
    q = []
    # Up
    if direction == 0:
        x_list = [i for i in range(N)]
        y_list = [i for i in range(N)]
    # Down
    elif direction == 1:
        x_list = [-i for i in range(1, N + 1)]
        y_list = [i for i in range(N)]
    # Left
    elif direction == 2:
        x_list = [i for i in range(N)]
        y_list = [i for i in range(N)]
    # Right
    elif direction == 3:
        x_list = [i for i in range(N)]
        y_list = [-i for i in range(1, N + 1)]

    # Up or Down
    if direction < 2:
        for y in y_list:

            for x in x_list:

                if not _data[x][y] == 0:
                    if q and q[-1] == _data[x][y]:
                        q[-1] *= 2
                        q.append(-1)
                    else:
                        if q and q[-1] == -1:
                            q.pop()
                        q.append(_data[x][y])

            if q and q[-1] == -1:
                q.pop()
            for idx in x_list:
                if q:
                    tmp = q.pop(0)
                    if tmp > result:
                        result = tmp
                    _data[idx][y] = tmp
                else:
                    _data[idx][y] = 0

    else:

        for x in x_list:

            for y in y_list:
                if not _data[x][y] == 0:
                    if q and q[-1] == _data[x][y]:
                        q[-1] *= 2
                        q.append(-1)
                    else:
                        if q and q[-1] == -1:

                            q.pop()
                        q.append(_data[x][y])

            if q and q[-1] == -1:
                q.pop()
            for idx in y_list:
                if q:
                    tmp = q.pop(0)
                    if tmp > result:
                        result = tmp
                    _data[x][idx] = tmp
                else:
                    _data[x][idx] = 0

    return _data


N = int(sys.stdin.readline())

init_data = []
for _ in range(N):
    init_data.append(list(map(int, sys.stdin.readline().split())))

result = 0
visited_q = []
search(init_data, 0)
print(result)
