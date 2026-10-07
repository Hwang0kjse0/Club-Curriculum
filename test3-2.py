# queue 큐 불러오기
from collections import deque

n, m = map(int, input().split())

# 빈 2차원 리스트
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


# 거리 저장 배열 (최단 거리 기록하기)
distance = [[0] * m for _ in range(n)]


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():

    queue = deque()

    # 시작 위치 큐에 넣기
    queue.append((0, 0))
    # 시작 칸도 거리 1로 계산
    distance[0][0] = 1

    while queue:

        x, y = queue.popleft()

        # 상하좌우 확인
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물이 있는 곳이면 무시
            if graph[nx][ny] == 0:
                continue

            # 이미 방문한 곳이면 무시
            if distance[nx][ny] != 0:
                continue

            # 거리 기록
            distance[nx][ny] = distance[x][y] + 1

            # 다음 탐색을 위해 큐에 추가
            queue.append((nx, ny))


bfs()

print(distance[n - 1][m - 1])