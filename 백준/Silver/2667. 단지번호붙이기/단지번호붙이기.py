N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
#graph = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0]]

def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = result+2
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            result += 1
print(result)

house = []
for i in range(result):
    count = 0
    for row in graph:
        count += row.count(i+2)
    house.append(count)
house = sorted(house)
for i in house:
    print(i)