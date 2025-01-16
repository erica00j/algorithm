import sys

N, M = map(int,sys.stdin.readline().split())
video = list(map(int,sys.stdin.readline().split()))

start = max(video)
end = sum(video)

while start <= end:
    count = 1
    sum_video = 0
    mid = (start+end)//2

    for i in video:
        if sum_video + i > mid:
            count += 1
            sum_video = 0
        sum_video += i

    if count <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)