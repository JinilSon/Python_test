import time

h = int(input())
count = 0

start_time = time.time()

for h in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):     # in 연산자와 not in 연산자는 뒤에 오는 문자열에 앞의 문자열을 포함하고 있는 지를 반환한다.
                count += 1

end_time = time.time()

print("3이 들어가는 경우의 수 :", count, "번")
print("경과시간 :", end_time - start_time, "초")