# 백준 15686 치킨 배달
# 구현, 브루트포스 알고리즘
# 골드 5
#

import sys
from itertools import combinations
INF = 1e9


def cal_ch_dist(chicken_list):
    sum_dist = 0

    for i in range(nh):
        h_row, h_col = house[i]
        tmp_min = INF

        for chicken in chicken_list:
            c_row, c_col = chicken
            tmp_min = min(tmp_min, abs(h_row - c_row) + abs(h_col - c_col))

        sum_dist += tmp_min
    return sum_dist


n, m = map(int, sys.stdin.readline().split())

chicken, house = [], []
nh = 0
nc = 0
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):

        if tmp[j] == 2:
            chicken.append((i, j))
            nc += 1
        elif tmp[j] == 1:
            house.append((i, j))
            nh += 1


result = INF
c_list = list(combinations(chicken, m))

for chi in c_list:

    num_ch_dist = cal_ch_dist(chi)
    if result > num_ch_dist:
        result = num_ch_dist

print(result)
