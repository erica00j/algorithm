K, N = map(int,input().split())
length = []
for i in range(K):
    length.append(int(input()))

start = 1
end = max(length)

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in length:
        count += i//mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)