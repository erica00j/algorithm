M = int(input())
N = 1000 - M
count=0
coin = [500,100,50,10,5,1]
for i in coin:
    count+=int(N/i)
    N = N - i*int(N/i)
print(count)