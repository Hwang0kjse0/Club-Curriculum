n, m = map(int, input().split())

rice_cakes = list(map(int, input().split()))

# 이진 탐색 범위
start = 0
end = max(rice_cakes)

# 최종 절단기 높이
result = 0

while start <= end:

    mid = (start + end) // 2

    total = 0

    # 높이 mid로 잘랐을 때 얻는 떡의 총 길이
    for cake in rice_cakes:

        if cake > mid:
            total += cake - mid

    # 떡이 부족하면 절단기 높이를 낮춤
    if total < m:
        end = mid - 1

    # 떡이 충분하면 더 높은 절단기 높이를 탐색
    else:
        result = mid
        start = mid + 1

print(result)