import heapq

# 방향 설정: 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dijkstra(n, graph):
    # 비용 테이블을 무한대로 초기화
    distance = [[float('inf')] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    # 우선순위 큐에 시작점 넣기 (비용, 좌표)
    queue = [(graph[0][0], 0, 0)]

    while queue:
        dist, x, y = heapq.heappop(queue)

        # 이미 처리된 노드면 무시
        if dist > distance[x][y]:
            continue

        # 4 방향으로 인접한 노드 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 현재 노드를 거쳐서 가는 것이 더 비용이 적다면 업데이트
                cost = dist + graph[nx][ny]

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(queue, (cost, nx, ny))

    return distance[n - 1][n - 1]

count = 1
while True:
    # 입력 처리
    n = int(input())
    if n==0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 다익스트라로 최단 경로 구하기
    result = dijkstra(n, graph)
    print(f"Problem {count}: {result}")
    count+=1