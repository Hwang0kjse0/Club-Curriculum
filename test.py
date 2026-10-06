n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):

    # 얼음 틀 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 아직 방문하지 않은 0이라면
    if graph[x][y] == 0:

        # 방문 처리
        graph[x][y] = 1

        # 상하좌우 탐색
        dfs(x - 1, y)  # 위
        dfs(x + 1, y)  # 아래
        dfs(x, y - 1)  # 왼쪽
        dfs(x, y + 1)  # 오른쪽

        return True

    # 1이거나 이미 방문한 곳
    return False


result = 0

for i in range(n):
    for j in range(m):

        if dfs(i, j) == True:
            result += 1


print(result)
