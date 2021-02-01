# # 이진 탐색을 이용한 탐색
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# n = int(input())
# array = list(map(int, input().split()))
# array.sort()
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     result = binary_search(array, i, 0, n - 1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 계수 정렬을 이용한 탐색(100001개의 방을 생성한 후, 부품이 있는 index를 입력받아 값을 1로 초기화 시킨 후, 필요한 부품의 index를 입력받아 해당 인덱스의 배열 값이 1일 경우 yse, 아닐경우 no 출력)
# n = int(input())
# array = [0] * 100001
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 집합 자료형(set함수)를 사용한 예제
# 집합자료형은 파이썬 2.3부터 지원되는 자료형으로 인덱스가 없는 집합을 만든다
# 첫 번째 특징 : 집합 자료형은 순서를 가지지 않는다.
# 두 번째 특징 : 집합 자료형은 중복을 허용하지 않는다.
# 세 번째 특징 : 집합 자료형은 인덱싱이 되지 않는다
# 인덱싱을 하고 싶다면 list형이나 tuple형으로 변환 시켜 사용하면 된다.

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

