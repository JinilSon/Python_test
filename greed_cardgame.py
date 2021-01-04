import time
# 각 행의 가장 작은 수들 중 가장 큰 수를 구하는 알고리즘
n, m = map(int, input().split())        # 열, 행을 입력받는다( n x m )

start_time = time.time()

result = 0
for i in range(n):
    data = list(map(int, input().split()))  # 각 행들의 카드 내용을 입력받는다
    min_value = min(data)                   # 행의 최소값 차출
    result = max(result, min_value)         # 이전 최소값과 비교하여 크면 result 변수에 저장

'''
    # 2중 for문을 사용하는 경우
    min_value = 10001   # 해당 카드 내용보다 크기가 매우 큰 수를 기입
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
'''
end_time = time.time()

print(result)
print(end_time - start_time)