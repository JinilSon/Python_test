n, m = map(int, input().split())    # n은 최소 화폐 개수, m

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)   # 10001로 구해야하는 수만큼의 배열 초기화

d[0] = 0
for i in range(n):
    for j in range(array[i], m + i):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
