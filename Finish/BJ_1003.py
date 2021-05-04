# 백준 1003 피보나치
# 다이나믹 프로그래밍
# 실버 3

###############
# version 1
###############
import sys


def check_count(number):
    count_0, count_1 = 1, 0
    iter_count = 0
    while iter_count < number:

        tmp = count_0 + count_1
        count_0 = count_1
        count_1 = tmp
        iter_count += 1

    return count_0, count_1


data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.extend(list(map(int, sys.stdin.readline().split())))

for idx in range(n):

    count_0, count_1 = check_count(data[idx])
    print(count_0, count_1)

###############
# version 2
###############
# import sys
#
# n = int(sys.stdin.readline())
# dp = [[1, 0], [0, 1]]
# data = [int(sys.stdin.readline()) for _ in range(n)]
#
# # 미리 만들어 두기 Dynamic programing
# for i in range(2, max(data) + 1):
#     dp.append([dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]])
#
# for i in data:
#     print(dp[i][0], dp[i][1])
