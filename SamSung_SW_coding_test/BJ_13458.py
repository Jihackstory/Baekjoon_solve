# 백준 13458 시험 감독
# 수학
# 브론즈 2
# 9분

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = list(map(int, sys.stdin.readline().split()))

result = 0

for idx in range(N):

    if A[idx] > B:
        result += (A[idx] - B)//C
        if (A[idx] - B) % C:
            result += 1

    result += 1

print(result)