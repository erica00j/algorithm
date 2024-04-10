n,m = map(int, input().split())
graph=[]

for _ in range(n):
    graph.append(list(map(int, input())))
#graph = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    # 아직 방문하지 않았다면
    if graph[x][y]==0:
        #방문처리
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    # 이미 방문했거나 벽인 경우
    return False

icecream = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            #print(i,j)
            icecream += 1

print(icecream)
