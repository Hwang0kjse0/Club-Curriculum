#입력 받기
n, m = map(int, input().split())
#2차원 리스트가 될 빈 리스트 만들기
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    # 범위를 벗어나면 탐색 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 아직 방문하지 않은 곳이라면
    if graph[x][y] == 0:

        # 방문 처리
        graph[x][y] = 1

        # 상하좌우 탐색
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)

        return True

    return False


result = 0

for i in range(n):
    for j in range(m):

        if dfs(i, j):
            result += 1


print(result)