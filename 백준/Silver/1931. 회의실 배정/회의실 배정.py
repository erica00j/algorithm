N = int(input())
data = []
count = 1
for i in range(N):
    a,b = map(int,input().split())
    data.append([a,b])
data.sort(key=lambda x:(x[1],x[0]))

end = data[0][1]
for i in range(1,N):
    if data[i][0]>=end:
        end = data[i][1]
        count += 1
print(count)