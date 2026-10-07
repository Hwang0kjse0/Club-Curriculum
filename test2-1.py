# 입력 받기
n, m = map(int, input().split())

# 2차원 리스트가 될 빈 리스트 만들기
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# dfs 탐색을 수행하는 함수
def dfs(x, y):

    # 얼음 틀 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False # 정상 좌표가 아닐 시 False 반환

    # 아직 방문하지 않은 0이라면
    if graph[x][y] == 0:

        # 1로 바꿔 방문 처리하기
        graph[x][y] = 1

        # 상하좌우 탐색
        dfs(x - 1, y)  # 위
        dfs(x + 1, y)  # 아래
        dfs(x, y - 1)  # 왼쪽
        dfs(x, y + 1)  # 오른쪽

        return True

    # 1이거나 이미 방문한 곳
    return False

# 얼음 수 count
result = 0
# 얼음 틀의 모든 칸을 하나씩 확인
for i in range(n):
    for j in range(m):

        if dfs(i, j) == True:
            result += 1


print(result)
