# 위상 정렬 알고리즘

from collections import deque
import copy

v = int(input())                        # 노드의 개수 n
indegree = [0] * (v + 1)                # 진입차수는 0으로 초기화
graph = [[] for i in range(v + 1)]      # 노드의 개수만큼 공간 생성(간선 연결 리스트)
time = [0] * (v + 1)                    # 각 노드별 시간 테이블

for i in range(1, v + 1):
    data = list(map(int, input().split()))  # data구조(시간, 강의 번호, -1로 끝남)
    time[i] = data[0]                       # 입력받은 데이터의 시간을 추출하여 time테이블에 입력
    for x in data[1:-1]:
        indegree[i] += 1                    # 0번째 노드를 제외하고 전부 진입차수는 1이다.
        graph[x].append(i)                  # 진입 차수 번지에 다음으로 갈 수 있는 노드의 값을 추가한다.


def topology_sort():
    result = copy.deepcopy(time)        # 알고리즘 수행 결과를 담을 리스트
    q = deque()                         # deque라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            print(now)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v + 1):
        print(result[i])



topology_sort()