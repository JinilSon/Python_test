# 퀵 정렬(퀵 정렬은 정렬 알고리즘 중에서 가장 많이 사용하는 정렬 알고리즘이다.)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 정렬(퀵 정렬과 비슷하게 빠른 알고리즘으로써는 병합 정렬이라는 알고리즘이 있다.)
# 퀵 정렬에서는 피벗(교환하기 위한 기준)을 사용한다.
# 피벗은 미리 명시해야 한다.
# 피벗 설정하고 리스트를 분할하는 방법에는 여러 가지 방식이 있는데, 가장 대표적인 분할방식은 호어 분할 방식이다.
# 리스트에서 첫 번째 데이터를 피벗으로 정한다.
# 이 후, 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 왼쪽의 큰 데이터와 오른쪽의 작은 데이터를 서로 교환한다, 이러한 과정을 반복한다.
# ## 왼쪽에서 찾는 데이터와 오른쪽에서 찾는 데이터가 교차될 경우, 작은 데이터와 피벗의 위치를 변경한다.
# 마지막으로, 피벗을 기준으로 왼쪽과 오른쪽 리스트로 구분하여 정렬을 다시 수행한다.
# 퀵 정렬의 평균 시간 복잡도는 O(NlogN) 이다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 시간 면에서는 비효율적이지만, 직관적인 식이다.
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살린 정렬 소스


def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 피벗보다 작은 x 값들로 이루어진 리스트
    right_side = [x for x in tail if x > pivot] # 피벗보다 큰 x  값들로 이루어진 리스트

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))
