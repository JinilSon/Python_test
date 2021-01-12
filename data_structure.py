from collections import deque

# 스택
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
print(stack)
print(stack[::-1])

# 큐
queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
queue.reverse()
print(queue)


# 재귀함수
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다')


recursive_function(1)


# 팩토리얼
def factorial_iterative(n):     # 반복적(for문 사용)
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):     # 재귀적(재귀함수 사용)
    if n <= 1:                      # 종료 조건(n이 0 또는 1일 때)
        return 1
    return n * factorial_recursive(n-1)     # n * 재귀함수(n-1)


print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

