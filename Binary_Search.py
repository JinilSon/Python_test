# 이진탐색이란? : 리스트 내에서 데이터를 매우 빠르게 탐색하는 알고리즘(시간 복잡도는 O(logN))

# # 순차탐색(시간 복잡도는 O(N))
# #           n = 문자열의 길이, target = 찾으려는 문자열, array = 배열
# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i + 1
#
#
# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()        # 생성할 원소 개수와 문자열을 한 줄로 입력 받음
# n = int(input_data[0])
# target = input_data[1]
#
# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# array = input().split()             # 배열의 구성원을 입력받음
#
# print(sequential_search(n, target, array))


# # 이진탐색은 변수 3개(시작점, 끝점, 중간점)을 이용하여 반복적으로 비교하여 찾는 탐색과정이다.
# # 재귀함수를 이용한 구현
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
#
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print("해당하는 원소가 없습니다.")
# else:
#     print(result + 1)

# 반복문을 이용한 이진탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("해당하는 원소가 없습니다.")
else:
    print(result + 1)