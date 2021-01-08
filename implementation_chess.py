import time
# from random import randint

# x, y = randint(1, 8), randint(1, 8)   # 난수로 시작 위치를 지정할 경우
input_data = input()
x = int(ord(input_data[0]) - int(ord('a'))) + 1
y = int(input_data[1])

start_time = time.time()

# # test_algorithm
# #    RU  RD LU  LD  UR UL DR  DL
# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [-1, 1, -1, 1, -2, -2, 2, 2]

# correct_algorithm
#           RU      RD       LU        LD      UR        UL       DR       DL
steps = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]

count = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count += 1

# for i in range(len(dx)):
#     nx = x + dx[i]
#     ny = y + dy[i]
#
#     if nx < 1 or ny < 1 or nx > 8 or ny > 8:
#         continue
#
#     count += 1

end_time = time.time()

print("시작위치 :", input_data, "(", x, y, ")")
print("나이트의 움직일 수 있는 경우의 수 :", count)
print("경과시간 :", end_time - start_time, "초")
