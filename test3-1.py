# queue 큐 불러오기
from collections import deque

n, m = map(int, input().split())

#빈 2차원 리스트
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


# 각 칸까지의 거리를 저장(최단 거리 기록하기)
distance = [[0] * m for _ in range(n)]


def bfs():

    queue = deque()

    # 시작 위치를 큐에 넣음
    queue.append((0, 0))

    # 시작 칸도 1칸으로 계산
    distance[0][0] = 1

    while queue:

        x, y = queue.popleft()

        # 위쪽
        nx = x - 1
        ny = y

# 다음 위치 범위 확인
        if 0 <= nx < n and 0 <= ny < m:
            # 갈 수 있는 칸 & 아직 방문하지 않은 칸
            if graph[nx][ny] == 1 and distance[nx][ny] == 0:
                # 거리 증가하기
                distance[nx][ny] = distance[x][y] + 1
                # 범위 내에 다음 위치에 넣기
                queue.append((nx, ny))


        # 아래쪽
        nx = x + 1
        ny = y

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


        # 왼쪽
        nx = x
        ny = y - 1

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


        # 오른쪽
        nx = x
        ny = y + 1

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


bfs()

print(distance[n - 1][m - 1])