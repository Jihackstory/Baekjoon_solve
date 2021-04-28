# 백준 14888 연산자 끼워넣기
#
# 실버 1
#

import sys
from itertools import permutations



n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))

# + - * /
operator_num = list(map(int, sys.stdin.readline().split()))

op = []
for idx in range(4):
    op += [idx] * operator_num[idx]

operator_set = permutations(op, len(op))

max_result = -1e9
min_result = 1e9

for operator in operator_set:
    result = number[0]

    for idx in range(n-1):

        if operator[idx] == 0:
            result += number[idx + 1]

        elif operator[idx] == 1:
            result -= number[idx + 1]

        elif operator[idx] == 2:
            result *= number[idx + 1]

        elif operator[idx] == 3:
            if result < 0:
                result = 0 - result
                result = result // number[idx + 1]
                result = 0 - result

            else:
                result = result // number[idx + 1]

    max_result = max(max_result, result)
    min_result = min(min_result, result)


print(max_result)
print(min_result)


