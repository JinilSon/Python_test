# input()을 더 빠르게 동작하게 하기 위해 sys.std.readline 으로 치환하였다.


import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())        # 노드의 개수, 간선의 개수
start = int(input())                    # 시작 노드의 인덱스
graph = [[] for i in range(n + 1)]      # 각 노드에 대한 정보를 담는 리스트
visited = [False] * (n + 1)             # 방문 체크 리스트
distance = [INF] * (n + 1)              # 최단 거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

