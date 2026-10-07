n, m = map(int, input().split())

rice_cakes = list(map(int, input().split()))

# 절단시 높이 = 가장 높은 떡
height = max(rice_cakes)

while height >= 0:
 # 잘린 떡을 전부 더한 값(count)
    total = 0

    for cake in rice_cakes:

        if cake > height:
            total += cake - height

    if total >= m:
        print(height)
        break

    height -= 1