# 백준 20056 마법사 상어와 파이어볼
# 구현, 시뮬레이션
# 골드 5
#

import sys


def move(cur_info):

    new_info = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            for m, s, d in cur_info[i][j]:

                nx = (i + dx[d] * s) % n
                ny = (j + dy[d] * s) % n

                new_info[nx][ny].append((m,s,d))

    # return new_info
    new_info = split_fireball(new_info)

    return new_info


def split_fireball(info):
    new_info = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):

            len_info = len(info[i][j])

            if len_info == 1:

                new_info[i][j].append((info[i][j][0]))
            elif len_info > 1:
                sum_m, sum_s = 0, 0
                flag_odd, flag_even = 0, 0

                for m, s, d in info[i][j]:
                    sum_m += m
                    sum_s += s

                    if d % 2:
                        flag_odd += 1
                    else:
                        flag_even += 1

                nm = int(sum_m / 5)
                ns = int(sum_s / len_info)
                if nm:

                    if flag_odd * flag_even == 0:
                        d_list = [0, 2, 4, 6]
                    else:
                        d_list = [1, 3, 5, 7]

                    for idx in range(4):
                        new_info[i][j].append((nm, ns, d_list[idx]))

    return new_info


n, m, k = map(int, sys.stdin.readline().split())

init_info = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    # r, c, m, s, d
    tmp = list(map(int, sys.stdin.readline().split()))
    init_info[tmp[0]-1][tmp[1]-1].append(tuple(tmp[2:]))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

m_info = init_info
for _ in range(k):
    m_info = move(m_info)


result = 0
for i in range(n):
    for j in range(n):
        for m, s, d in m_info[i][j]:
            result += m

print(result)
