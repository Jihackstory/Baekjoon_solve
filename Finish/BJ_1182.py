# 백준 1182 부분수열의 합
# 브루트포스 알고리즘, 백트래킹
# 실버 2

import sys
from itertools import combinations

N, S = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(1, N+1):
    for sub in combinations(data, i):
        if sub and S == sum(sub):
            result += 1

print(result)


