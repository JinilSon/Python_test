# sorted 함수는 병합 정렬로 퀵 정렬 보다는 느리지만 최악의 경우에도 O(NlogN)을 보장한다.
array = [7, 4, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

array.sort()
print(array)

# sorted()나 sort()를 이용할 때 key 매개변수를 입력으로 받을 수 있다.
# key 값으로는 하나의 함수가 들어가야 하며, 이는 정렬 기준이 된다.
array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]


def setting(data):
    return data[1]


result = sorted(array2, key=setting)
print(result)

# 정렬 라이브러리 문제 유형
# 정렬 라이브러리로 풀 수 있는 문제 : 단순히 숙지하고 있는지를 판단
# 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택 정렬, 삽입정렬, 퀵 정렬 등의 원리를 알아야 한다.
# 더 빠른 정렬이 필요한 문제 : 퀵 정렬 혹은 계수 정렬, 기수 정렬 등을 이용한 빠른 계산을 목표
