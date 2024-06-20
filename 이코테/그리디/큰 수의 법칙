N,M,K = map(int,input().split())
data = list(map(int,input().split()))
result = 0
result += max(data)*int(M/K)*K
data.remove(max(data))
result += max(data)*(M-int(M/K)*K)
print(result)
