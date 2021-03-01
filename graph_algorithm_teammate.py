def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)              # 부모 테이블 초기화

for i in range(0, n + 1):           # 부모 테이블 자기 자신의 값으로 초기화
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합 연산인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')