# 해당 문제는 플로이드 워셜 알고리즘으로 제작함

INF = int(1e9)                                              # 무한

n, m = map(int, input().split())                            # n : 노드의 수, m : 간선의 수
graph = [[INF] * (n + 1) for _ in range(n + 1)]             # 모든 노드가 시작점인 상태에서 다른 모든 노드에게로의 공간

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0                                 # 자신에게로 향하는 거리는 0이다.

for _ in range(m):
    a, b = map(int, input().split())                        # 입력받은 간선의 경로를 1로 초기화시킨다.
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())                            # x : 타회사, k : 소개팅 장소

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])       # 각 노드에서 다른 노드까지의 거리를 입력하고 최솟값이 있으면 교체한다.


distance = graph[1][k] + graph[k][x]                        # 현재 위치가 1번 노드인 A가 K에 가서 소개팅을하고 X 타회사에 가야한다.

if distance >= INF:                                         # 최종 합산 거리를 계산 할 수 없으면 -1로, 계산할 수 있으면 그대로 표현한다.
    print("-1")
else:
    print(distance)
