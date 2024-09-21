N = int(input())

# 화단의 가격 정보를 입력받음
money_graph = [list(map(int, input().split())) for _ in range(N)]

# 방문 여부를 나타내는 리스트
visited = [[False] * N for _ in range(N)]

# 이동을 나타내는 배열 (꽃술에서 꽃잎이 퍼져나가는 방향)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 꽃을 심을 수 있는 위치인지 확인하는 함수
def can_place_flower(x, y):
    # 꽃술 자리
    if visited[x][y]:
        return False

    # 꽃잎 자리가 화단 범위를 넘거나 이미 다른 꽃과 겹치는지 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
            return False
    return True

# 꽃을 심고 비용을 계산하는 함수
def place_flower(x, y):
    cost = money_graph[x][y]
    visited[x][y] = True  # 꽃술 위치 방문 처리

    # 꽃잎이 퍼지는 4칸 방문 처리 및 비용 계산
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        visited[nx][ny] = True
        cost += money_graph[nx][ny]

    return cost

# 꽃을 제거하고 방문 처리를 되돌리는 함수
def remove_flower(x, y):
    visited[x][y] = False  # 꽃술 위치 방문 해제

    # 꽃잎이 퍼진 4칸 방문 해제
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        visited[nx][ny] = False

# 백트래킹을 통해 최소 비용을 구하는 함수
def backtrack(flower_count, current_cost):
    if flower_count == 3:  # 꽃 3개를 다 심었으면
        return current_cost

    min_cost = float('inf')

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if can_place_flower(i, j):
                # 꽃을 심고 비용 계산
                cost = place_flower(i, j)
                # 재귀 호출로 다음 꽃을 심음
                min_cost = min(min_cost, backtrack(flower_count + 1, current_cost + cost))
                # 꽃을 제거하여 원래 상태로 되돌림
                remove_flower(i, j)

    return min_cost

# 백트래킹 시작
result = backtrack(0, 0)
print(result)
