N,M = map(int,input().split())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))
print(data)

a = []
for i in range(len(data)):
    a.append(min(data[i]))

print(max(a))
