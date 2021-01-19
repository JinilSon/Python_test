import time

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

start_time = time.time()


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1     # 현재 노드를 방문처리하고,,
        dfs(x - 1, y)       # 상
        dfs(x, y - 1)       # 우
        dfs(x+1, y)         # 하
        dfs(x, y+1)         # 좌 중에서 0인 값을 모두 방문처리한다.
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:   # 한 덩어리의 아이스크림을 모두 방문처리했으면 result 값을 올린다
            result += 1

end_time = time.time()
print(result)
print("경과시간 :", end_time-start_time)
