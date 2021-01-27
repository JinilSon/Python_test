n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)    # sort(reverse=True)로 내림차순으로 정렬

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]     # 튜플 문법으로 값을 바꿈
    else:
        break

print(sum(a))

