# 백준 1874 스택 수열
# 자료구조, 스택
# 실버 3

import sys
MAX_N = 100000
N = int(sys.stdin.readline())
stack = []
result = []
count = 1

for _ in range(N):
    number = int(sys.stdin.readline())
    tmp = 1
    while tmp < MAX_N:

        if not stack:
            stack.append(count)

        else:
            if stack[-1] == number:
                stack.pop()
                result.append('-')
                break
            else:
                stack.append(count)

        if stack[-1] > number:
            result = ['NO']
            break

        count += 1
        result.append('+')
        tmp += 1

    if result == ['NO']:
        break

print('\n'.join(result))

# import sys
#
# n = int(sys.stdin.readline())
# p = map(lambda x: int(x.rstrip()), sys.stdin.readlines())
#
# def solution():
#     stack, result, cnt = [], [], 1
#     for i in p:
#         while cnt <= i:
#             stack.append(cnt)
#             result.append('+')
#             cnt += 1
#         if stack.pop() != i:
#             return 'NO'
#         else:
#             result.append('-')
#     return '\n'.join(result)
#
# print(solution())