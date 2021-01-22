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
array2[0], array2[1] = array2[1], array2[0]         # 파이썬의 스와프 공식이다

print(array2)


# 삽입정렬
# 특정한 데이터가 적절한 위치에 들어가기 이전에 , 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다.
# 이전의 정렬된 데이터와 비교하여 적절한 위치에 위치시킨다.

array3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array3)):
    for j in range(i, 0, -1):   # 인덱스 i 부터 0까지 감소하며 반복
        if array3[j] < array3[j - 1]:
            array3[j], array3[j - 1] = array3[j - 1], array3[j]
        else:
            break

print(array3)
