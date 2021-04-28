# 백준 9095 1, 2, 3 더하기
# 다이나믹 프로그래밍
# 실버 3


## 첫번째 풀이
# import sys
#
#
# # 조합 수 계산 (nCr)
# def num_combination(n, r):
#     _result = 1
#
#     if r > n//2:
#         r = n - r
#
#     if r == 0:
#         return 1
#
#     for _ in range(r):
#         _result *= n/r
#         n -= 1
#         r -= 1
#     return int(_result)
#
#
# def sol(num_set):
#
#     total = sum(num_set)
#     _result = num_combination(total, num_set[0]) * \
#               num_combination(total - num_set[0], num_set[1])
#
#     return _result
#
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     N = int(sys.stdin.readline())
#
#     num_N = [N, 0, 0]
#
#     result = 0
#
#     while 1:
#
#         while 1:
#             result += sol(num_N)
#             num_N[1] += 1
#             num_N[0] -= 2
#             if num_N[0] < 0:
#                 break
#
#         num_N[1] = 0
#         num_N[0] = N - 3 * num_N[2]
#
#         num_N[2] += 1
#         num_N[0] -= 3
#         if num_N[0] < 0:
#             break
#
#     print(result)

## 두번째 풀이 (DP)

import sys

N = int(sys.stdin.readline())

MAX_num = 11
DP_mem = [1, 2, 4]


for i in range(MAX_num-3):
    DP_mem.append(sum(DP_mem[-3:]))

for _ in range(N):
    number = int(sys.stdin.readline())
    print(DP_mem[number-1])

