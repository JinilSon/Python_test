# C라는 도시에서 위급 상황이 발생하여 최대한 많은 도시로 메시지를 보내고자 한다
# 하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면 X에서 Y로 향하는 통로가 있어야한다.
# 최적화된 다익스트라 알고리즘 문제
# 큐의 역할 : 다음으로 계산할 노드를 알려준다
# graph의 역할 : 입력된 노드와 통로의 길이를 받는다
# distance의 역할 : 최단 거리를 입력받는다.
import heapq
import sys

input = sys.stdin.readline()
INF = int(1e9)

n, m, start = map(int, input().split())         # n:도시의 개수, m:통로의 개수, start:시작노드
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))                     # x에서 y 노드로 가는 비용이 z이다.


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

count = 0

max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)