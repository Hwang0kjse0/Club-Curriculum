n = int(input())
plans = input().split()

# 시작 위치
x, y = 1, 1

# L, R, U, D에 따른 x, y 변화량
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    # 현재 명령이 어떤 방향인지 찾기
    for i in range(4):

        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    # 공간을 벗어나면 이동하지 않음
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    # 이동
    x = nx
    y = ny

print(x, y)