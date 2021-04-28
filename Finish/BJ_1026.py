# 백준 1026번 보물
# 정렬

import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort(reverse=True)

index_num = sorted(range(len(B)), key=lambda k: B[k])
result_sum = 0
for i in range(N):
    result_sum += A[i] * B[index_num[i]]


print(result_sum)
