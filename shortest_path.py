# # input()을 더 빠르게 동작하게 하기 위해 sys.std.readline 으로 치환하였다.
# # 시간 복잡도 = O(V제곱)
#
# import sys
# input = sys.stdin.readline
#
# INF = int(1e9)
#
# n, m = map(int, input().split())        # 노드의 개수, 간선의 개수
# start = int(input())                    # 시작 노드의 인덱스
# graph = [[] for i in range(n + 1)]      # 각 노드에 대한 정보를 담는 리스트
# visited = [False] * (n + 1)             # 방문 체크 리스트
# distance = [INF] * (n + 1)              # 최단 거리 테이블을 모두 무한으로 초기화
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
#
# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#         return index
#
#
# def dijkstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for i in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
#
# dijkstra(start)
#
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

# improved dijkstra 알고리즘
# 힙 자료구조를 이용하게 되면 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리하므로
# 출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.
# 최악의 경우에도 시간 복잡도 O(ElogV)를 보장하여 해결 할 수 있다.(여기서 E는 간선의 개수이다.)
# 힙 자료구조는 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나다.

# 파이썬에서는 우선순위 큐 라이브러리로 PriorityQueue와 heapq를 사용할 수 있다.
# 하지만, 일반적으로 heapq가 빠르게 동작하기 때문에 시간이 제한된 상황에서는 headpq를 추천한다.
# 우선순위 큐에는 최소 힙과 최대 힙을 이용하는데
# 최소 힙은 값이 낮은 데이터가 먼저 삭제, 최대 힙은 값이 높은 데이터가 먼저 삭제되는 구조이다.

# 우선순위 큐는 힙 자료구조 뿐만 아니라 리스트를 활용하여 작성할 수 도 있는데,
# 리스트를 활용화면 삽입시간이 O(1) 삭제시간이 O(N)이 걸리고,
# 힙을 사용시 삽입시간이 O(logN) 삭제시간이 O(logN)이 걸리기에 주로 힙을 사용한다.
# 파이썬의 우선순위 큐 라이브러리는 최소 힙에 기반한다는 점을 기억해야 한다.
# 우선순위 큐 방식은 리스트와 달리 튜플 방식으로 큐에 넣는다.

import heapq
import sys
input = sys.stdin.readline              # input을 sys의 readline으로 대체하여 처리시간 단축
INF = int(1e9)                          # 무한을 의미하는 값으로 초기화(후에 더 작은 값이 오면 대체하기 위해)

n, m = map(int, input().split())        # 노드의 개수, 간선의 개수
start = int(input())
graph = [[] for i in range(n + 1)]      # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n + 1)              # 최단 거리 테이블을 모두 무한대로 초기화

for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))             # (b, c)라는 튜플 형식으로 추가


def dijkstra(start):
    q = []                              # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))       # 거리:0, 연결노드:start 노드(0)  큐에 삽입
    distance[start] = 0                 # 리스트 0의 값의 간선길이를 0으로 초기화
    while q:                            # 큐가 비어있지 않다면,,
        dist, now = heapq.heappop(q)    # 큐에서 pop 처리를 하여 거리와 현재노드를 구함
        if distance[now] < dist:        # 이미 처리 된적이 있는 노드일 경우 무시
            continue
        for i in graph[now]:            # 현재 노드와 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]]:   # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우(갱신될 값이 리스트에 들어있는 값보다 작을 경우)
                distance[i[0]] = cost   #
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 해당 식에서는 우선순위 큐와 최단거리 테이블, 노드들의 정보가 있는 리스트들의 구조를 헷갈리지 말아야 한다.
# 우선순위 큐의 구조(heapq) : (비용, 노드)
# 노드 정보 리스트(graph)의 구조 : [a노드][(b노드, b노드 로의 길이)]
# 최단거리 테이블의 구조(distance) : distance[노드] = 최단거리 값
