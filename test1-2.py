# 크기와 이동순서 입력 받기
n = int(input())
plans = input().split()

# 시작 위치
x, y = 1, 1

# L, R, U, D에 따른 x, y 변화량
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    # 현재 명령이 어떤 방향인지 찾기 (0~3)
    for i in range(4):

        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    # 범위를 벗어나면 저장하지 않고(무시하고) 다음 순서로 진행
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    # 범위를 벗어나지 않았을 때 현위치를 다음 위치로 변경
    x = nx
    y = ny

print(x, y)