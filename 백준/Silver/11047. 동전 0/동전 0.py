N, K = map(int,input().split())
data = []
result = 0
for i in range(N):
    data.append(int(input()))
data.sort(reverse=True)

for i in data:
    result += K//i
    K = K - (K//i)*i
print(result)