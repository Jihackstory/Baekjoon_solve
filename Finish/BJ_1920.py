# 19분 18초
import sys

N = int(sys.stdin.readline())
base_set = set(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
element = list(map(int, sys.stdin.readline().split()))


# version 1
# for i in element:
#
#     if base_set.issuperset([i]):
#         print('1')
#     else:
#         print('0')

# version 2
for i in element:

    if i in base_set:
        print('1')
    else:
        print('0')