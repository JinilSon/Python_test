import time
# # 본인이 그저 풀어본 답안
# N, M = map(int, input().split())
# X, Y, Direction = map(int, input().split())
# # X, 세로위치  Y, 가로위치  Direction, 방향(0:북쪽, 1:동쪽, 2:남쪽, 3:서쪽)
#
# Map = [[int(x) for x in input().split()] for y in range(N)]
# t_map = [[0 for _ in range(M)] for _ in range(N)]
#
# start_time = time.time()
#
# count = 0
# switch = 0
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# # 현재 위치 카운팅
# count += 1
# t_map[X][Y] = 1
#
# # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
# while 1:
#
#     Direction -= 1
#     if Direction < 0:
#         Direction = 3
#
# # 2. 캐릭터의 바로 왼쪽방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
# #    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
#     if Map[X+dx[Direction]][Y+dy[Direction]] == 0:
#         if t_map[X+dx[Direction]][Y+dy[Direction]] == 0:
#             t_map[X+dx[Direction]][Y+dy[Direction]] = 1
#             X += dx[Direction]
#             Y += dy[Direction]
#             count += 1
#             switch = 0
#
#     switch += 1
#
#     if switch == 4:
#         back = (Direction + 2) % 4
#         if Map[X+dx[back]][Y+dy[back]] == 0:
#             X += dx[back]
#             Y += dy[back]
#             count += 1
#             switch = 0
#         elif Map[X+dx[back]][Y+dy[back]] == 1:
#             break
#
# end_time = time.time()
#
# print("맵의 구성도")
# for i in range(N):
#     for j in range(M):
#         print((Map[i][j]), end=" ")
#     print("\n")
# print("다녀온 맵의 구성도")
# for i in range(N):
#     for j in range(M):
#         print((t_map[i][j]), end=" ")
#     print("\n")
# print("방문한 칸의 수 :", count)
# print("수행시간 :", end_time - start_time)


# 답안
n, m = map(int, input().split())
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1         # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

start_time = time.time()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
    print(direction)

end_time = time.time()

print("맵의 구성도")
for i in range(n):
    for j in range(m):
        print((array[i][j]), end=" ")
    print("\n")
print("다녀온 맵의 구성도")
for i in range(n):
    for j in range(m):
        print((d[i][j]), end=" ")
    print("\n")
print("방문한 칸의 수 :", count)
print("수행시간 :", end_time - start_time)
