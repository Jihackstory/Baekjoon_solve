# 백준 14501 퇴사
# 다이나믹 프로그래밍, 브루트포스 알고리즘
# 실버 4
#

import sys

N = int(sys.stdin.readline())

time_list = [0 for _ in range(N)]
money_list = [0 for _ in range(N)]
result = 0

for idx in range(N):

    time_list[idx], money_list[idx] = map(int, sys.stdin.readline().split())


dp = [0 for _ in range(N+5)]

for idx in range(N):
    if dp[idx] > dp[idx+1]:
        dp[idx+1] = dp[idx]

    if dp[idx + time_list[idx]] < dp[idx] + money_list[idx]:
        dp[idx + time_list[idx]] = dp[idx] + money_list[idx]

print(dp[N])

