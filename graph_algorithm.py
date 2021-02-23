# DFS/BFS와 최단경로 알고리즘 모드 그래프 알고르지므에 해당된다
# 그래프란 노드와 노드 사이에 연결된 간선의 정보를 가지고 있는 자료구조를 의미한다.
# 알고리즘 문제를 접했을 때, 서로 다른 개체가 연결되어 있다는 이야기가 나오면 그래프 알고리즘을 떠올려야 한다.
# 그래프의 구현 방법 2가지(인접 행렬, 인접 리스트)
# 인접 행렬 방식은 간선 정보를 저장하기 위해 O(V의 제곱)의 메모리 공간이 필요
# 인접 리스트 방식은 O(E) 만큼의 메모리 공간이 필요
# 특정 노드에서 다른 특정 노드로의 간선의 비용을 인접행렬 방식은 O(1)의 시간으로 인접 리스트 방식은 O(V)만큼의 시간으로 알수 있다.

# 다익스트라 알고리즘은 인접행렬을 이용한 방식이고, 플로이드 워셜 알고리즘은 인접 리스트를 이용한 알고리즘이다.
# 노드의 개수가 많으면 다익스트라, 적으면 플로이드 워셜을 추천한다.

# 서로소 집합이란 공통 원소가 없는 두 집합을 의미한다.
# 서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조라고 할 수 있다.
# 서로소 집합 자료구조는 union과 find 2개의 연산으로 조작할 수 있다.
# union 연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이며,
# find 연산은 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다.

# 서로소 집합 자료구조는 트리자료구조를 이용하여 집합을 표현
# 1. union 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
#           A와 B의 루트 노드 A', B'를 각각 찾는다.
#           A'를 B'의 부모 노드로 설정한다.(B'가 A'를 가르키도록)
# 2. 모든 union 연산을 처리할 때까지, 1번 과정을 반복한다.

# 기본적인 서로소 집합 알고리즘
def find_parent(parent, x):
    if parent[x] != x:                              # 루트 노드를 찾을 때까지 재귀적으로 호출
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):                            # parent 노드 리스트 초기화
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end=' ')                 # 각 원소가 속한 집합은 연결되어 있는 서로소 들의 집합에서 제일 작은 수를 지칭
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end=' ')                        # 부모 테이블이란, 연결된 서로소 집합 중 작은 수들을 표출
for i in range(1, v + 1):
    print(parent[i], end=' ')



# 위의 코드는 find 함수가 1, 2, 3, 4, 5 순서대로 처리를 함으로써 비효율적이다 ( O(VM))
# 이는 경로 압축기법으로 바로 개선시킬 수 있다

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 서로소 집합은 다양한 알고리즘에 사용될 수 있다.
# 서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다는 특징이 있다.
# ( 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별가능하다)
# 서로소 집합을 활용한 사이클 판별
# 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
#   루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
#   루트 노드가 서로 같다면 사이클이 발생한 것이다.
# 2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 수행한다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        return parent[x]


def union_parent(parent ,a ,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)      # 부모 테이블 초기화

for i in range(1, v + 1):   # 부모 테이블 상에서, 자기 자신으로 초기화
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent ,b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클 발생!")
else:
    print("사이클이 발생하지 않았습니다.")