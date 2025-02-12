import sys
import heapq

def solve():
    input = sys.stdin.readline

    n,m,k = map(int,input().split())
    beer = []
    likes=[]

    for _ in range(k):
        a,b = map(int,input().split())
        beer.append((a,b))

    beer.sort(key=lambda x:x[1])
    hap = 0
    for i in beer:
        if len(likes) < n:
            heapq.heappush(likes,i)
            hap += i[0]
            if len(likes) == n:
                if hap >= m:
                    return i[1]
                else:
                    hap -= heapq.heappop(likes)[0]
    else:
        return -1

print(solve())