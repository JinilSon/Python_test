# # 신장 트리란 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.
#
#
# # 크루스칼 알고리즘
# # 최소한의 비용으로 신장 트리를 찾는 대표적인 알고리즘(그리디 알고리즘)
# # 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# # 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# #   사이클이 발생하면 포함X, 발생하지 않으면 포함시킨다.
# # 3. 모든 간선에 대하여 2번 과정을 반복한다.
#
# # 최종적으로는 신장 트리에 포함되는 간선의 개수가 *노드의개수 - 1*의 값을 가진다는 특징이 있다.
# def find_parent(parent ,x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
#
# def union_parent(parent , a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v + 1)
# edges = []
# result = 0
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))
#
# edges.sort()
#
# for edge in edges:
#     cost, a, b = edge
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result += cost
#
# print(result)

# 위상 정렬 Topology Sort
# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것이다.
# 차례대로 모든 노드를 확인하고, 해당 노드에서 출발하는 간선을 차례대로 제거해야 한다.
# 위상 정렬의 시간 복잡도는 O(V + E)이다.
# ex) 선수과목을 고려한 학습순서 설정
# 진입차수란 특정한 노드로 들어오는 간선의 개수를 의미한다.
# 1. 진입차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
#   큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
#   새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()