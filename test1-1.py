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

    # 공간을 벗어나면 이동하지 않음
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    # 이동 가능하면 현재 위치를 변경
    x = nx
    y = ny

print(x, y)