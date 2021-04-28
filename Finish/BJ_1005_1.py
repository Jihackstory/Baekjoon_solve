import sys

data = []
n = int(sys.stdin.readline())
for i in range(n):
    tmp = []
    tmp.append(list(map(int, sys.stdin.readline().split())))

    for j in range(tmp[0][1] + 2):
        tmp.append(list(map(int, sys.stdin.readline().split())))

    data.append(tmp)

for i in range(n):

    # 건물 수, 규칙 수
    num_building, num_building_rule = data[i][0]

    # 건물 지어지는 시간
    init_building_time = data[i][1]

    # 최종적으로 지어야 하는 건물
    gool = data[i][-1][0] - 1

    # 이 건물을 짓기 위해 필요한 선행 건물 목록
    tmp_graph = [[] for i in range(num_building)]
    # 이 건물을 지으면 지을 수 있는 건물 목록
    graph = [[] for i in range(num_building)]

    # make rule_path
    for idx in range(num_building_rule):
        building_rule = data[i][2+idx]
        tmp_graph[building_rule[1] - 1].append(building_rule[0] - 1)
        graph[building_rule[0] - 1].append(building_rule[1] - 1)

    # 이 건물이 지어지기 위해 걸리는 시간
    building_time = [0 for i in range(num_building)]

    for _ in range(num_building):
        # 처음 시작 위치 = 선행 건물 목록이 없는 것
        cur_node = tmp_graph.index([])
        # 건물 짓기 완료
        tmp_graph[cur_node].append(1e9)

        for idx in range(len(graph[cur_node])):
            # 선행 건물 지어지면 목록에서 제거
            # -> 선행 건물이 다 지어진 순서대로 검색하기 위함
            tmp_graph[graph[cur_node][idx]].remove(cur_node)

            # 건물이 지어지는 시간 계산
            cost = building_time[cur_node] + init_building_time[cur_node]

            # 이전에 찾은 것보다 오래 걸리면 업데이트
            if cost > building_time[graph[cur_node][idx]]:
                building_time[graph[cur_node][idx]] = cost

    print(building_time[gool] + init_building_time[gool])

