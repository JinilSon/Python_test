n = 1260        # 1260원의 잔돈을 거슬러주어야 한다. (500원 ,100원, 50원, 10원 의 종류가 있고)
count = 0       # 잔돈은 무조건 10의 배수이다
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin  # python에서 //는 int값을, /는 float값을 반환한다. (coin의 값을 변화시키는 것이 아닌 coin의 값을 이용하여 count 값을 계산)
    n %= coin           # 위의 식에서 바꾸지 않은 coin의 변경사항(해당화폐로 거슬러 줄 수 있는 동전의 개수)을 적용

print(count)