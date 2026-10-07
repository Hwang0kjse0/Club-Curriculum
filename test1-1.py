# 크기와 이동순서 입력 받기
n = int(input())
plans = input().split()

# 시작 위치
x = 1 
y = 1

for plan in plans:

    # 다음 위치 계산
    if plan == 'L':
        nx = x
        ny = y - 1

    elif plan == 'R':
        nx = x
        ny = y + 1

    elif plan == 'U':
        nx = x - 1
        ny = y

    elif plan == 'D':
        nx = x + 1
        ny = y

    # 범위를 벗어나면 저장하지 않고(무시하고) 다음 순서로 진행
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue # 반복을 끝내고 다음 반복으로 넘어가라

    # 범위를 벗어나지 않았을 때 현위치를 다음 위치로 변경
    x = nx
    y = ny

print(x, y)