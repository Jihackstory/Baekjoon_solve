import sys

T = int(sys.stdin.readline())


def dfs(L_graph, n):
    visited[n] = True
    result.append(n)
    print('시작하는 것 : ', n)
    for i in L_graph[n]:
        if not visited[i]:
            dfs(L_graph, i)
    print('끝나는 것 : ', n)
    result_num = len(result)
    if result_num > 1:
        intersection = list(set(graph[result[-1]]) & set(graph[result[-2]]))

        if result_num > 2 and intersection and len(graph[result[-1]]) == 2:
            result_set.append((result[-1],result[-3]))
            result.pop(-3)
            result.pop()


        elif L_graph[result[-1]].count(result[-2]):

            result_set.append((result[-1], result[-2]))
            result.pop()
            result.pop()
        else:
            result.pop()

    return


def num_edge(cur_node):
    tmp = near_location(cur_node)
    for i in range(3):
        if enemy[cur_node] + enemy[tmp[i]] <= W:
            graph[cur_node].append(tmp[i])


def near_location(cur_node):

    return [int(cur_node / N) * N + (cur_node + 1) % N,
            int(cur_node / N) * N + (cur_node - 1) % N,
            cur_node + N * ((-1) ** int(cur_node / N))]


for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    in_circle = list(map(int, sys.stdin.readline().split()))
    out_circle = list(map(int, sys.stdin.readline().split()))

    result_set = []
    visited = [0 for i in range(2 * N)]
    fixed = [0 for i in range(2 * N)]
    graph = [[] for i in range(2 * N)]
    enemy = in_circle + out_circle

    for idx in range(2 * N):
        num_edge(idx)

    for i in range(2 * N):
        result = []

        if not visited[i]:
            dfs(graph, i)

    print(2 * N - len(result_set))

