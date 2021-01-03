from random import randint      # 난수 모듈
import time                     # 시간 모듈

array = []
for _ in range(10000):              # for _ in range() 에서 _는 인덱스 무시를 뜻한다.
    array.append(randint(1, 100))   # append()함수로 배열에 난수를 10000번 집어넣는다.

start_time = time.time()            # 성능 측정 시작

for i in range(len(array)):         # 선택 정렬 이중 for 문
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]      # 스와프(i값과 min_index 값이 다르면 배열의 값이 바뀐다.)

end_time = time.time()
print("선택 정렬 성능 측정 : ", end_time - start_time)              # 성능 측정 종료시간 - 시작시간


array = []                          # 배열 재 초기화
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정 : ", end_time - start_time)    # 성능 측정 종료시간 - 시작시간


