# 선택정렬 Selection Sorting
# : 가장 작은 수를 앞으로 보내는 방법을 반복함

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):  # i + 1 은 j의 시작 인덱스
        if array[min_index] > array[j]: # j 번째 배열의 값이 i 번째 배열의 값보다 작다면 j 번째 배열의 값이 최솟값이다.
            min_index = j
        array[i], array[min_index] = array[min_index], array[i]

print(array)

array2 = [3, 5]
array[0], array[1] = array[1], array[0]         # 파이썬의 스와프 공식이다

print(array2)
