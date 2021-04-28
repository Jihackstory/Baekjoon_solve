# 백준 14503 로봇 청소기
#
# 골드 5
#

import sys

n, m = map(int, sys.stdin.readline().split())

row, col, direction = map(int, sys.stdin.readline().split())
data = []
for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

result = 1
count = 0

# 0: 북, 1: 동, 2: 남, 3: 서
d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:

    data[row][col] = 2

    direction = (direction - 1) % 4
    nr = row + d_list[direction][0]
    nc = col + d_list[direction][1]

    if data[nr][nc] == 0:
        result += 1
        row = nr
        col = nc
        count = 0
    else:
        count += 1

    if count == 4:

        nr = row + d_list[(direction - 2) % 4][0]
        nc = col + d_list[(direction - 2) % 4][1]

        if data[nr][nc] == 1:
            break
        else:
            row = nr
            col = nc
            count = 0

    # # 청소기 이동경로 체크
    # for i in range(n):
    #     print(''.join(map(str, data[i])))
    # print('==========================================')


print(result)

