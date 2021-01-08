import time

n, m, k = map(int, input().split())       # 공백으로 구분하여 입력으로 n, m, k를 받는다 ( map(type, 대상)은 대상을 type으로 변환해준다. )
data = list(map(int, input().split()))    # data값도 입력받아 map으로 변환 list로 배열화 시킨다.

start_time = time.time()                  # 보통 연산 횟수가 10억을 넘어가면 c언어를 기준으로 1초가 소요된다
                                          # So, n

data.sort()                               # 입력받은 수들 정렬하기
first = data[n-1]                         # 첫 번째 큰 수
second = data[n-2]                        # 두 번째 큰 수


# 가장 큰 수 가 더해진 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)


result = 0
result_count = 0
result_count += count * first
result_count += (m - count) * second

while True:
    for i in range(k):                  # 해당 수 최대 반복 횟수 만큼 첫 번째 큰 수를 더하고
        if m == 0:                        # but, 만약 해당 수 최대 반복 횟수 이전에 숫자가 더해져야되는 횟수가 0이 되면 break
            break
        result += first                 # 결과에 +
        m -= 1                          # 더한 횟수 -
    if m == 0:
        break
    result += second
    m -= 1

end_time = time.time()

print(result)
print(result_count)
print(end_time - start_time)            # 성능 측정