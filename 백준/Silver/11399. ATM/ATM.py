N = int(input())
data = list(map(int,input().split()))
data.sort()
result = 0
for i in range(len(data)):
    result += data[i]*(N-i)
print(result)