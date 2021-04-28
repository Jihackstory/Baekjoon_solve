# 백준 14888 연산자 끼워넣기
# 브루트포스 알고리즘, 백트래킹
# 실버 1
#

import sys


def dfs(num, k, operator):
    global max_result, min_result

    if sum(operator) == 0:
        max_result = max(max_result, num)
        min_result = min(min_result, num)

    for idx in range(4):

        if operator[idx] > 0:
            tmp = operator[:]
            tmp[idx] -= 1
            in_num = cal(num, number[k+1], idx)
            dfs(in_num, k+1, tmp)


def cal(num1, num2, op):

    if op == 0:
        num1 += num2

    elif op == 1:
        num1 -= num2

    elif op == 2:
        num1 *= num2

    elif op == 3:

        if num1 < 0:
            num1 = 0 - num1
            num1 = num1 // num2
            num1 = 0 - num1

        else:
            num1 = num1 // num2

    return num1


n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))

# + - * /
operator_num = list(map(int, sys.stdin.readline().split()))

max_result = -1e9
min_result = 1e9

dfs(number[0], 0, operator_num)

print(max_result)
print(min_result)


