# 백준 1003 피보나치
# 다이나믹 프로그래밍
# 실버 3


import sys


def pibonacci(number, init_count):
    count = [] + init_count
    if number == 0:
        # print("0이 출력됩니다.")
        count[0] += 1
        return 0, count
    elif number == 1:
        # print("1이 출력됩니다.")
        count[1] += 1
        return 1, count
    else:
        pibo_num1, count1 = pibonacci(number - 1, count)
        pibo_num2, count2 = pibonacci(number - 2, count)
        count[0] += count1[0] + count2[0]
        count[1] += count1[1] + count2[1]

        return pibo_num1 + pibo_num2, count


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
    # init_count = [0, 0]
    # pibo_num, count_tmp = pibonacci(data[idx], init_count)
    # print(count_tmp[0], count_tmp[1])
    count_0, count_1 = check_count(data[idx])
    print(count_0, count_1)

