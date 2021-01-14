# Breadth First Search  너비 우선 탐색 알고리즘(가까운 곳부터 탐색), DFS 는 가장 멀리 있는 노드를 우선으로 탐색한다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
# 재귀함수로 DFS 를 구현하면 컴퓨터 특성 상 실제 프로그램의 수행 시간은 느려질 수 있다
# 그래서 코딩 테스트에서는 보통 DFS 보다 BFS 구현이 조금 더 빠르게 동작한다.

from collections import deque
import time

start_time = time.time()


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],  # 1 과 연결된 노드
    [1, 7],     # 2 와 연결된 노드
    [1, 4, 5],  # ...
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 노드의 트리형식 리스트, 시작노드, 노드방문 리스트
bfs(graph, 1, visited)

end_time = time.time()

print('\n소요시간 :', end_time - start_time)