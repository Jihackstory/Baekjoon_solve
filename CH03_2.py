import sys

N, M, K = map(int, sys.stdin.readline().split())
data_list = list(map(int, sys.stdin.readline().split()))

max_sum = 0
first = 0
second = 0

for data in data_list:

    if data > first:
        second = first
        first = data
        print(first, second)

    elif data > second:
        second = data


a = M // K
b = M % K
if first == second:
    max_sum = N * first
else:
    max_sum = first * a * K + second * b

print(max_sum)
