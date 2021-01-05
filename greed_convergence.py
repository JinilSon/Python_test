import time

count = 0
n, k = map(int, input().split())
start_time = time.time()
while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1


end_time = time.time()

print(str(end_time - start_time) + "초")
print(str(count) + "번")