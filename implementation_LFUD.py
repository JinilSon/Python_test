from random import randint
import time


# N X N 의 정사각형 공간 위에서 상하좌우를 입력받아 공간 안에서 움직이는 알고리즘을 만들어라. 공간을 벗어나면 해당 값을 무시해야 한다.
n = int(input())
plans = input().split()
start_time = time.time()

x, y = randint(1, n), randint(1, n)
nx, ny = 0, 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']                   # python의 배열은 [](대괄호)로 정의한다.

print("스타트 지점 :", x, y)

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:        # continue는 해당 반복문의 남은 명령을 수행하지 않고 반복문의 차례를 다음으로 넘기는 명령이다
        print("진행 무시!")
        continue

    x, y = nx, ny
    print("현재 위치 :", x, y)

end_time = time.time()
print("\n최종위치 :", x, y)
print("소요시간 :", end_time - start_time, "초")
