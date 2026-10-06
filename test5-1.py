n, m = map(int, input().split())

rice_cakes = list(map(int, input().split()))

height = max(rice_cakes)

while height >= 0:

    total = 0

    for cake in rice_cakes:

        if cake > height:
            total += cake - height

    if total >= m:
        print(height)
        break

    height -= 1